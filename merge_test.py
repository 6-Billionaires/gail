import pandas as pd
import numpy as np

prevs = pd.read_csv('expert_actions.csv', index_col=0)[:10]

print(prevs)
print('prevs desc: ', prevs.columns)
actions = pd.DataFrame()

w = 6  # window size
i = 0  # start index

df = pd.read_csv('/Users/shatapy/Desktop/GAIL_bill/data/0-226360-20180423-quote.csv')

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
    i = max_arg + 1

print('action done')

actions = actions[:10]
print(actions)
print('actions desc: ', actions.describe())
