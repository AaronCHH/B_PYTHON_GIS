import os, os.path
from pysqlite2 import dbapi2 as sqlite

import time
startTime = time.time()

if os.path.exists("gshhs-spatialite.db"):
    os.remove("gshhs-spatialite.db")

db = sqlite.connect("gshhs-spatialite.db")
#db.enable_load_extension(True)
#db.execute('SELECT load_extension("libspatialite-2.dll")')
cursor = db.cursor()

cursor.execute("SELECT InitSpatialMetaData()")

#######################

cursor.execute("DROP TABLE IF EXISTS gshhs")
cursor.execute("CREATE TABLE gshhs (" +
               "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
               "level INTEGER)")
cursor.execute("CREATE INDEX gshhs_level on gshhs(level)")
cursor.execute("SELECT AddGeometryColumn('gshhs', 'geom', " +
               "4326, 'POLYGON', 2)")
cursor.execute("SELECT CreateSpatialIndex('gshhs', 'geom')")
db.commit()

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
                       "VALUES (?, GeomFromText(?, 4326))",
                       (level, wkt))
    db.commit()

#######################

import shapely.wkt

LONDON = 'POINT(-0.1263 51.4980)'
pt = shapely.wkt.loads(LONDON)

#cursor.execute("EXPLAIN QUERY PLAN " +
#               "SELECT id,level,AsText(geom) " +
#               "FROM gshhs WHERE id IN " +
#               "(SELECT pkid FROM idx_gshhs_geom" + 
#               " WHERE xmin <= ? AND ? <= xmax" +
#               " AND ymin <= ? and ? <= ymax) " +
#               "AND Contains(geom, GeomFromText(?, 4326))",
#               (pt.x, pt.x, pt.y, pt.y, LONDON))
#for row in cursor:
#    print row

cursor.execute("SELECT id,level,AsText(geom) " +
               "FROM gshhs WHERE id IN " +
               "(SELECT pkid FROM idx_gshhs_geom" + 
               " WHERE xmin <= ? AND ? <= xmax" +
               " AND ymin <= ? and ? <= ymax) " +
               "AND Contains(geom, GeomFromText(?, 4326))",
               (pt.x, pt.x, pt.y, pt.y, LONDON))

shoreline = None
for id,level,wkt in cursor:
    if level == 1:
        shoreline = wkt

#########################

f = file("uk-shoreline.wkt", "w")
f.write(shoreline)
f.close()

endTime = time.time()
print "Took %0.4f seconds" % (endTime-startTime)

