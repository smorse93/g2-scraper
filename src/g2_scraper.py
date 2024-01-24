
from typing import List,Optional, Union, Dict
from src.write_output import write_output
from src.get_products import FAILED_DUE_TO_CREDITS_EXHAUSTED, FAILED_DUE_TO_NO_KEY,FAILED_DUE_TO_NOT_SUBSCRIBED, FAILED_DUE_TO_UNKNOWN_ERROR, get_products


def clean_data(social_details):
    success, credits_exhausted, not_subscribed, unknown_error, no_key = [], [], [], [], []

    for detail in social_details:
        if detail.get("error") is None:
            success.append(detail)
        elif detail["error"] == FAILED_DUE_TO_CREDITS_EXHAUSTED:
            credits_exhausted.append(detail)
        elif detail["error"] == FAILED_DUE_TO_NOT_SUBSCRIBED:
            not_subscribed.append(detail)
        elif detail["error"] == FAILED_DUE_TO_UNKNOWN_ERROR:
            unknown_error.append(detail)
        elif detail["error"] == FAILED_DUE_TO_NO_KEY:
            no_key.append(detail)

            

    return success, credits_exhausted, not_subscribed, unknown_error, no_key

def print_data_errors(credits_exhausted, not_subscribed, unknown_error, no_key):
    
    if credits_exhausted:
        name = "products" if len(credits_exhausted) > 1 else "product"
        print(f"Could not get data for {len(credits_exhausted)} {name} due to credit exhaustion. Please consider upgrading your plan by visiting https://rapidapi.com/Chetan11dev/api/g2-data-api/pricing to continue scraping data.")

    if not_subscribed:
        name = "products" if len(not_subscribed) > 1 else "product"
        print(f"Could not get data for {len(not_subscribed)} {name} as you are not subscribed to G2 Data Api. Please subscribe to a free plan by visiting https://rapidapi.com/Chetan11dev/api/g2-data-api/pricing")

    if unknown_error:
        name = "products" if len(unknown_error) > 1 else "product"
        print(f"Could not get data for {len(unknown_error)} {name} due to Unknown Error.")

    if no_key:
        name = "products" if len(no_key) > 1 else "product"
        print(f"Could not get data for {len(no_key)} {name} as you are not subscribed to G2 Data Api. Please subscribe to a free plan by visiting https://rapidapi.com/Chetan11dev/api/g2-data-api/pricing")

      
def extract_product_from_link(x):
    x= x.strip()
    if 'g2.com/products/' in x:
        product = x.split('g2.com/products/')[1]
        if '/' in product:
            product = product.split('/')[0]
        return product
    return x


class G2:
    @staticmethod
    def get_products(products:  Union[str, List[str]], key: Optional[str] =None,  use_cache: bool = True) -> Dict:
        """
        Function to scrape data from ___.

        :param products: G2 Product(s) to scrape data for.
        :param key: Rapid API key for  Scraping.
        :param use_cache: Boolean indicating whether to use cached data.
        :return: List of dictionaries with the scraped data.
        """
        cache = use_cache
        if isinstance(products, str):
            products = [products]  

        products = [extract_product_from_link(product) for product in products]
        result = []
        for product in products:
            data = {"product": product}
            metadata = {"key": key}
            
            result_item = get_products(data, cache=cache, metadata=metadata)
            
            success, credits_exhausted, not_subscribed, unknown_error, no_key = clean_data([result_item])
            print_data_errors(credits_exhausted, not_subscribed, unknown_error, no_key)

            if success:
                result_item = result_item['data']
                result.append(result_item)
                write_output(product, result_item)

        if result:
            write_output('_all',result, lambda x:x)
        
        get_products.close()

        return result