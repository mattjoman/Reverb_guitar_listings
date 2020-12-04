import numpy as np
import pandas as pd
from re import search
from scipy import stats

# Get the data
data = pd.read_csv('cleaned_big_dataset.csv')
print(data.info())

################################################################################################
									# FEATURE ENGINEERING #
################################################################################################









# Getting the brand of guitar (improve on this)
def get_brand(x):
	elif search('Squier', x) or search('squier', x):
		return 'Squier'	
	if search('Fender', x) or search('fender', x):
		return 'Fender'
	elif search('Epiphone', x) or search('epiphone', x):
		return 'Epiphone'
	elif search('Gibson', x) or search('gibson', x):
		return 'Gibson'
	elif search('Ibanez', x) or search('ibanez', x):
		return 'Ibanez'
	elif search('Danelectro', x) or search('danelectro', x):
		return 'Danelectro'
	elif search('Schecter', x):
		return 'Schecter'
	elif search('Jackson', x):
		return 'Jackson'
	elif search('ESP', x):
		return 'ESP'
	elif search('Sterling', x):
		return 'Sterling'
	elif search('Ernie Ball', x):
		return 'Ernie Ball'
	elif search('Yamaha', x):
		return 'Yamaha'
	elif search('Paul Reed Smith', x):
		return 'Paul Reed Smith'
	elif search('PRS', x):
		return 'PRS'
	elif search('Charvel', x):
		return 'Charvel'
	elif search('Suhr', x):
		return 'Suhr'

	else:
		return 'Other'

data['brand'] = data.Listing_title.map(lambda x: get_brand(x))










# Convert brands and models to numeric values for modelling
# Make sure the if/elif/else statements match the categories created
def get_brand_num(x):
	if x == 'Fender':
		return 1
	elif x == 'Gibson':
		return 2
	elif x == 'Squier':
		return 3
	elif x == 'Epiphone':
		return 4
	elif x == 'Ibanez':
		return 5
	elif x == 'Danelectro':
		return 6
	elif x == 'Schecter':
		return 7
	elif x == 'Jackson':
		return 8
	elif x == 'ESP':
		return 9
	elif x == 'Ernie Ball':
		return 10
	elif x == 'Sterling':
		return 11
	elif x == 'Yamaha':
		return 12
	elif x == 'Paul Reed Smith':
		return 13
	elif x == 'PRS':
		return 14
	elif x == 'Charvel':
		return 15
	elif x == 'Suhr':
		return 16
	####################
	else:
		return 0

data['brand_num'] = data.brand.map(lambda x: get_brand_num(x))










# Get the model of guitar (strat, tele, les paul, sg, ...)
# include more models and alternative spellings
model = []
for i in np.arange(len(data.original_price.values)):
	title = data.Listing_title.values[i]
	
	if search('Strat', title):
		model.append('Strat')
	elif search('Tele', title):
		model.append('Tele')
	elif search('Jaguar', title):
		model.append('Jaguar')
	elif search('Jazzmaster', title):
		model.append('Jazzmaster')
	elif search('Les Paul', title):
		model.append('Les Paul')
	elif search('SG', title):
		model.append('SG')
	elif search('Firebird', title):
		model.append('Firebird')
	elif search('Flying V', title):
		model.append('Flying V')
	elif search('Jem', title):
		model.append('Jem')

	else:	# Other brand
		model.append('Other')

data['model'] = model










# Convert brands and models to numeric values for modelling
# Make sure the if/elif/else statements match the categories created
def get_model_num(x):
	if x == 'Strat':
		return 1
	elif x == 'Tele':
		return 2
	elif x == 'Jaguar':
		return 3
	elif x == 'Jazzmaster':
		return 4
	elif x == 'Les Paul':
		return 5
	elif x == 'SG':
		return 6
	elif x == 'Firebird':
		return 7
	elif x == 'Flying V':
		return 8
	elif x == 'Jem':
		return 9

	else:
		return 0

data['model_num'] = data.model.map(lambda x: get_model_num(x))










special_score = np.empty(len(data.current_price.values))

rare = np.empty(len(data.current_price.values))
custom_shop = np.empty(len(data.current_price.values))
relic = np.empty(len(data.current_price.values))
vintage = np.empty(len(data.current_price.values))
signature = np.empty(len(data.current_price.values))
case_included = np.empty(len(data.current_price.values))
NOS = np.empty(len(data.current_price.values))
fifties_sixties = np.empty(len(data.current_price.values))
fancy_wood = np.empty(len(data.current_price.values))
signed = np.empty(len(data.current_price.values))
famous = np.empty(len(data.current_price.values))


for i in np.arange(len(data.current_price.values)):
	
	ss = 0
	title = data.Listing_title.values[i]

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

data['rare'] = rare
data['custom_shop'] = custom_shop
data['relic'] = relic
data['vintage'] = vintage
data['signature'] = signature
data['case_included'] = case_included
data['NOS'] = NOS
data['fifties_sixties'] = fifties_sixties
data['fancy_wood'] = fancy_wood
data['signed'] = signed
data['famous'] = famous

data['special_score'] = special_score










# convert the conditions to numerical values
def conv_conditions(x):
	if x == 'Mint':
		return 1
	elif x == 'Excellent':
		return 2
	elif x == 'Very Good':
		return 3
	elif x == 'Good':
		return 4
	elif x == 'Fair':
		return 5
	else:
		return 0

data['condition'] = data.Condition.map(lambda x: conv_conditions(x))










# Calculate the discount
discount = data.original_price.values - data.current_price.values
data['discount'] = discount

# was there a discount?
cur_p = data.current_price.values
ori_p = data.original_price.values
is_discounted = np.empty(len(ori_p))
for i in np.arange(len(data.current_price.values)):
	if cur_p[i] < ori_p[i]:
		is_discounted[i] = 1
	else:
		is_discounted[i] = 0

data['is_discounted'] = is_discounted










# Get the country it was made in
country = []
country_num = np.empty(len(data.current_price.values))
for i in np.arange(len(data.current_price.values)):
	title = data.Listing_title.values[i]
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

data['country'] = country
data['country_num'] = country_num










# Get the length of the description.
data['length'] = data.Listing_title.map(lambda x: len(x))










# Getting the log prices
data['log_current_price'] = data.current_price.map(lambda x: np.log(x))
data['log_original_price'] = data.original_price.map(lambda x: np.log(x))










# Putting the prices into bins for classification models

# Get the log prices
prices = data.log_current_price.values

# Fit a normal PDF to the logged prices
loc, scale = stats.norm.fit(prices)

# Put prices into categorical bins using a PPF

# Creating bin edges
bins = 40
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

data['binned_prices'] = which_bin
data['bin_centres'] = centre_val










################################################################################################
										# SAVING #
################################################################################################

print(data.info())

data.to_csv('engineered_big_dataset.csv', index=False)