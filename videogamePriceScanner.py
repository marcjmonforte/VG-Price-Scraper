# videogamePriceScanner.py - Quickly check the prices for games on multiple sites.

import requests, bs4

input_game_name = raw_input("What game are you looking for?\t")
input_console_name = raw_input("And what console do you want that game for?\t")
game_name_list = input_game_name.split(" ")
search_game_name = "+".join(game_name_list)
console_name_list = input_console_name.split(" ")

for word in console_name_list:
	if str(word).lower() in ['switch']:
		search_page_URL = 'https://www.gamestop.com/browse/nintendo-switch?nav=16k-3-' + \
		search_game_name + ',28zu0,131e8'
		search_page_text = requests.get(search_page_URL)
		search_page_text.raise_for_status()
		search_page_soup = bs4.BeautifulSoup(search_page_text.text, "lxml")
		print "Fetching results from URL:'%s'..." % search_page_URL
		break

	elif str(word).lower() in ['playstation', 'ps3', 'ps4']:
		for word in console_name_list:
			if str(word).lower() in ['3', 'ps3']:
				search_page_URL = 'https://www.gamestop.com/browse/playstation-3?nav=16k-3-' + \
				search_game_name + ',28zu0,138d'
				search_page_text = requests.get(search_page_URL)
				search_page_text.raise_for_status()
				search_page_soup = bs4.BeautifulSoup(search_page_text.text, "lxml")
				print "Fetching results from URL:'%s'..." % search_page_URL
				break

			elif str(word).lower() in ['4', 'ps4', 'playstation']:
				search_page_URL = 'https://www.gamestop.com/browse/playstation-4?nav=16k-3-' + \
				search_game_name + ',28zu0,131dc'
				search_page_text = requests.get(search_page_URL)
				search_page_text.raise_for_status()
				search_page_soup = bs4.BeautifulSoup(search_page_text.text, "lxml")
				print "Fetching results from URL:'%s'..." % search_page_URL
				break

	elif str(word).lower() in ['ds', '3ds', '2ds', 'gameboy', 'gb', 'gba']:
		search_page_URL = 'https://www.gamestop.com/browse/nintendo-3ds?nav=16k-3-' + \
		search_game_name + ',28zu0,131a2'
		search_page_text = requests.get(search_page_URL)
		search_page_text.raise_for_status()
		search_page_soup = bs4.BeautifulSoup(search_page_text.text, "lxml")
		print "Fetching results from URL:'%s'..." % search_page_URL
		break

	elif str(word).lower() in ['pc', 'computer', 'macbook', 'windows', 'mac', 'osx']:
		search_page_URL = 'https://www.gamestop.com/browse/pc?nav=16k-3-' + \
		search_game_name + ',28zu0,138c'
		search_page_text = requests.get(search_page_URL)
		search_page_text.raise_for_status()
		search_page_soup = bs4.BeautifulSoup(search_page_text.text, "lxml")
		print "Fetching results from URL:'%s'..." % search_page_URL
		break
	
	elif str(word).lower() in ['xbox', 'xb', 'xb1', 'xbox 360', 'xbox360', '360', 'xbone']:
		for word in console_name_list:
			if str(word).lower() in ['xb1', 'xbox one', 'xboxone', 'xbox1', 'xbox 1', 'xbox']:
				search_page_URL = 'https://www.gamestop.com/browse/xbox-one?nav=16k-3-' + \
				search_game_name + ',28zu0,131e0'
				search_page_text = requests.get(search_page_URL)
				search_page_text.raise_for_status()
				search_page_soup = bs4.BeautifulSoup(search_page_text.text, "lxml")
				print "Fetching results from URL:'%s'..." % search_page_URL
				break

			elif str(word).lower() in ['360', 'xbox 360', 'xbox360', 'xb360']:
				search_page_URL = 'https://www.gamestop.com/browse/xbox-360?nav=16k-3-' + \
				search_game_name + ',28zu0,1385'
				search_page_text = requests.get(search_page_URL)
				search_page_text.raise_for_status()
				search_page_soup = bs4.BeautifulSoup(search_page_text.text, "lxml")
				print "Fetching results from URL:'%s'..." % search_page_URL
				break

search_result = search_page_soup.find_all('a', 'ats-product-title-lnk')
search_result_list = []
for item in search_result:
	if item.get('href') not in search_result_list:
		if "/games/" in item.get('href'):
			search_result_list.append(item.get('href'))

if search_result_list == []:
	print "No results found."
else:
	for item in search_result_list:
		print "\nFetching results from URL:'%s'..." % item
		product_page_URL = "https://www.gamestop.com" + item
		product_page_text = requests.get(product_page_URL)
		product_page_text.raise_for_status()
		product_page_soup = bs4.BeautifulSoup(product_page_text.text, "lxml")

		product_page_name = product_page_soup.find('h1', 'grid_17 ats-prod-title')
		product_page_name = product_page_name.text
		product_page_name_list = product_page_name.split()
		new_product_page_name = " ".join(product_page_name_list)
		print new_product_page_name

		product_page_conditions = product_page_soup.find_all('strong', 'ats-prodBuy-condition')
		new_product_page_conditions = []
		for item in product_page_conditions:
			new_product_page_conditions.append(item.text.strip())

		product_page_prices = product_page_soup.find_all('h3', 'ats-prodBuy-price')
		new_product_page_prices = []
		for item in product_page_prices:
			new_product_page_prices.append(item.text)


		product_page_dict = dict(zip(new_product_page_conditions, new_product_page_prices))
		for k, v in product_page_dict.iteritems():
			print " * " +  k.title() + " : " + v.strip()
		

