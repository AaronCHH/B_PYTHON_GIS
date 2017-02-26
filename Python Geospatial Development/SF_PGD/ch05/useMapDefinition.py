import mapnik

map = mapnik.Map(800, 400)
mapnik.load_map(map, "mapDefinition.xml")
map.zoom_to_box(mapnik.Box2d(-180, -90, +180, +90))
mapnik.render_to_file(map, "map.png")
