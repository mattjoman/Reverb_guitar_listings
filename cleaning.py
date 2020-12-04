import numpy as np
import pandas as pd

# Get the data
data = pd.read_csv('big_dataset.csv')
print(data.info())

################################################################################################
										# CLEANING #
################################################################################################





# Dropping rows with 'None' (there aren't many)
indexes = data[ data['Listing_title'] == 'None'].index
data.drop(indexes , inplace=True)





# Getting floats from the price strings
data['original_price'] = data.Original_price.map(lambda x: float(x.replace('£', '').replace('GBP', '').replace(',', '')))
data['current_price'] = data.Current_price.map(lambda x: float(x.replace('£', '').replace('GBP', '').replace(',', '')))





################################################################################################
											# SAVING #
################################################################################################





data.to_csv('cleaned_big_dataset.csv', index=False)
