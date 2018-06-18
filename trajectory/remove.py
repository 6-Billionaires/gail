import os
import pandas as pd
from glob import glob

order = pd.read_csv('../data/0-000430-20180503-order.csv')
quote = pd.read_csv('../data/0-000430-20180503-quote.csv')

obs = order.merge(quote)
obs.to_csv('test_obs.csv')
