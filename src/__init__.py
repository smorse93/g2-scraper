from .extract_product_links import ExtractProductLinks
from .extract_products import ExtractProducts

from .config import *
tasks_to_be_run = [
        ExtractProductLinks if SCRAPER == 'ExtractProductLinks' else ExtractProducts
]
