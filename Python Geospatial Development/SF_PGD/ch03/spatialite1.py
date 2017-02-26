import os, os.path
from pysqlite2 import dbapi2 as sqlite

if os.path.exists("distal.db"):
    os.remove("distal.db")

db = sqlite.connect("distal.db")
db.enable_load_extension(True)
db.execute('SELECT load_extension("...")')
cursor = db.cursor()

# Initialize the SpatiaLite meta-tables.

cursor.execute('SELECT InitSpatialMetaData()')

# Create the database tables.

cursor.execute("DROP TABLE IF EXISTS countries")
cursor.execute("""
    CREATE TABLE countries (
        id   INTEGER PRIMARY KEY AUTOINCREMENT,
        name CHAR(255))
""")
cursor.execute("""
    SELECT AddGeometryColumn('countries', 'outline',
                             4326, 'POLYGON', 2)
""")
cursor.execute("""
    SELECT CreateSpatialIndex('countries', 'outline')
""")

cursor.execute("DROP TABLE IF EXISTS shorelines")
cursor.execute("""
    CREATE TABLE shorelines (
        id    INTEGER PRIMARY KEY AUTOINCREMENT,
        level INTEGER)
""")
cursor.execute("""
    SELECT AddGeometryColumn('shorelines', 'outline',
                             4326, 'POLYGON', 2)
""")
cursor.execute("""
    SELECT CreateSpatialIndex('shorelines', 'outline')
""")

cursor.execute("DROP TABLE IF EXISTS places")
cursor.execute("""
    CREATE TABLE places (
        id   INTEGER PRIMARY KEY AUTOINCREMENT,
        name CHAR(255))
""")
cursor.execute("""
    SELECT AddGeometryColumn('places', 'position',
                             4326, 'POINT', 2)
""")
cursor.execute("""
    SELECT CreateSpatialIndex('places', 'position')
""")

db.commit()

