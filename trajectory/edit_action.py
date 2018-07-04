import pandas as pd
import glob
from concurrent.futures import ThreadPoolExecutor
import os

def edit_acts(ticker):
    print(ticker)
    quote = pd.read_csv(glob.glob(ticker+'/*-quote.csv')[0], index_col=0)

    date = glob.glob(ticker+'/*')[0][25:33]
    date_dash = date[:4]+'-'+date[4:6]+'-'+date[6:]

    quote_start = quote.index.get_loc(date_dash + ' 09:06:00')
    quote_end = quote.index.get_loc(date_dash + ' 15:00:00')

    print(quote_start)
    print(quote_end)

    action = pd.read_csv('action_list/actions0-'+str(ticker[9:])+'-'+date+'.csv', index_col=0)
    action = action[quote_start:quote_end]
    action.index = range(quote_end-quote_start)

    action.to_csv('expert_actions/action'+str(ticker[9:])+'.csv')
    print('expert_actions/action'+str(ticker)+'.csv: done')


if __name__ == '__main__':

    tickers = []

    for ticker in glob.glob('../data1/*'):
        tickers.append(ticker)

    with ThreadPoolExecutor(max_workers=16) as Executor:
        jobs = [Executor.submit(edit_acts, t) for t in tickers]