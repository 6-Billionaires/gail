import pandas as pd
import numpy as np
from glob import glob

df = pd.DataFrame().to_csv('expert_actions.csv')

for data in glob('data/*'):

    if 'quote' not in data:
        continue

    print(data)
    df = pd.read_csv(data)
    prev_actions = pd.read_csv('expert_actions.csv', index_col=0)

    def count_trans(df):
        cnt = 0
        for i in range(len(df)):
            if df.loc[i][0] == 1:
                cnt += 1
        return cnt


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

    print('actions: ', actions)

    print("num of new actions: ", len(actions))

    print('num of new transactions: ', count_trans(actions))

    new_actions = actions.append(prev_actions, ignore_index=True)
    print('num merged: ', len(new_actions))
    new_actions.to_csv("expert_actions.csv")
    print('done')


