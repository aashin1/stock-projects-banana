import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

while True:
    Choose_stock = input("What stock? ")

    stocks = [Choose_stock]


    def get_stock(ticker):
            data = yf.download(ticker, start = '2025-01-01', end = pd.Timestamp.today().strftime('%Y-%m-%d')) 
            return data
    data = get_stock(Choose_stock)
    if data.empty:
        print("That one does not exist!")
    else:
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
        plt.title(f"Raw Closing price, MA20, MA50 of {Choose_stock}")

        plt.xlabel("Date")
        plt.ylabel("Price ($)")
        plt.legend()
        plt.xticks(rotation=45, fontsize=8)
        plt.xlabel("Date", fontsize=10)

        plt.show()
        break
