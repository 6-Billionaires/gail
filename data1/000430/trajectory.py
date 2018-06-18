import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('0-000430-20180503-quote.csv')
actions = pd.DataFrame([0, 0])

len_df = len(df)
prices = df.loc[0:len_df]['Price(last excuted)']
prices.plot()
plt.show()

p = 2
a = 3

for i in range(p, 200):
    if(df.loc[i-p]['Price(last excuted)'] < df.loc[i]['Price(last excuted)'] < df.loc[i+a]['Price(last excuted)']):
        actions = actions.append([1])
    else:
        actions = actions.append([0], ignore_index=True)
    price = df.loc[i]['Price(last excuted)']
    print(i, price)


print(actions[:][0])

