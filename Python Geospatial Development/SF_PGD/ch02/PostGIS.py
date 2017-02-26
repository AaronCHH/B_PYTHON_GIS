import psycopg2

import time
startTime = time.time()

connection = psycopg2.connect("dbname=... user=...")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS gshhs")
cursor.execute("""CREATE TABLE gshhs (
                    id      SERIAL,
                    level   INTEGER,

                    PRIMARY KEY (id))
               """)
cursor.execute("CREATE INDEX levelIndex ON gshhs(level)")
cursor.execute("SELECT AddGeometryColumn('gshhs', " +
                         "'geom', 4326, 'POLYGON', 2)")
cursor.execute("CREATE INDEX geomIndex ON gshhs " +
               "USING GIST (geom)")
connection.commit()

#######################

import os.path
from osgeo import ogr

for level in [1, 2, 3, 4]:
    fName = os.path.join("GSHHS_l",
                         "GSHHS_l_L"+str(level)+".shp")
    shapefile = ogr.Open(fName)
    layer = shapefile.GetLayer(0)
    for i in range(layer.GetFeatureCount()):
        feature = layer.GetFeature(i)
        geometry = feature.GetGeometryRef()
        wkt = geometry.ExportToWkt()

        cursor.execute("INSERT INTO gshhs (level, geom) " +
                       "VALUES (%s, ST_GeomFromText(%s, " +
                       "4326))", (level, wkt))
    connection.commit()

#######################

old_level = connection.isolation_level
connection.set_isolation_level(0)
cursor.execute("VACUUM ANALYZE")
connection.set_isolation_level(old_level)

#######################

LONDON = 'POINT(-0.1263 51.4980)'

cursor.execute("SELECT id,ST_AsText(geom) FROM gshhs " +
               "WHERE (level=%s) AND " +
               "(ST_Contains(geom, ST_GeomFromText(%s, 4326)))",
               (1, LONDON))

shoreline = None
for id,wkt in cursor:
    shoreline = wkt

#########################

f = file("uk-shoreline.wkt", "w")
f.write(shoreline)
f.close()

endTime = time.time()
print "Took %0.4f seconds" % (endTime-startTime)

