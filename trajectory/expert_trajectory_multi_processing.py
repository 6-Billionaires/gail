import pandas as pd
import numpy as np
from glob import glob
import multiprocessing
from concurrent.futures import ThreadPoolExecutor
import os


def count_trans(df):
    cnt = 0
    for i in range(len(df)):
        if df.loc[i][0] == 1:
            cnt += 1
    return cnt


def one(name, data):

    if 'quote' not in data:
        return

    name = "action_list/actions"+name+".csv"

    if name in glob('action_list/*'):
        print(name, ': already saved')
        return

    print(name)

    # if 'multi_actions/actions'+name not in data:
    #     return

    df = pd.read_csv(data)

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

    actions.to_csv(name)
    print('saved: ', name)


if __name__ == '__main__':

    l = []

    print()

    for data in glob('../data/*'):
        l.append(data)

    with ThreadPoolExecutor(max_workers=16) as Executor:
        # jobs = [Executor.submit(get_test_news, u) for u in range(66466, 44882, -1)]
        jobs = [Executor.submit(one, l[d][8:25], l[d]) for d in range(0, len(l))]
        # jobs = [Executor.submit(get_news, u) for u in range(66485, 66460, -1)]
