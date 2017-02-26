# mapGenerator.py

import os, os.path, sys, tempfile
import mapnik

def generateMap(datasource, minX, minY, maxX, maxY,
                mapWidth, mapHeight,
                hiliteExpr=None, background="#8080a0",
                hiliteLine="#000000", hiliteFill="#408000",
                normalLine="#404040", normalFill="#a0a0a0",
                points=None):
    srcType = datasource['type']
    del datasource['type']

    if srcType == "OGR":
        source = mapnik.Ogr(**datasource)
    elif srcType == "PostGIS":
        source = mapnik.PostGIS(**datasource)
    elif srcType == "SQLite":
        source = mapnik.SQLite(**datasource)

    layer = mapnik.Layer("Layer")
    layer.datasource = source

    map = mapnik.Map(mapWidth, mapHeight,
                     '+proj=longlat +datum=WGS84')
    map.background = mapnik.Color(background)

    style = mapnik.Style()

    rule = mapnik.Rule()
    if hiliteExpr != None:
        rule.filter = mapnik.Filter(hiliteExpr)

    rule.symbols.append(mapnik.PolygonSymbolizer(
        mapnik.Color(hiliteFill)))
    rule.symbols.append(mapnik.LineSymbolizer(
        mapnik.Stroke(mapnik.Color(hiliteLine), 0.1)))

    style.rules.append(rule)

    rule = mapnik.Rule()
    rule.set_else(True)

    rule.symbols.append(mapnik.PolygonSymbolizer(
        mapnik.Color(normalFill)))
    rule.symbols.append(mapnik.LineSymbolizer(
        mapnik.Stroke(mapnik.Color(normalLine), 0.1)))

    style.rules.append(rule)
    
    map.append_style("Map Style", style)
    layer.styles.append("Map Style")
    map.layers.append(layer)

    if points != None:
        memoryDatasource = mapnik.MemoryDatasource()
        context = mapnik.Context()
        context.push("name")
        next_id = 1
        for long,lat,name in points:
            wkt = "POINT (%0.8f %0.8f)" % (long,lat)
            feature = mapnik.Feature(context, next_id)
            feature['name'] = name
            feature.add_geometries_from_wkt(wkt)
            next_id = next_id + 1
            memoryDatasource.add_feature(feature)

        layer = mapnik.Layer("Points")
        layer.datasource = memoryDatasource

        style = mapnik.Style()
        rule = mapnik.Rule()

        pointImgFile = os.path.join(os.path.dirname(__file__),
                                    "point.png")

        shield = mapnik.ShieldSymbolizer(
                   mapnik.Expression('[name]'),
                   "DejaVu Sans Bold", 10,
                   mapnik.Color("#000000"),
                   mapnik.PathExpression(pointImgFile))
        shield.displacement = (0, 7)
        shield.unlock_image = True
        rule.symbols.append(shield)

        style.rules.append(rule)

        map.append_style("Point Style", style)
        layer.styles.append("Point Style")

        map.layers.append(layer)

    map.zoom_to_box(mapnik.Envelope(minX, minY, maxX, maxY))

    scriptDir = os.path.dirname(__file__)
    cacheDir = os.path.join(scriptDir, "..", "mapCache")
    if not os.path.exists(cacheDir):
        os.mkdir(cacheDir)
    fd,filename = tempfile.mkstemp(".png", dir=cacheDir)
    os.close(fd)

    mapnik.render_to_file(map, filename, "png")

    return "../mapCache/" + os.path.basename(filename)

