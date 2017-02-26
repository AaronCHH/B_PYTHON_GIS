import os.path
import pyproj
import MySQLdb

connection = MySQLdb.connect(user="...", passwd="...")
cursor = connection.cursor()
cursor.execute("USE distal")
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
                       "(name, position) VALUES (%s, " +
                       "GeomFromWKB(Point(%s, %s), 4326))",
                       (featureName, long, lat))

        num_inserted += 1
        if num_inserted % 1000 == 0:
            connection.commit()
f.close()
connection.commit()
