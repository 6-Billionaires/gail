import pandas as pd
import glob
from concurrent.futures import ThreadPoolExecutor
import numpy as np


def create_obs(ticker):
    print(ticker)
    quote = pd.read_csv(glob.glob(ticker+'/*-quote.csv')[0], index_col=0)
    order = pd.read_csv(glob.glob(ticker+'/*-order.csv')[0], index_col=0)

    date = glob.glob(ticker+'/*')[0][22:30]
    date = date[:4]+'-'+date[4:6]+'-'+date[6:]

    quote_start = quote.index.get_loc(date + ' 09:06:00')
    quote_end = quote.index.get_loc(date + ' 15:00:00')

    order_start = order.index.get_loc(date + ' 09:06:00')
    order_end = order.index.get_loc(date + ' 15:00:00')

    quote_window = quote[quote_start:quote_end]
    order_window = order[order_start:order_end]

    # print('quote len: ', len(quote_window))
    # print('order len: ', len(order_window))

    data = pd.concat([quote_window, order_window], axis=1)
    # print('data shape: ', data.shape)

    all_history = pd.DataFrame([])

    for i in range(len(quote_window)):
        history = quote[quote_start+i-60:quote_start+i]['Price(last excuted)']
        history = pd.DataFrame(history.values.reshape([1, 60]))
        all_history = all_history.append(history, ignore_index=True)
        if i % 1000 == 0:
            print(i)
    all_history.index = data.index
    # print('all_history shape: ', all_history.shape)

    data_with_history = pd.concat([data, all_history], axis=1)
    # print('data history shape: ', data_with_history.shape)

    data_with_history.to_csv('expert_obs/'+ticker[6:]+'.csv')
    print(ticker[6:] + ': done')


if __name__ == '__main__':

    tickers = []

    for ticker in glob.glob('data1/*'):
        tickers.append(ticker)

    with ThreadPoolExecutor(max_workers=16) as Executor:
        jobs = [Executor.submit(create_obs, t) for t in tickers]