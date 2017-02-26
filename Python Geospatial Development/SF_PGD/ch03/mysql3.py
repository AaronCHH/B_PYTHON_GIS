import os.path
import MySQLdb
import osgeo.ogr

connection = MySQLdb.connect(user="...", passwd="...")
cursor = connection.cursor()

cursor.execute("USE distal")
cursor.execute("DELETE FROM shorelines")
cursor.execute("SET GLOBAL max_allowed_packet=52428800")

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
                       "(%s, PolygonFromText(%s, 4326))",
                       (level, wkt))

    connection.commit()

