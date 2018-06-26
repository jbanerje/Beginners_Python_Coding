import pandas as pd
import os
import quandl
import time

#auth_tok = "QzbDZuyCjX5rt1_TCm9p"
quandl.ApiConfig.api_key = 'QzbDZuyCjX5rt1_TCm9p'

data = quandl.Dataset('WIKI/AAPL').data()

dataset_data = quandl.Dataset('WIKI/AAPL').data(params={ 'start_date':'2001-01-01', 'end_date':'2010-01-01', 'collapse':'annual', 'transformation':'rdiff', 'rows':4 })

print(dataset_data.)
