from bs4 import BeautifulSoup
from bose import BaseTask
from bose import BaseTask, Wait, Output, BrowserConfig
from bose.utils import merge_dicts_in_one_dict

def write(result):
    Output.write_finished(result)
    Output.write_csv(result, "finished.csv")

class Task(BaseTask):
    browser_config = BrowserConfig(use_undetected_driver=True, is_eager=True)
    def run(self, driver):

        def htmltosoup(page):
            return BeautifulSoup(page, 'html.parser')


        def get_company_data(company_url):

            # driver.get_by_current_page_referrer(company_url)
            # driver.get(company_url)
            driver.organic_get(company_url)
            # short_random_sleep()
            if driver.is_bot_detected():
              driver.wait_for_enter("Bot has been detected. Solve it to continue.")
            else: 
                print("Not Detected")

            driver.get_element_or_none_by_selector('h1.l2.pb-half.inline-block', Wait.VERY_LONG * 4)
            html = htmltosoup(driver.page_source)

            website = html.select_one('a[itemprop$="url"]')['href']

            try:
                description = html.select_one('div[itemprop$="description"]').text
            except AttributeError:
                description = "No description available"

            try: 
                ratings = html.select_one('div[class$="text-center ai-c star-wrapper__desc__rating"]').text
                number_of_reviews = html.select_one('li[class$="list--piped__li"]').text 
            except AttributeError:
                ratings = "No ratings available"
                number_of_reviews = 0
                
            
            details_list = html.find_all("div", class_ = 'ml-1')

            
            details_titles = ['LinkedIn Page' if 'LinkedIn' in p.next.text and 'Page' in p.next.text else  p.next.text for p in details_list]

            details_values = []
            
            for p in details_list:
                
                p.find("div", class_ = 'fw-semibold').decompose()
                link = p.find("a", class_ = 'link')
            
                if link is not None:
                    p = link['href']
                else:
                    data = str(p)
                    
                    if 'Twitter' in data:
                        p =  data.replace('<div class="ml-1">', '').replace('</div>', '').replace('<br/>', ' ').strip()
                    else:
                        p = p.text
            
                details_values.append(p)

            details = dict(zip(details_titles, details_values))

            _details = {'Description': description,
                            'Website': website,
                            'Ratings': ratings.strip(),
                            'Number Of Reviews': number_of_reviews}

            _details.update(details)
            
            return _details
        seeds = Output.read_pending()

        result = []

        for item in seeds:
            link = item['g2Link']
            data = get_company_data(link)
            result.append(merge_dicts_in_one_dict({"Ownership": None,'Total Revenue (USD mm)': None }, item, data))
            print(f'Done {link}')
            write(result)
        write(result)
        Output.write_csv(result, "finished.csv")
if __name__ == '__main__':
    Task().begin_task()