from cloudscraper import create_scraper
from bs4 import BeautifulSoup
from latest_user_agents import get_random_user_agent
import logging
from datetime import date

today_date = date.today()
date_save = today_date.strftime("%Y-%m-%d")
logging.basicConfig(filename='scraper.log', level=logging.DEBUG, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

class FishLine:
    def __init__(self):
        self.session = create_scraper()
        self.headers = {'User-Agent': get_random_user_agent()}

    def extract(self, url, date):
        store = 'Finish Line'
        r = self.session.get(url, headers=self.headers)
        soup = BeautifulSoup(r.text, 'lxml')
        title = soup.select_one('.titleDesk').text.strip()
        price = soup.select_one('.fullPrice').text.strip()
        reviews = soup.select_one('.ldjsonData')['data-averageratingdecimal']
        rating = soup.select_one('.ldjsonData')['data-reviewcount']
        product_item = (
            date,
            store,
            title, 
            price,
            reviews,
            rating
        )
        logging.info(product_item)
        return product_item
    
links = [
    'https://www.finishline.com/store/product/big-kids-jordan-tatum-1-basketball-shoes/prod2859647?styleId=DX5359&colorId=600',
    'https://www.finishline.com/store/product/little-kids-jordan-tatum-1-basketball-shoes/prod2859680?styleId=DX5357&colorId=600',
    'https://www.finishline.com/store/product/jordan-tatum-1-basketball-shoes/prod2859661?styleId=DV6208&colorId=600',
    'https://www.finishline.com/store/product/kids-toddler-jordan-tatum-1-basketball-shoes/prod2859615?styleId=DX5358&colorId=600',
    'https://www.finishline.com/store/product/air-jordan-retro-1-high-og-casual-shoes/prod2854212?styleId=DZ5485&colorId=052'
]

for link in links:
    prod = FishLine().extract(link, date_save)
    print(prod)