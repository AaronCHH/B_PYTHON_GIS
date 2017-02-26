import traceback

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.contrib.gis.geos import Point

from shapeEditor.shared.models import Shapefile
from shapeEditor.shared.models import Feature
from shapeEditor.shared        import utils
from shapeEditor.editor.forms  import ImportShapefileForm
from shapeEditor.shapefileIO   import importer
from shapeEditor.shapefileIO   import exporter

#############################################################################

def list_shapefiles(request):
    shapefiles = Shapefile.objects.all().order_by("filename")
    return render(request, "list_shapefiles.html",
                  {'shapefiles' : shapefiles})

#############################################################################

def import_shapefile(request):
    if request.method == "GET":
        form = ImportShapefileForm()
        return render(request, "import_shapefile.html",
                      {'form'    : form,
                       'err_msg' : None})
    elif request.method == "POST":
        form = ImportShapefileForm(request.POST,
                                   request.FILES)
        if form.is_valid():
            shapefile = request.FILES['import_file']
            encoding  = request.POST['character_encoding']

            err_msg = importer.import_data(shapefile, encoding)

            if err_msg == None:
                return HttpResponseRedirect("/editor")
        else:
            err_msg = None

        return render(request, "import_shapefile.html",
                      {'form'    : form,
                       'err_msg' : err_msg})

#############################################################################

def export_shapefile(request, shapefile_id):
    try:
        shapefile = Shapefile.objects.get(id=shapefile_id)
    except Shapefile.DoesNotExist:
        return HttpResponseNotFound()

    return exporter.export_data(shapefile)

#############################################################################

def edit_shapefile(request, shapefile_id):
    try:
        shapefile = Shapefile.objects.get(id=shapefile_id)
    except Shapefile.DoesNotExist:
        return HttpResponseNotFound()

    tms_url          = "http://" + request.get_host() + "/tms/"

    find_feature_url = "http://" + request.get_host() \
                     + "/editor/find_feature"

    add_feature_url  = "http://" + request.get_host() \
                     + "/editor/edit_feature/" \
                     + str(shapefile_id)

    return render(request, "select_feature.html",
                  {'shapefile'        : shapefile,
                   'find_feature_url' : find_feature_url,
                   'add_feature_url'  : add_feature_url,
                   'tms_url'          : tms_url})

#############################################################################

def delete_shapefile(request, shapefile_id):
    try:
        shapefile = Shapefile.objects.get(id=shapefile_id)
    except Shapefile.DoesNotExist:
        return HttpResponseNotFound()

    if request.method == "GET":
        return render(request, "delete_shapefile.html",
                      {'shapefile' : shapefile})
    elif request.method == "POST":
        if request.POST['confirm'] == "1":
            shapefile.delete()
        return HttpResponseRedirect("/editor")

#############################################################################

def find_feature(request):
    try:
        shapefile_id = int(request.GET['shapefile_id'])
        latitude     = float(request.GET['latitude'])
        longitude    = float(request.GET['longitude'])

        shapefile = Shapefile.objects.get(id=shapefile_id)
        pt = Point(longitude, latitude)
        radius = utils.calc_search_radius(latitude, longitude, 100)

        if shapefile.geom_type == "Point":
            query = Feature.objects.filter(
                        geom_point__dwithin=(pt, radius))
        elif shapefile.geom_type in ["LineString", "MultiLineString"]:
            query = Feature.objects.filter(
                        geom_multilinestring__dwithin=(pt, radius))
        elif shapefile.geom_type in ["Polygon", "MultiPolygon"]:
            query = Feature.objects.filter(
                        geom_multipolygon__dwithin=(pt, radius))
        elif shapefile.geom_type == "MultiPoint":
            query = Feature.objects.filter(
                        geom_multipoint__dwithin=(pt, radius))
        elif shapefile.geom_type == "GeometryCollection":
            query = feature.objects.filter(
                        geom_geometrycollection__dwithin=(pt, radius))
        else:
            print "Unsupported geometry: " + shapefile.geom_type
            return HttpResponse("")

        if query.count() != 1:
            return HttpResponse("")

        feature = query[0]
        return HttpResponse("/editor/edit_feature/" +
                            str(shapefile_id)+"/"+str(feature.id))
    except:
        traceback.print_exc()
        return HttpResponse("")

#############################################################################

def edit_feature(request, shapefile_id, feature_id=None):
    if request.method == "POST" and "delete" in request.POST:
        return HttpResponseRedirect("/editor/delete_feature/" +
                                    shapefile_id+"/"+feature_id)
    try:
        shapefile = Shapefile.objects.get(id=shapefile_id)
    except Shapefile.DoesNotExist:
        return HttpResponseNotFound()

    if feature_id == None:
        feature = Feature(shapefile=shapefile)
    else:
        try:
            feature = Feature.objects.get(id=feature_id)
        except Feature.DoesNotExist:
            return HttpResponseNotFound()

    attributes = []
    for attr_value in feature.attributevalue_set.all():
        attributes.append([attr_value.attribute.name,
                           attr_value.value])
    attributes.sort()

    geometry_field = utils.calc_geometry_field(shapefile.geom_type)
    form_class     = utils.get_map_form(shapefile)

    if request.method == "GET":
        wkt  = getattr(feature, geometry_field)
        form = form_class({'geometry' : wkt})

        return render(request, "edit_feature.html",
                      {'shapefile'  : shapefile,
                       'form'       : form,
                       'attributes' : attributes})
    elif request.method == "POST":
        form = form_class(request.POST)
        try:
            if form.is_valid():
                wkt = form.cleaned_data['geometry']
                setattr(feature, geometry_field, wkt)
                feature.save()
                return HttpResponseRedirect("/editor/edit/" +
                                            shapefile_id)
        except ValueError:
            pass

        return render(request, "edit_feature.html",
                      {'shapefile'  : shapefile,
                       'form'       : form,
                       'attributes' : attributes})

#############################################################################

def delete_feature(request, shapefile_id, feature_id):
    try:
        feature = Feature.objects.get(id=feature_id)
    except Feature.DoesNotExist:
        return HttpResponseNotFound()

    if request.method == "POST":
        if request.POST['confirm'] == "1":
            feature.delete()

        return HttpResponseRedirect("/editor/edit/" +
                                    shapefile_id)

    return render(request, "delete_feature.html")

