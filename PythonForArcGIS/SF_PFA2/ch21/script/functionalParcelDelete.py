# functionalParcelDelete.py
parcelList = [1, 2, 5, 10, 15] 
parcelZoning = {1: 'residential', 2: 'commerial', 5: 'industrial', 10: 'residential', 15: 'agricultural'}
parcelPricing = {1: 145000.0, 2: 400000.0, 15: 90005000.0, 10: 900000.0, 5: 8000000.0}

# Determine which parcels to delete.
highCost = []
for k, v in parcelPricing.items():
    if v > 1000000:
        highCost.append(k)
# Delete the high cost parcels and tcorresponding attributes.
for i in highCost:
    parcelList.remove(i)
    del parcelPricing[i]
    del parcelZoning[i]
