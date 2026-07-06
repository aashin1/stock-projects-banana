import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

stocks = ["AAPL"]

def get_stock(ticker):
        data = yf.download(ticker, start = '2020-01-01', end = '2026-01-01') 
        return data
for stock in stocks:
    data = get_stock(stock)
    raw_price = data["Close"]
    MA20=data["Close"].rolling(window=20).mean()
    MA50=data["Close"].rolling(window=50).mean()
    data["Signal"] = (MA20 > MA50).astype(int)
    data["MA20"] = MA20
    data["MA50"] = MA50
print(data[["Close", "MA20", "MA50", "Signal"]].tail(10))
plt.plot(raw_price, label = 'Raw Close Price')
plt.plot(MA20, label = 'Rolling Mean 20 Days')
plt.plot(MA50, label = 'Rolling Mean 50 Days')
plt.title("Raw Closing price, MA20, MA50")
plt.legend()
plt.show()
