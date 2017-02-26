import os
import os.path
import shutil
import tempfile
import zipfile

from osgeo import osr
from osgeo import ogr

from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper

from shapeEditor.shared import utils

#############################################################################

def export_data(shapefile):

    # Create a temporary directory to hold our shapefile.

    dst_dir = tempfile.mkdtemp()
    dst_file = str(os.path.join(dst_dir, shapefile.filename))

    # Create the shapefile and its associated spatial reference.

    dst_spatial_ref = osr.SpatialReference()
    dst_spatial_ref.ImportFromWkt(shapefile.srs_wkt)

    driver = ogr.GetDriverByName("ESRI Shapefile")
    datasource = driver.CreateDataSource(dst_file)
    layer = datasource.CreateLayer(str(shapefile.filename),
                                   dst_spatial_ref)

    # Define the various fields which will hold the shapefile's attributes.

    for attr in shapefile.attribute_set.all():
        field = ogr.FieldDefn(str(attr.name), attr.type)
        field.SetWidth(attr.width)
        field.SetPrecision(attr.precision)
        layer.CreateField(field)

    # Setup a coordinate transformation to convert from our internal spatial
    # reference system to the shapefile's original SRS.

    src_spatial_ref = osr.SpatialReference()
    src_spatial_ref.ImportFromEPSG(4326)

    coord_transform = osr.CoordinateTransformation(src_spatial_ref,
                                                   dst_spatial_ref)

    # See which field in the Feature object holds the feature's geometry.

    geom_field = utils.calc_geometry_field(shapefile.geom_type)

    # Start exporting the shapefile's contents.

    for feature in shapefile.feature_set.all():
        geometry = getattr(feature, geom_field)

        # If necessary, unwrap the geometry again.

        geometry = utils.unwrap_geos_geometry(geometry)

        # Convert the geometry into an OGR geometry object, and transform it
        # into the shapefile's original spatial reference system.

        dst_geometry = ogr.CreateGeometryFromWkt(geometry.wkt)
        dst_geometry.Transform(coord_transform)

        dst_feature = ogr.Feature(layer.GetLayerDefn())
        dst_feature.SetGeometry(dst_geometry)

        # Save the feature's attributes into the shapefile.

        for attr_value in feature.attributevalue_set.all():
            utils.set_ogr_feature_attribute(attr_value.attribute,
                                            attr_value.value,
                                            dst_feature,
                                            shapefile.encoding)

        # Finally, save the feature into the shapefile.

        layer.CreateFeature(dst_feature)
        dst_feature.Destroy()

    # Close the shapefile.

    datasource.Destroy()

    # Compress the shapefile into a ZIP archive.

    temp = tempfile.TemporaryFile()
    zip = zipfile.ZipFile(temp, "w", zipfile.ZIP_DEFLATED)

    shapefile_base = os.path.splitext(dst_file)[0]
    shapefile_name = os.path.splitext(shapefile.filename)[0]

    for fName in os.listdir(dst_dir):
        zip.write(os.path.join(dst_dir, fName), fName)

    zip.close()

    # Delete the shapefile directory.

    shutil.rmtree(dst_dir)

    # Finally, wrap the compressed ZIP archive in a FileWrapper so it can be
    # sent back to the user's web browser.

    f = FileWrapper(temp)
    response = HttpResponse(f, content_type="application/zip")
    response['Content-Disposition'] = \
        "attachment; filename=" + shapefile_name + ".zip"
    response['Content-Length'] = temp.tell()
    temp.seek(0)
    return response

