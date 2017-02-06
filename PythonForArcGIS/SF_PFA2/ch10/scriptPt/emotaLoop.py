# emotaLoop.py
# Purpose: Nest conditions inside a loop to print an emoticon for each file name.
myFiles = ['crops.csv', 'data1.shp', 'rast', 'xy1.txt']

for f in myFiles:
    if f.endswith('.shp'):
        print '   ;]   ' + f
    elif f.endswith('.txt'):
        print '   :(   ' + f
    else:
        print '   :o   ' + f
