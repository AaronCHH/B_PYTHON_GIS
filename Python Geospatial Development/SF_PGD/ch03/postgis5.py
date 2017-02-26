import os.path
import psycopg2
connection = psycopg2.connect("dbname=distal user=... password=...")
cursor = connection.cursor()
cursor.execute("SET NAMES 'utf8'")

num_inserted = 0

f = file(os.path.join("DISTAL-data",
                      "geonames_dd_dms_date_20121126.txt"),
         "r")

heading = f.readline() # Ignore field names.

for line in f.readlines():
    parts = line.rstrip().split("\t")
    lat = float(parts[3])
    long = float(parts[4])
    featureClass = parts[9]
    featureDesignation = parts[10]
    nameType = parts[17]
    featureName = parts[22]

    if (featureClass == "P" and nameType == "N" and
        featureDesignation in ["PPL", "PPLA", "PPLC"]):
        cursor.execute("INSERT INTO places " +
                       "(name, position) VALUES (%s, " +
                       "ST_SetSRID(" +
                       "ST_MakePoint(%s,%s), 4326))",
                       (featureName, long, lat))

        num_inserted += 1
        if num_inserted % 1000 == 0:
            connection.commit()

f.close()
connection.commit()
