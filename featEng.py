# Getting the brand of guitar (improve on this)
def get_brand(_data):

	import numpy as np
	import pandas as pd
	from re import search

	y = []
	titles = _data.Listing_title.values

	for i in np.arange(len(_data.Listing_title)):
		
		x = titles[i]

		if search('Squier', x) or search('squier', x) or search('SQUIER', x):
			y.append('Squier')
		elif search('Fender', x) or search('fender', x) or search('FENDER', x):
			y.append('Fender')
		elif search('Epiphone', x) or search('epiphone', x) or search('EPIPHONE', x):
			y.append('Epiphone')
		elif search('Gibson', x) or search('gibson', x) or search('GIBSON', x):
			y.append('Gibson')
		elif search('Ibanez', x) or search('ibanez', x) or search('IBANEZ', x):
			y.append('Ibanez')
		elif search('Danelectro', x) or search('danelectro', x) or search('DANELECTRO', x):
			y.append('Danelectro')
		elif search('Schecter', x) or search('schecter', x) or search('SCHECTER', x):
			y.append('Schecter')
		elif search('Jackson', x) or search('jackson', x) or search('JACKSON', x):
			y.append('Jackson')
		elif search('ESP', x):
			y.append('ESP')
		elif search('Sterling', x) or search('sterling', x) or search('STERLING', x):
			y.append('Sterling')
		elif search('Ernie Ball', x) or search('ernie ball', x) or search('EARNIE BALL', x):
			y.append('Ernie Ball')
		elif search('Music Man', x) or search('music man', x) or search('MUSIC MAN', x):
			y.append('Music Man')
		elif search('Yamaha', x) or search('yamaha', x) or search('YAMAHA', x):
			y.append('Yamaha')
		elif search('Paul Reed Smith', x) or search('paul reed smith', x) or search('PAUL REED SMITH', x):
			y.append('Paul Reed Smith')
		elif search('PRS', x) or search('Prs', x) or search('prs', x):
			y.append('PRS')
		elif search('Charvel', x) or search('charvel', x) or search('CHARVEL', x):
			y.append('Charvel')
		elif search('Suhr', x) or search('suhr', x) or search('SUHR', x):
			y.append('Suhr')
		elif search('G&L', x) or search('g&l', x):
			y.append('G&L')
		elif search('Peavey', x) or search('peavey', x) or search('PEAVEY', x):
			y.append('Peavey')
		elif search('Gretsch', x) or search('gretsch', x) or search('GRETSCH', x):
			y.append('Gretsch')
		elif search('Washburn', x) or search('washburn', x) or search('WASHBURN', x):
			y.append('Washburn')
		elif search('Godin', x) or search('godin', x) or search('GODIN', x):
			y.append('Godin')
		elif search('Carvin', x) or search('carvin', x) or search('CARVIN', x):
			y.append('Carvin')
		elif search('Tokai', x) or search('tokai', x) or search('TOKAI', x):
			y.append('Tokai')
		elif search('Kramer', x) or search('kramer', x) or search('KRAMER', x):
			y.append('Kramer')
		elif search('Teisco', x) or search('teisco', x) or search('TEISCO', x):
			y.append('Teisco')
		elif search('Warmoth', x) or search('warmoth', x) or search('WARMOTH', x):
			y.append('Warmoth')
		elif search('Line 6', x) or search('line 6', x) or search('LINE 6', x):
			y.append('Line 6')
		elif search('Mayones', x) or search('mayones', x) or search('MAYONES', x):
			y.append('Mayones')
		elif search('Fernandes', x) or search('fernandes', x) or search('FERNANDES', x):
			y.append('Fernandes')
		elif search('EVH', x):
			y.append('EVH')
		elif search('Hagstrom', x) or search('hagstrom', x) or search('HAGSTROM', x):
			y.append('Hagstrom')
		elif search('Dean', x) or search('dean', x) or search('DEAN', x):
			y.append('Dean')
		elif search('Greco', x) or search('Greco', x) or search('GRECO', x):
			y.append('Greco')
		elif search('Tom Anderson', x) or search('tom anderson', x) or search('TOM ANDERSON', x):
			y.append('Tom Anderson')
		elif search('Chapman', x) or search('chapman', x) or search('CHAPMAN', x):
			y.append('Chapman')
		elif search('Knaggs', x) or search('knaggs', x) or search('KNAGGS', x):
			y.append('Knaggs')
		elif search('Rickenbacker', x) or search('rickenbacker', x) or search('RICKENBACKER', x):
			y.append('Rickenbacker')

		else:
			y.append('Other')

	_data['brand'] = y

	return _data







# Convert brands and models to numeric values for modelling
# Make sure the if/elif/else statements match the categories created
def get_brand_num(_data):

	import numpy as np
	import pandas as pd
	
	y = np.empty(len(_data.Listing_title))
	brand = _data.brand.values

	for i in np.arange(len(_data.Listing_title)):
		x = brand[i]

		if x == 'Fender':
			y[i] = 1
		elif x == 'Gibson':
			y[i] = 2
		elif x == 'Squier':
			y[i] = 3
		elif x == 'Epiphone':
			y[i] = 4
		elif x == 'Ibanez':
			y[i] = 5
		elif x == 'Danelectro':
			y[i] = 6
		elif x == 'Schecter':
			y[i] = 7
		elif x == 'Jackson':
			y[i] = 8
		elif x == 'ESP':
			y[i] = 9
		elif x == 'Ernie Ball':
			y[i] = 10
		elif x == 'Sterling':
			y[i] = 11
		elif x == 'Yamaha':
			y[i] = 12
		elif x == 'Paul Reed Smith':
			y[i] = 13
		elif x == 'PRS':
			y[i] = 14
		elif x == 'Charvel':
			y[i] = 15
		elif x == 'Suhr':
			y[i] = 16
		elif x == 'Music Man':
			y[i] = 17
		elif x == 'G&L':
			y[i] = 18
		elif x == 'Peavey':
			y[i] = 19
		elif x == 'Gretsch':
			y[i] = 20
		elif x == 'Washburn':
			y[i] = 21
		elif x == 'Godin':
			y[i] = 22
		elif x == 'Carvin':
			y[i] = 23
		elif x == 'Tokai':
			y[i] = 24
		elif x == 'Kramer':
			y[i] = 25
		elif x == 'Teisco':
			y[i] = 26
		elif x == 'Warmoth':
			y[i] = 27
		elif x == 'Line 6':
			y[i] = 28
		elif x == 'Mayones':
			y[i] = 29
		elif x == 'Fernandes':
			y[i] = 30
		elif x == 'EVH':
			y[i] = 31
		elif x == 'Hagstrom':
			y[i] = 32
		elif x == 'Dean':
			y[i] = 33
		elif x == 'Greco':
			y[i] = 34
		elif x == 'Tom Anderson':
			y[i] = 35
		elif x == 'Chapman':
			y[i] = 36
		elif x == 'Knaggs':
			y[i] = 37
		elif x == 'Rickenbacker':
			y[i] = 38
		####################
		else:
			y[i] = 0

	_data['brand_num'] = y
	return _data







# Get the model of guitar (strat, tele, les paul, sg, ...)
# include more models and alternative spellings
def getModel(_data):
	
	import numpy as np
	import pandas as pd
	from re import search

	y = []
	titles = _data.Listing_title.values

	for i in np.arange(len(_data.original_price.values)):
		x = titles[i]
		
		if search('Strat', x):
			y.append('Strat')
		elif search('Tele', x):
			y.append('Tele')
		elif search('Jaguar', x):
			y.append('Jaguar')
		elif search('Jazzmaster', x):
			y.append('Jazzmaster')
		elif search('Les Paul', x):
			y.append('Les Paul')
		elif search('SG', x):
			y.append('SG')
		elif search('Firebird', x):
			y.append('Firebird')
		elif search('Flying V', x):
			y.append('Flying V')
		elif search('Jem', x):
			y.append('Jem')

		else:	# Other brand
			y.append('Other')

	_data['model'] = y
	return _data





# Convert brands and models to numeric values for modelling
# Make sure the if/elif/else statements match the categories created
def get_model_num(_data):

	import numpy as np
	import pandas as pd
	
	models = _data.model.values
	y = np.empty(len(models))

	for i in np.arange(len(_data.original_price.values)):
		x = models[i]

		if x == 'Strat':
			y[i] = 1
		elif x == 'Tele':
			y[i] = 2
		elif x == 'Jaguar':
			y[i] = 3
		elif x == 'Jazzmaster':
			y[i] = 4
		elif x == 'Les Paul':
			y[i] = 5
		elif x == 'SG':
			y[i] = 6
		elif x == 'Firebird':
			y[i] = 7
		elif x == 'Flying V':
			y[i] = 8
		elif x == 'Jem':
			y[i] = 9

		else:
			y[i] = 0

	_data['model_num'] = y
	return _data









def getSpecialScore(_data):
	
	import numpy as np
	import pandas as pd
	from re import search

	special_score = np.empty(len(_data.current_price.values))

	rare = np.empty(len(_data.current_price.values))
	custom_shop = np.empty(len(_data.current_price.values))
	relic = np.empty(len(_data.current_price.values))
	vintage = np.empty(len(_data.current_price.values))
	signature = np.empty(len(_data.current_price.values))
	case_included = np.empty(len(_data.current_price.values))
	NOS = np.empty(len(_data.current_price.values))
	fifties_sixties = np.empty(len(_data.current_price.values))
	fancy_wood = np.empty(len(_data.current_price.values))
	signed = np.empty(len(_data.current_price.values))
	famous = np.empty(len(_data.current_price.values))


	for i in np.arange(len(_data.current_price.values)):
		
		ss = 0
		title = _data.Listing_title.values[i]

		if search('Rare', title):
			rare[i] = 1
			ss += 1
		else:
			rare[i] = 0

		if search('Custom Shop', title):
			custom_shop[i] = 1
			ss += 2
		else:
			custom_shop[i] = 0

		if search('Relic', title):
			relic[i] = 1
			ss += 1
		else:
			relic[i] = 0

		if search('Vintage', title):
			vintage[i] = 1
			ss += 1
		else:
			vintage[i] = 0

		if search('Signature', title):
			signature[i] = 1
			ss += 1
		else:
			signature[i] = 0

		if search('Case Included', title) or search('Original Case', title):
			case_included[i] = 1
			ss += 1
		else:
			case_included[i] = 0

		if search('NOS', title):
			NOS[i] = 1
			ss += 2
		else:
			NOS[i] = 0

		if search('50s', title) or search('60s', title):
			fifties_sixties[i] = 1
			ss += 1
		else:
			fifties_sixties[i] = 0

		if search('Flamed Maple', title) or search('AAA', title) or search('Wood Library', title):
			fancy_wood[i] = 1
			ss += 1
		else:
			fancy_wood[i] = 0

		if search('Signed', title):
			signed[i] = 1
			ss += 2
		else:
			signed[i] = 0

		if search('Guthrie Govan', title) or search('Jimmy Page', title):
			famous[i] = 1
			ss += 2
		else:
			famous[i] = 0

		special_score[i] = ss

	_data['rare'] = rare
	_data['custom_shop'] = custom_shop
	_data['relic'] = relic
	_data['vintage'] = vintage
	_data['signature'] = signature
	_data['case_included'] = case_included
	_data['NOS'] = NOS
	_data['fifties_sixties'] = fifties_sixties
	_data['fancy_wood'] = fancy_wood
	_data['signed'] = signed
	_data['famous'] = famous

	_data['special_score'] = special_score

	return _data





# convert the conditions to numerical values
def conv_conditions(_data):

	import numpy as np
	import pandas as pd
	
	conditions = _data.Condition.values
	y = np.empty(len(conditions))

	for i in np.arange(len(y)):
		x = conditions[i]

		if x == 'Mint':
			y[i] = 1
		elif x == 'Excellent':
			y[i] = 2
		elif x == 'Very Good':
			y[i] = 3
		elif x == 'Good':
			y[i] = 4
		elif x == 'Fair':
			y[i] = 5
		else:
			y[i] = 0

	_data['condition'] = y
	return _data







# Calculate the discount
def getDiscount(_data):

	import numpy as np
	import pandas as pd

	discount = _data.original_price.values - _data.current_price.values
	_data['discount'] = discount

	# was there a discount?
	cur_p = _data.current_price.values
	ori_p = _data.original_price.values
	is_discounted = np.empty(len(ori_p))
	for i in np.arange(len(_data.current_price.values)):
		if cur_p[i] < ori_p[i]:
			is_discounted[i] = 1
		else:
			is_discounted[i] = 0

	_data['is_discounted'] = is_discounted
	return _data






# Get the country it was made in
def getCountry(_data):

	import numpy as np
	import pandas as pd
	from re import search

	country = []
	country_num = np.empty(len(_data.current_price.values))
	for i in np.arange(len(_data.current_price.values)):
		title = _data.Listing_title.values[i]
		if search('MIM', title):
			country.append('Mexico')
			country_num[i] = 1
		elif search('American', title):
			country.append('USA')
			country_num[i] = 2
		elif search('Japanese', title):
			country.append('Japan')
			country_num[i] = 3
		elif search('Korean', title) or search('Korea', title):
			country.append('Korea')
			country_num[i] = 4
		else:
			country.append('Other')
			country_num[i] = 0

	_data['country'] = country
	_data['country_num'] = country_num
	return _data








# Putting the prices into bins for classification models
def binPrices(_data, _bins):

	import numpy as np
	import pandas as pd
	from scipy import stats

	# Get the log prices
	prices = _data.log_current_price.values

	# Fit a normal PDF to the logged prices
	loc, scale = stats.norm.fit(prices)

	# Put prices into categorical bins using a PPF

	# Creating bin edges
	bins = _bins
	edges = np.empty(bins-1)
	for b in np.arange(bins-1):
		edges[b] = stats.norm.ppf(((b+1)/bins), loc=loc, scale=scale)

	# Creating bin centres
	centres = np.empty(bins)
	for c in np.arange(bins):
		centres[c] = stats.norm.ppf(((2*c+1)/2)/bins, loc=loc, scale=scale)

	cen = pd.DataFrame(centres)
	cen.to_csv('bin_centres.csv', index=False)

	# Binning the prices
	i = 0
	which_bin = np.empty(len(prices))
	centre_val = np.empty(len(prices))
	for p in prices:
		if p < edges[0]:
			bin_ = 0
			centre = np.exp(centres[0])
		elif p > edges[-1]:
			bin_ = bins-1
			centre = np.exp(bins-1)
		else:
			for e in np.arange(len(edges)):
				if p > edges[e]:
					bin_ = e+1
					centre = np.exp(centres[e+1])
				else:
					bin_ = bin_
					centre = centre

		which_bin[i] = bin_
		centre_val[i] = centre

		i += 1

	_data['binned_prices'] = which_bin
	_data['bin_centres'] = centre_val
	return _data
