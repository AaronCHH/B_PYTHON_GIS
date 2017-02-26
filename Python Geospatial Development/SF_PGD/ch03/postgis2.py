import os.path
import psycopg2
import osgeo.ogr

connection = psycopg2.connect("dbname=distal user=... password=...")
cursor = connection.cursor()

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
                   "VALUES (%s, ST_GeometryFromText(%s, " +
                   "4326))", (name.encode("utf8"), wkt))

connection.commit()

