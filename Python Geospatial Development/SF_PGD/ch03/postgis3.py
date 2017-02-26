import os.path
import psycopg2
import osgeo.ogr

connection = psycopg2.connect("dbname=distal user=... password=...")
cursor = connection.cursor()

cursor.execute("DELETE FROM shorelines")

for level in [1, 2, 3, 4]:
    srcFile = os.path.join("DISTAL-data", "GSHHS_shp", "f",
                           "GSHHS_f_L" + str(level) + ".shp")
    shapefile = osgeo.ogr.Open(srcFile)
    layer = shapefile.GetLayer(0)

    for i in range(layer.GetFeatureCount()):
        feature = layer.GetFeature(i)
        wkt = feature.GetGeometryRef().ExportToWkt()

        cursor.execute("INSERT INTO shorelines " +
                       "(level,outline) VALUES " +
                       "(%s, ST_GeometryFromText(%s, 4326))",
                       (level, wkt))

    connection.commit()

