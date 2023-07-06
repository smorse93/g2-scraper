import pydash
from selenium.webdriver.common.by import By
from bose import *
from urllib.parse import urlparse, parse_qs

class ExtractProductLinks(BaseTask):
    
    GET_FIRST_PAGE = True
    product_url = "https://www.g2.com/categories/sales-intelligence"
    
    browser_config = BrowserConfig(use_undetected_driver=True)

    def run(self, driver: BoseDriver, data):
        links = []

        def put_links():
            
            if driver.is_bot_detected():
              driver.prompt("Bot has been detected. Solve it to continue.")
            else: 
                print("Not Detected")

            els = driver.get_elements_or_none_by_selector('[data-ordered-events-scope="products"][itemtype="http://schema.org/ListItem"]', Wait.VERY_LONG)

            def get_innerhtml(el):
                    return el.get_attribute("innerHTML")
                            
            def domap(el):
                href = el.find_element(By.CSS_SELECTOR, 'a.d-ib.c-midnight-100.js-log-click').get_attribute("href")
                productName = el.find_element(By.CSS_SELECTOR, 'a.d-ib.c-midnight-100.js-log-click > div').get_attribute("innerHTML")
                
                result = {
                    'Product Name':productName,
                    'g2Link':href,
                }


                usr = el.find_elements(By.CSS_SELECTOR, '.grid-x .cell.medium-4:nth-child(1) div .mb-0 + ul > li')
                inds = el.find_elements(By.CSS_SELECTOR, '.grid-x .cell.medium-4:nth-child(2) div .mb-0 + ul > li')
                mks = el.find_elements(By.CSS_SELECTOR, '.grid-x .cell.medium-4:nth-child(3) div .mb-0 + ul > li')
                
                result['Users'] = ', '.join(pydash.uniq(list(map(get_innerhtml, usr))))
                result['Industries'] = ', '.join(pydash.uniq(list(map(get_innerhtml, inds))))
                result['Market Segment'] = ', '.join(pydash.uniq(list(map(get_innerhtml, mks))))

                return  result

            result = list(map(domap, els))
            print(f'Got {len(result)} new links')

            links.extend(result)

            Output.write_json(links, 'pending.json')
            
            return result

        def get_page_count():
            el = driver.get_element_or_none_by_selector('#product-list  ul  li:last-child > a.pagination__named-link.js-log-click', Wait.SHORT)
            url = el.get_attribute("href")
            
            url_parts = urlparse(url)
            query_params = parse_qs(url_parts.query)

            # Extract the 'page' parameter from the query parameters
            page_number = query_params.get('page', [])[0]

            return int(page_number)
        
        first= f"{self.product_url}#product-list"
        driver.organic_get(first)

        if driver.is_bot_detected():
            driver.prompt("Bot has been detected. Solve it to continue.")

        page_count = get_page_count()
        for next_page in range(2, page_count + 1):
            put_links()
            driver.short_random_sleep()
            driver.get_by_current_page_referrer(f"{self.product_url}?order=g2_score&page={next_page}#product-list" )
        put_links()