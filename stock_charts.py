import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt 

stocks = ["AAPL", "TSLA", "MSFT", "AMZN", "NVDA"]

def get_stock(ticker):
    data = yf.download(ticker, start = '2020-01-01', end = '2026-01-01') 
    return data
for_data = []
for stock in stocks:
    data = get_stock(stock)
    returns = data["Close"].pct_change()
    print(returns.describe())
    for_data.append({"stock": stock, "mean": returns.mean().iloc[0], "std_deviation": returns.std().iloc[0], "return per unit of risk": returns.mean().iloc[0]/returns.std().iloc[0]})
    returns.plot(
        kind='hist',
        edgecolor ='black',
    )
print(pd.DataFrame(for_data).sort_values(by='mean', ascending=False))
# plt.show()




