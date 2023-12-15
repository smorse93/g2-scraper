from botasaurus import bt
from botasaurus.cache import DontCache

from .helpers import applyTransformer, convert_unicode_dict_to_ascii_dict
from .get_products_utils import *
from botasaurus import *
from time import sleep
from .utils import default_request_options
import requests



FAILED_DUE_TO_CREDITS_EXHAUSTED = "FAILED_DUE_TO_CREDITS_EXHAUSTED"
FAILED_DUE_TO_NOT_SUBSCRIBED = "FAILED_DUE_TO_NOT_SUBSCRIBED"
FAILED_DUE_TO_NO_KEY = "FAILED_DUE_TO_NO_KEY"
FAILED_DUE_TO_UNKNOWN_ERROR = "FAILED_DUE_TO_UNKNOWN_ERROR"

def update_credits():
    credits_used  = bt.LocalStorage.get_item("credits_used", 0)
    bt.LocalStorage.set_item("credits_used", credits_used + 1)

def do_request(data, retry_count=3):
    
    params = data["params"]
    key = data["key"]

    if retry_count == 0:
        print(f"Failed to get data, after 3 retries")
        return DontCache(None)

    url = "https://g2-data-api.p.rapidapi.com/g2-products/"

    querystring = params
    headers = {
        "X-RapidAPI-Key": key,
    	"X-RapidAPI-Host": "g2-data-api.p.rapidapi.com"
    }

    
    response = requests.get(url, headers=headers, params=querystring)
    response_data = response.json()
    if response.status_code == 200 or response.status_code == 404:
        
        message = response_data.get("message", "")
        if "API doesn't exists" in message:
            return DontCache({
                        "data":  None,
                        "error":FAILED_DUE_TO_UNKNOWN_ERROR
                    })

        update_credits()
        
        return {
            "data": convert_unicode_dict_to_ascii_dict(response_data),
            "error": None
        }
    else:
        message = response_data.get("message", "")
        if "exceeded the MONTHLY quota" in message:
            return  DontCache({
                        "data":  None,
                        "error":FAILED_DUE_TO_CREDITS_EXHAUSTED
                    })
        elif "exceeded the rate limit per second for your plan" in message or "many requests" in message:
            sleep(2)
            return do_request(data, retry_count - 1)
        elif "You are not subscribed to this API." in message:
            
            return DontCache({
                        "data": None,
                        "error": FAILED_DUE_TO_NOT_SUBSCRIBED
                    })

        print(f"Error: {response.status_code}", response_data)
        return  DontCache({
                        "data":  None,
                        "error":FAILED_DUE_TO_UNKNOWN_ERROR, 
                    })


@request(**default_request_options,)
def get_products(_, data, metadata):
    if not metadata.get('key'):
         return  DontCache({
                        "data":  None,
                        "error":FAILED_DUE_TO_NO_KEY
                    })
    
    data = {
        **metadata,
        "params": data,
    }

    return do_request(data)
