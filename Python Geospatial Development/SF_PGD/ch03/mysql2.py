import os.path
import MySQLdb
import osgeo.ogr

connection = MySQLdb.connect(user="...", passwd="...")
cursor = connection.cursor()

cursor.execute("USE distal")
cursor.execute("DELETE FROM countries")
cursor.execute("SET GLOBAL max_allowed_packet=52428800")

srcFile = os.path.join("DISTAL-data", "TM_WORLD_BORDERS-0.3",
                       "TM_WORLD_BORDERS-0.3.shp")
shapefile = osgeo.ogr.Open(srcFile)
layer = shapefile.GetLayer(0)

for i in range(layer.GetFeatureCount()):
    feature = layer.GetFeature(i)
    name = feature.GetField("NAME").decode("Latin-1")
    wkt = feature.GetGeometryRef().ExportToWkt()

    cursor.execute("INSERT INTO countries (name,outline) " +
                   "VALUES (%s, PolygonFromText(%s, 4326))",
                   (name.encode("utf8"), wkt))

connection.commit()

