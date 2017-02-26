import psycopg2

connection = psycopg2.connect("dbname=distal user=... password=...")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS countries")
cursor.execute("""
    CREATE TABLE countries (
        id   SERIAL,
        name VARCHAR(255),

        PRIMARY KEY (id))
""")
cursor.execute("""
    SELECT AddGeometryColumn('countries', 'outline',
                             4326, 'GEOMETRY', 2)
""")
cursor.execute("""
    CREATE INDEX countryIndex ON countries
        USING GIST(outline)
""")

cursor.execute("DROP TABLE IF EXISTS shorelines")
cursor.execute("""
    CREATE TABLE shorelines (
        id   SERIAL,
        level INTEGER,

        PRIMARY KEY (id))
""")
cursor.execute("""
    SELECT AddGeometryColumn('shorelines', 'outline',
                             4326, 'GEOMETRY', 2)
""")
cursor.execute("""
    CREATE INDEX shorelineIndex ON shorelines
        USING GIST(outline)
""")

cursor.execute("DROP TABLE IF EXISTS places")
cursor.execute("""
    CREATE TABLE places (
        id   SERIAL,
        name VARCHAR(255),

        PRIMARY KEY (id))
""")
cursor.execute("""
    SELECT AddGeometryColumn('places', 'position',
                             4326, 'POINT', 2)
""")
cursor.execute("""
    CREATE INDEX placeIndex ON places
        USING GIST(position)
""")
connection.commit()

