# URLConf for the shapeEditor.editor application.

from django.conf.urls import patterns, url

urlpatterns = patterns('shapeEditor.editor.views',
    url(r'^$',                             'list_shapefiles'),
    url(r'^import$',                       'import_shapefile'),
    url(r'^export/(?P<shapefile_id>\d+)$', 'export_shapefile'),
)
