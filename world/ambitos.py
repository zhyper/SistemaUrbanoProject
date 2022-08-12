from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import Ambitos

ambitos_mapping = {
    'objectid': 'OBJECTID',
    'admapkey': 'AdMapKey',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON25D',
}

ambitos_shp = Path(__file__).resolve().parent / 'data' / 'ambitos_wgs84_geografica.shp'

def run(verbose=True):
    lm = LayerMapping(Ambitos, ambitos_shp, ambitos_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)