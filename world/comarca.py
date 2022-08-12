from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import Comarca



comarca_mapping = {
    'admapkey': 'AdMapKey',
    'geom': 'MULTIPOLYGON25D',
}
comarca_shp = Path(__file__).resolve().parent / 'data' / 'AMBITOS_GEORREF_CUS_SA.shp'

def run(verbose=True):
    lm = LayerMapping(Comarca, comarca_shp, comarca_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)

