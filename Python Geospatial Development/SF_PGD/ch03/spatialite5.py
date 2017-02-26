import os.path
from pysqlite2 import dbapi2 as sqlite
db = sqlite.connect("distal.db")
db.enable_load_extension(True)
db.execute('SELECT load_extension("...")')
cursor = db.cursor()

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
                       "(name, position) VALUES "
                       "(?, MakePoint(?, ?, 4326))",
                       (featureName.decode("utf-8"),
                        long, lat))

        num_inserted += 1
        if num_inserted % 1000 == 0:
            db.commit()

f.close()
db.commit()
