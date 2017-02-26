import os.path
from pysqlite2 import dbapi2 as sqlite
import osgeo.ogr

db = sqlite.connect("distal.db")
db.enable_load_extension(True)
db.execute('SELECT load_extension("...")')
cursor = db.cursor()

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
                       "(?, ST_PolygonFromText(?, 4326))",
                       (level, wkt))

    db.commit()

