# database.py

import os.path
import pyproj
from shapely.geometry import Polygon
import shapely.wkt

#############################################################################
# Edit these constants as necessary for your setup.

MYSQL_DBNAME   = "distal"
MYSQL_USERNAME = "XXX"
MYSQL_PASSWORD = "XXX"

POSTGIS_DBNAME   = "distal"
POSTGIS_USERNAME = "XXX"
POSTGIS_PASSWORD = "XXX"

SPATIALITE_DB_PATH = os.path.join(os.path.dirname(__file__),
                                  "..", "distal.db")

DB_TYPE = "XXX" # One of: MySQL, PostGIS or SpatiaLite.

#############################################################################

def open():
    global _connection, _cursor

    if DB_TYPE == "MySQL":
        import MySQLdb
        _connection = MySQLdb.connect(user=MYSQL_USERNAME,
                                      passwd=MYSQL_PASSWORD)
        _cursor = _connection.cursor()
        _cursor.execute("USE "+MYSQL_DBNAME)
    elif DB_TYPE == "PostGIS":
        import psycopg2
        params = []
        params.append("dbname=" + POSTGIS_DBNAME)
        if POSTGIS_USERNAME not in ["", None]:
            params.append("user=" + POSTGIS_USERNAME)
        if POSTGIS_PASSWORD not in ["", None]:
            params.append("password=" + POSTGIS_PASSWORD)
        _connection = psycopg2.connect(" ".join(params))
        _cursor = _connection.cursor()
    elif DB_TYPE == "SpatiaLite":
        from pysqlite2 import dbapi2 as sqlite
        _connection = sqlite.connect(SPATIALITE_DB_PATH)
#        _connection.enable_load_extension(True)
#        _connection.execute('SELECT load_extension("...")')
        _cursor = _connection.cursor()
    else:
        raise RuntimeError("Unknown database type: " + DB_TYPE)

#############################################################################

def list_countries():
    global _cursor
    results = []
    _cursor.execute("SELECT id,name FROM countries ORDER BY name")
    for id,name in _cursor:
        if DB_TYPE == "SpatiaLite":
            name = name.encode("utf-8")
        results.append((id, name))
    return results

#############################################################################

def get_country_details(country_id):
    global _cursor

    if DB_TYPE == "MySQL":
        _cursor.execute("SELECT name," +
                        "AsText(Envelope(outline)) " +
                        "FROM countries WHERE id=%s",
                        (country_id,))
    elif DB_TYPE == "PostGIS":
        _cursor.execute("SELECT name," +
                        "ST_AsText(ST_Envelope(outline)) " +
                        "FROM countries WHERE id=%s",
                        (country_id,))
    elif DB_TYPE == "SpatiaLite":
        _cursor.execute("SELECT name," +
                        "ST_AsText(ST_Envelope(outline)) " +
                        "FROM countries WHERE id=?",
                        (country_id,))

    row = _cursor.fetchone()
    if row != None:
        return {'name'       : row[0],
                'bounds_wkt' : row[1]}
    else:
        return None

#############################################################################

def get_country_datasource():
    if DB_TYPE == "MySQL":
        vrtFile = os.path.join(os.path.dirname(__file__),
                               "countries.vrt")
        f = file(vrtFile, "w")
        f.write('<OGRVRTDataSource>\n')
        f.write('  <OGRVRTLayer name="countries">\n')
        f.write('    <SrcDataSource>MYSQL:' + MYSQL_DBNAME)
        if MYSQL_USERNAME not in ["", None]:
            f.write(",user=" + MYSQL_USERNAME)
        if MYSQL_PASSWORD not in ["", None]:
            f.write(",passwd=" + MYSQL_PASSWORD)
        f.write(',tables=countries</SrcDataSource>\n')
        f.write('    <SrcSQL>\n')
        f.write('      SELECT id,outline FROM countries\n')
        f.write('    </SrcSQL>\n')
        f.write('  </OGRVRTLayer>\n')
        f.write('</OGRVRTDataSource>\n')
        f.close()

        return {'type'  : "OGR",
                'file'  : vrtFile,
                'layer' : "countries"}
    elif DB_TYPE == "PostGIS":
        return {'type'     : "PostGIS",
                'dbname'   : "distal",
                'table'    : "countries",
                'user'     : POSTGIS_USERNAME,
                'password' : POSTGIS_PASSWORD}
    elif DB_TYPE == "SpatiaLite":
        return {'type'           : "SQLite",
                'file'           : SPATIALITE_DBNAME,
                'table'          : "countries",
                'geometry_field' : "outline",
                'key_field'      : "id"}

#############################################################################

def find_places_within(startLat, startLong, searchRadius):
    global _cursor

    geod = pyproj.Geod(ellps="WGS84")

    x,y,angle = geod.fwd(startLong, startLat, 0,
                         searchRadius)
    maxLat = y

    x,y,angle = geod.fwd(startLong, startLat, 90,
                         searchRadius)
    maxLong = x

    x,y,angle = geod.fwd(startLong, startLat, 180,
                         searchRadius)
    minLat = y

    x,y,angle = geod.fwd(startLong, startLat, 270,
                         searchRadius)
    minLong = x

    if DB_TYPE == "MySQL":
        p = Polygon([(minLong, minLat), (maxLong, minLat),
                     (maxLong, maxLat), (minLong, maxLat),
                     (minLong, minLat)])
        wkt = shapely.wkt.dumps(p)
        _cursor.execute("SELECT name,X(position),Y(position) " +
                        "FROM places WHERE MBRContains(" +
                        "GeomFromText(%s), position)", (wkt,))
    elif DB_TYPE == "PostGIS":
        p = Polygon([(minLong, minLat), (maxLong, minLat),
                     (maxLong, maxLat), (minLong, maxLat),
                     (minLong, minLat)])
        wkt = shapely.wkt.dumps(p)
        _cursor.execute("SELECT name,ST_X(position),ST_Y(position) " +
                        "FROM places WHERE ST_CONTAINS(" +
                        "ST_GeomFromText(%s, 4326), position)",
                        (wkt,))
    elif DB_TYPE == "SpatiaLite":
        _cursor.execute("SELECT name,X(position),Y(position) " +
                        "FROM places WHERE id in (SELECT pkid " +
                        "FROM idx_places_position " +
                        "WHERE xmin >= ? AND xmax <= ? " +
                        "AND ymin >= ? and ymax <= ?)",
                        (minLong, maxLong, minLat, maxLat))

    places = [] # List of (long, lat, name) tuples.

    geod = pyproj.Geod(ellps="WGS84")

    for row in _cursor:
        name,long,lat = row
        angle1,angle2,distance = geod.inv(startLong, startLat,
                                          long, lat)
        if distance > searchRadius: continue

        places.append([long, lat, name])

    return {'places'  : places,
            'minLat'  : minLat,
            'minLong' : minLong,
            'maxLat'  : maxLat,
            'maxLong' : maxLong}

#############################################################################

def get_shoreline_datasource():
    if DB_TYPE == "MySQL":
        vrtFile = os.path.join(os.path.dirname(__file__),
                               "shorelines.vrt")
        f = file(vrtFile, "w")
        f.write('<OGRVRTDataSource>\n')
        f.write('  <OGRVRTLayer name="shorelines">\n')
        f.write('    <SrcDataSource>MYSQL:' + MYSQL_DBNAME)
        if MYSQL_USERNAME not in ["", None]:
            f.write(",user=" + MYSQL_USERNAME)
        if MYSQL_PASSWORD not in ["", None]:
            f.write(",passwd=" + MYSQL_PASSWORD)
        f.write(',tables=shorelines</SrcDataSource>\n')
        f.write('    <SrcSQL>\n')
        f.write('      SELECT id,outline FROM shorelines ' +
                                        'WHERE level=1\n')
        f.write('    </SrcSQL>\n')
        f.write('  </OGRVRTLayer>\n')
        f.write('</OGRVRTDataSource>\n')
        f.close()

        return {'type'  : "OGR",
                'file'  : vrtFile,
                'layer' : "shorelines"}
    elif DB_TYPE == "PostGIS":
        return {'type'     : "PostGIS",
                'dbname'   : "distal",
                'table'    : "shorelines",
                'user'     : POSTGIS_USERNAME,
                'password' : POSTGIS_PASSWORD}
    elif DB_TYPE == "SpatiaLite":
        return {'type'           : "SQLite",
                'file'           : SPATIALITE_DBNAME,
                'table'          : "shorelines",
                'geometry_field' : "outline",
                'key_field'      : "id"}

#############################################################################

def load_shorelines():
    global _cursor

    shorelines = []

    if DB_TYPE == "MySQL":
        _cursor.execute("SELECT AsText(outline) " +
                        "FROM shorelines WHERE level=1")
    elif DB_TYPE == "PostGIS":
        _cursor.execute("SELECT ST_AsText(outline) " +
                        "FROM shorelines WHERE level=1")
    elif DB_TYPE == "SpatiaLite":
        _cursor.execute("SELECT ST_AsText(outline) " +
                        "FROM shorelines WHERE level=1")

    for row in _cursor:
        outline = shapely.wkt.loads(row[0])
        shorelines.append(outline)

    return shorelines

#############################################################################

def create_tile_tables():
    global _cursor, _connection

    if DB_TYPE == "MySQL":
        _cursor.execute("""
            CREATE TABLE IF NOT EXISTS tiled_shorelines (
                intLat  INTEGER,
                intLong INTEGER,
                outline GEOMETRY,

                PRIMARY KEY (intLat, intLong))
        """)
    elif DB_TYPE == "PostGIS":
        _cursor.execute("DROP TABLE IF EXISTS tiled_shorelines")
        _cursor.execute("""
            CREATE TABLE tiled_shorelines (
                intLat  INTEGER,
                intLong INTEGER,

                PRIMARY KEY (intLat, intLong))
        """)
        _cursor.execute("""
            SELECT AddGeometryColumn('tiled_shorelines', 'outline',
                                     4326, 'GEOMETRY', 2)
        """)
        _cursor.execute("""
            CREATE INDEX tiledShorelineIndex ON tiled_shorelines
                USING GIST(outline)
        """)
    elif DB_TYPE == "SpatiaLite":
        _cursor.execute("DROP TABLE IF EXISTS tiled_shorelines")
        _cursor.execute("""
            CREATE TABLE tiled_shorelines (
                intLat  INTEGER,
                intLong INTEGER,
                PRIMARY KEY (intLat, intLong))
        """)
        _cursor.execute("""
            SELECT AddGeometryColumn('tiled_shorelines', 'outline',
                                     4326, 'GEOMETRY', 2)
        """)
        _cursor.execute("""
            SELECT CreateSpatialIndex('tiled_shorelines', 'outline')
        """)

    _connection.commit()

#############################################################################

def save_tiled_shoreline(iLat, iLong, outline_wkt):
    global _cursor, _connection

    if DB_TYPE == "MySQL":
        _cursor.execute("INSERT INTO tiled_shorelines " +
                        "(intLat, intLong, outline) " +
                        "VALUES (%s, %s, GeomFromText(%s))",
                        (iLat, iLong, outline_wkt))
    elif DB_TYPE == "PostGIS":
        _cursor.execute("INSERT INTO tiled_shorelines " +
                        "(intLat, intLong, outline) " +
                        "VALUES (%s, %s, ST_GeomFromText(%s, 4326))",
                        (iLat, iLong, outline_wkt))
    elif DB_TYPE == "SpatiaLite":
        _cursor.execute("INSERT INTO tiled_shorelines " +
                        "(intLat, intLong, outline) " +
                        "VALUES (?, ?, ST_GeomFromText(%s, 4326))",
                        (iLat, iLong, outline_wkt))

    _connection.commit()

#############################################################################

def get_tiled_shoreline_datasource(iLat, iLong):
    if DB_TYPE == "MySQL":
        vrtFile = os.path.join(os.path.dirname(__file__),
                               "shorelines.vrt")
        f = file(vrtFile, "w")
        f.write('<OGRVRTDataSource>\n')
        f.write('  <OGRVRTLayer name="shorelines">\n')
        f.write('    <SrcDataSource>MYSQL:' + MYSQL_DBNAME)
        if MYSQL_USERNAME not in ["", None]:
            f.write(",user=" + MYSQL_USERNAME)
        if MYSQL_PASSWORD not in ["", None]:
            f.write(",passwd=" + MYSQL_PASSWORD)
        f.write(',tables=tiled_shorelines</SrcDataSource>\n')
        f.write('    <SrcSQL>\n')
        f.write('      SELECT outline FROM tiled_shorelines WHERE ' +
                      '(intLat=%d) AND (intlong=%d)' % (iLat, iLong) +
                      '\n')
        f.write('    </SrcSQL>\n')
        f.write('  </OGRVRTLayer>\n')
        f.write('</OGRVRTDataSource>\n')
        f.close()

        return {'type'  : "OGR",
                'file'  : vrtFile,
                'layer' : "shorelines"}
    elif DB_TYPE == "PostGIS":
        sql = "(SELECT outline FROM tiled_shorelines" \
            + " WHERE (intLat=%d) AND (intLong=%d)) " \
            % (iLat, iLong) + "AS shorelines"

        return {'type'                 : "PostGIS",
                'dbname'               : "distal",
                'table'                : sql,
                'extent_from_subquery' : True,
                'user'                 : POSTGIS_USERNAME,
                'password'             : POSTGIS_PASSWORD}
    elif DB_TYPE == "SpatiaLite":
        sql = "(SELECT outline FROM tiled_shorelines" \
            + " WHERE (intLat=%d) AND (intLong=%d)) " \
            % (iLat, iLong) + "AS shorelines"

        return {'type'           : "SQLite",
                'file'           : SPATIALITE_DBNAME,
                'table'          : sql,
                'geometry_field' : "outline",
                'key_field'      : "id"}

