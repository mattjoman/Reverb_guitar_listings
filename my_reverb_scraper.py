import numpy as np
import pandas as pd
from requests_html import HTMLSession

current_price_list = []
listing_title_list = []
condition_list = []
original_price_list = []

print('This will take a while...')

# Pages to scrape
pages = 500

for page in np.arange(1, pages+1):
	
	try:
		pagination = '&page=' + str(page)

		url = 'https://reverb.com/marketplace?product_type=electric-guitars&category=solid-body&condition=used' + pagination

		s = HTMLSession()
		r = s.get(url)

		r.html.render(sleep=8)

		products = r.html.xpath('/html/body/main/section/div[2]/div/div/div[2]/div/div[2]/ul', first=True)

		for guitar in products.absolute_links:

			req = s.get(guitar)

			try:
				listing_title = req.html.find('div.item2-title__inner', first=True).find('h1')[0].text
			except:
				listing_title = 'None'
			try:
				condition = req.html.find('div.item2-title__inner', first=True).find('div.condition-indicator__label')[0].text
			except:
				condition = 'None'
			try:
				current_price = req.html.find('div.price-with-shipping__price', first=True).find('span.price-display')[0].text
			except:
				current_price = 'None'
			try:
				original_price = req.html.find('div.price-with-shipping__price', first=True).find('div.price-with-shipping__price__original')[0].text
			except:
				original_price = current_price

			current_price_list.append(current_price)
			original_price_list.append(original_price)
			listing_title_list.append(listing_title)
			condition_list.append(condition)

		print('Page ', p, ' scraped!')

		r.close()
		s.close()
	except:
		print('Trouble encountered scraping page ' + str(page))


# SAVE DATA AS A .csv FILE
data = {
	'Current price': current_price_list,
	'Origninal price': original_price_list,
	'Listing title': listing_title_list,
	'Condition': condition_list,
}
data = pd.DataFrame(data)
data.to_csv('big_dataset.csv', index=False)
