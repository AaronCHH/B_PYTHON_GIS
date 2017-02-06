import arcpy
def listfieldnames(table):
  fields = arcpy.ListFields(table)
  namelist = []
  for field in fields:
    namelist.append(field.name)
  return namelist

if __name__ == "__main__":
  fieldnames = listfieldnames("DATA/streets.shp")
  print fieldnames
  raw_input()