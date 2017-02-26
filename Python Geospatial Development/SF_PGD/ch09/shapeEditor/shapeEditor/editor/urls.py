# URLConf for the shapeEditor.editor application.

from django.conf.urls import patterns, url

urlpatterns = patterns('shapeEditor.editor.views',
    url(r'^$',                             'list_shapefiles'),
    url(r'^import$',                       'import_shapefile'),
    url(r'^export/(?P<shapefile_id>\d+)$', 'export_shapefile'),
    url(r'^edit/(?P<shapefile_id>\d+)$',   'edit_shapefile'),
    url(r'^delete/(?P<shapefile_id>\d+)$', 'delete_shapefile'),
    url(r'^find_feature$',                 'find_feature'),
    url(r'^edit_feature/(?P<shapefile_id>\d+)/' +
        r'(?P<feature_id>\d+)$',           'edit_feature'),
    url(r'^edit_feature/(?P<shapefile_id>\d+)$',
        'edit_feature'), # feature_id = None -> add.
    url(r'^delete_feature/(?P<shapefile_id>\d+)/' +
        r'(?P<feature_id>\d+)$',           'delete_feature'),
)
