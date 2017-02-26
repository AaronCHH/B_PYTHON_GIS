from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.shortcuts import render

from shapeEditor.shared.models import Shapefile
from shapeEditor.editor.forms import ImportShapefileForm
from shapeEditor.shapefileIO import importer
from shapeEditor.shapefileIO import exporter

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

