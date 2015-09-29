from PyQt4.QtGui import QColor

iface = qgis.utils.iface
mc = iface.mapCanvas()

layer = mc.currentLayer()
features = layer.getFeatures()

color_dict = dict()

for feature in features:
    cat = feature.attribute('designacao')
    rgba_value = feature.attribute('rgba')
    color_dict[cat] = rgba_value

renderer = layer.rendererV2()
categories = renderer.categories()

for category in categories:
    value = category.value()
    cat_id = renderer.categoryIndexForValue(value)
    print cat_id
    if value != u'':
        rgba = color_dict[value].split(',')
        rgba = [int(i) for i in rgba ]
        color = QColor(rgba[0],rgba[1],rgba[2],rgba[3])
        
        symbol = category.symbol()
        symbol.setColor(color)
        renderer.updateCategorySymbol(cat_id,symbol)

mc.refresh() 
qgis.utils.iface.legendInterface().refreshLayerSymbology(layer)
    
#rage = renderer.rootRule()
#
#for children in root_rule.children():
#    print children
#    if children.children():
#        for children2 in children.children():
#            print children2