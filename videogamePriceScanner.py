# videogamePriceScanner.py - Quickly check the prices for games on multiple sites.

import requests, bs4, search_terms

def get_game_name():
	""" Gets and reformats user's desired game to use for search.
		INPUT: The name of the desired game, as a string.
		OUTPUT: Reformated game name for use in search URL. """

	input_game_name = raw_input("What game are you looking for?\t")
	game_name_list = input_game_name.split(" ")
	search_game_name = "+".join(game_name_list)
	
	if search_game_name:
		return search_game_name
	
	else:
		print "FUNCTION get_game_name(): Failure."
		return None

def get_console_list():
	""" Gets and reformats user's desired console to use for search.
		INPUT: The name of the desired console, as a string.
	   	OUTPUT: The name of the desired console, as a list. """

	input_console_name = raw_input("And what console do you want that game for?\t")
	console_name_list = input_console_name.split(" ")

	if console_name_list:
		return console_name_list

	else:
		print "FUNCTION get_console_name(): Failure."
		return None

def get_search_page_results(search_game_name, console_name_list):
	""" Prints the results of a search from Gamestop.com, as if the user
		searched for their desired game name and filtered by their desired
		console name.
		INPUT: get_game_name() and get_console_list()
		OUTPUT: Terminal-printed relevnat results from the search. """

	def get_search_page_soup(search_page_URL):
		""" Gets the raw JSON from the results of a search from Gamestop.com, 
		as if the user searched for their desired game name and filtered by 
		their desired console name.
		INPUT: "search_page_URL", which is defined mid-way through 
				the function get_search_page_results().
		OUTPUT: Raw text for use with BeautifulSoup. 
		"""

		search_page_text = requests.get(search_page_URL)
		search_page_text.raise_for_status()
		search_page_soup = bs4.BeautifulSoup(search_page_text.text, "lxml")
		if search_game_name:
			return search_page_soup
		else:
			print "FUNCTION get_search_page_soup(): Failure."
			return None

	for word in console_name_list:
		if str(word).lower() in search_terms.computer_search:
			search_page_URL = 'https://www.gamestop.com/browse/pc?nav=16k-3-' + \
			search_game_name + ',28zu0,138c'
			search_page_soup = get_search_page_soup(search_page_URL)

		elif str(word).lower() in search_terms.microsoft_search:
			print "Still in development..."

		elif str(word).lower() in search_terms.microsoft_xbox360_search:
			search_page_URL = 'https://www.gamestop.com/browse/xbox-360?nav=16k-3-' + \
			search_game_name + ',28zu0,1385'
			search_page_soup = get_search_page_soup(search_page_URL)	

		elif str(word).lower() in search_terms.microsoft_xbox_search:
			print "Still in development..."

		elif str(word).lower() in search_terms.microsoft_xboxone_search:
			search_page_URL = 'https://www.gamestop.com/browse/xbox-one?nav=16k-3-' + \
			search_game_name + ',28zu0,131e0'
			search_page_soup = get_search_page_soup(search_page_URL)

		elif str(word).lower() in search_terms.nintendo_3DS_search:
			search_page_URL = 'https://www.gamestop.com/browse/nintendo-3ds?nav=16k-3-' + \
			search_game_name + ',28zu0,131a2'
			search_page_soup = get_search_page_soup(search_page_URL)

		elif str(word).lower() in search_terms.nintendo_gameboy_search:
			print "Still in development..."

		elif str(word).lower() in search_terms.nintendo_gamecube_search:
			print "Still in development..."

		elif str(word).lower() in search_terms.nintendo_gba_search:
			print "Still in development..."

		elif str(word).lower() in search_terms.nintendo_search:
			print "Still in development..."

		elif str(word).lower() in search_terms.nintendo_switch_search:
			search_page_URL = 'https://www.gamestop.com/browse/nintendo-switch?nav=16k-3-' + \
			search_game_name + ',28zu0,131e8'
			search_page_soup = get_search_page_soup(search_page_URL)	

		elif str(word).lower() in search_terms.nintendo_wii_search:
			print "Still in development..."

		elif str(word).lower() in search_terms.nintendo_wiiU_search:
			print "Still in development..."

		elif str(word).lower() in search_terms.sony_playstation2_search:
			print "Still in development..."

		elif str(word).lower() in search_terms.sony_playstation3_search:
			search_page_URL = 'https://www.gamestop.com/browse/playstation-3?nav=16k-3-' + \
			search_game_name + ',28zu0,138d'
			search_page_soup = get_search_page_soup(search_page_URL)

		elif str(word).lower() in search_terms.sony_playstation4_search:
			search_page_URL = 'https://www.gamestop.com/browse/playstation-4?nav=16k-3-' + \
			search_game_name + ',28zu0,131dc'
			search_page_soup = get_search_page_soup(search_page_URL)

		elif str(word).lower() in search_terms.sony_playstation_search:
			print "Still in development..."

		elif str(word).lower() in search_terms.sony_psp_search:
			print "Still in development..."

		elif str(word).lower() in search_terms.sony_search:
			print "Still in development..."

		elif str(word).lower() in search_terms.sony_vita_search:
			print "Still in development..."

		else:
			print "FUNCTION get_search_page_results(): Failure."
			return None

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

# Execute the script.
get_search_page_results(get_game_name(), get_console_list())
print "\nScript complete."
print "." * 3

