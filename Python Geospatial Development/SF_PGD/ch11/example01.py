from osgeo import gdal, gdalconst
import struct

dataset = gdal.Open("data/e10g")
band = dataset.GetRasterBand(1)

fmt = "<" + ("h" * band.XSize)

totHeight = 0

for y in range(band.YSize):
    scanline = band.ReadRaster(0, y, band.XSize, 1,
                               band.XSize, 1,
                               band.DataType)
    values = struct.unpack(fmt, scanline)

    for value in values:
        if value == -500:
            # Special height value for the sea -> ignore.
            continue
        totHeight = totHeight + value

average = float(totHeight) / (band.XSize * band.YSize)
print "Average height =", average

