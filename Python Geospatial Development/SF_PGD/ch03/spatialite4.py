import codecs
import os.path
import pyproj
from pysqlite2 import dbapi2 as sqlite

db = sqlite.connect("distal.db")
db.enable_load_extension(True)
db.execute('SELECT load_extension("...")')
cursor = db.cursor()
cursor.execute("DELETE from places")

num_inserted = 0

srcProj = pyproj.Proj(proj='longlat', ellps='GRS80',
                      datum='NAD83')
dstProj = pyproj.Proj(proj='longlat', ellps='WGS84',
                      datum='WGS84')

f = file(os.path.join("DISTAL-data",
                      "NationalFile_20121001.txt"), "r")
heading = f.readline() # Ignore field names.
for line in f.readlines():
    parts = line.rstrip().split("|")
    featureName = parts[1]
    featureClass = parts[2]
    lat = float(parts[9])
    long = float(parts[10])

    if featureClass == "Populated Place":
        long,lat = pyproj.transform(srcProj, dstProj,
                                    long, lat)
        cursor.execute("INSERT INTO places " +
                       "(name, position) VALUES "
                       "(?, MakePoint(?, ?, 4326))",
                       (featureName.decode("utf-8"), long, lat))

        num_inserted += 1
        if num_inserted % 1000 == 0:
            db.commit()
f.close()
db.commit()
