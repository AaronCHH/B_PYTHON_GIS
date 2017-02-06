import parcelclass
myparcel = parcelclass.parcel("SFR", 200000)
print "Land use:", myparcel.landuse
mytax = myparcel.assessment()
print mytax