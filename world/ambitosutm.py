from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import Ambitosutm

ambitosutm_mapping = {
    'objectid': 'OBJECTID',
    'admapkey': 'AdMapKey',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON25D',
}

ambitosutm_shp = Path(__file__).resolve().parent / 'data' / 'ambitos_32719.shp'

def run(verbose=True):
    lm = LayerMapping(Ambitosutm, ambitosutm_shp, ambitosutm_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)