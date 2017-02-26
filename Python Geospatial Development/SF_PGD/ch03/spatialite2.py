import os, os.path
from pysqlite2 import dbapi2 as sqlite
import osgeo.ogr

db = sqlite.connect("distal.db")
db.enable_load_extension(True)
db.execute('SELECT load_extension("...")')
cursor = db.cursor()

cursor.execute("DELETE FROM countries")

srcFile = os.path.join("DISTAL-data", "TM_WORLD_BORDERS-0.3",
                       "TM_WORLD_BORDERS-0.3.shp")
shapefile = osgeo.ogr.Open(srcFile)
layer = shapefile.GetLayer(0)

for i in range(layer.GetFeatureCount()):
    feature = layer.GetFeature(i)
    name = feature.GetField("NAME").decode("Latin-1")
    wkt = feature.GetGeometryRef().ExportToWkt()

    cursor.execute("INSERT INTO countries (name,outline) " +
                   "VALUES (?, ST_PolygonFromText(?, " +
                   "4326))", (name, wkt))

db.commit()

