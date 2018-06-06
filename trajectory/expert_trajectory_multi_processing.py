import pandas as pd
import numpy as np
from glob import glob
import multiprocessing
from concurrent.futures import ThreadPoolExecutor

df = pd.DataFrame().to_csv('actions.csv')

count = 0

def count_trans(df):
    cnt = 0
    for i in range(len(df)):
        if df.loc[i][0] == 1:
            cnt += 1
    return cnt

def one(data) :

    if 'quote' not in data:
        return

    df = pd.read_csv(data)
    prev_actions = pd.read_csv('actions.csv', index_col=0)

    actions = pd.DataFrame()

    w = 6  # window size
    i = 0  # start index

    while i+w <= len(df):
        window = df.loc[i:i+w]['Price(last excuted)']
        min_p = np.min(window)
        max_p = np.max(window)
        min_arg = np.argmin(window)
        max_arg = np.argmax(window)

        actions = actions.append([0] * (max_arg-i+1), ignore_index=True)

        if min_arg < max_arg:
            if max_p - min_p >= 1.5:
                actions.loc[i] = [1]  # buy
                actions.loc[max_arg] = [2]  # sell
                print('new transaction')
        i = max_arg + 1

    actions = actions.append([0] * (w-1), ignore_index=True)
    actions.columns = ['0']

    new_actions = actions.append(prev_actions, ignore_index=True)
    print('num merged: ', len(new_actions))
    new_actions.to_csv("actions.csv")

if __name__ == '__main__':

    l = []
    for data in glob('data/*'):
        l.append(data)

    with ThreadPoolExecutor(max_workers=16) as  Executor:
        # jobs = [Executor.submit(get_test_news, u) for u in range(66466, 44882, -1)]
        jobs = [Executor.submit(one, l[d]) for d in range(0, len(l))]
        # jobs = [Executor.submit(get_news, u) for u in range(66485, 66460, -1)]
