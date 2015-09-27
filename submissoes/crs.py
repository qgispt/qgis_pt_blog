from qgis.utils import iface
from qgis.core import *
from qgis.gui import *

@qgsfunction(args=0, group='CRS')
def crslabel(value1,feature, parent):
    """
    Returns the project CRS 
    
    <h4>Syntax</h4>
    <p>crslabel(<i>value</i>)</p>
    <h4>Arguments</h4>
    <p><i>none</i> &rarr; 0</p>
    <h4>Example</h4>
    <p><!-- Show example of function.-->
    crslabel &rarr; EPSG:4326 - WGS84</p>
    <h4>Note:</h4>
    <p>This function only produces the EPSG code and the description.
    </p>
    """
    crs=iface.mapCanvas().mapSettings().destinationCrs()
    return crs.authid() +' - '+ crs.description() 

