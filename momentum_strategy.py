import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf

while True: 
    
    Choose_stock = input("What stock? ")
    stocks = [Choose_stock]
        
    def get_stock(ticker):
        data=yf.download(ticker, period="2y")
        return data
    data = get_stock(Choose_stock)

    if data.empty:
        
        print("That one does not exist!")
   
    else:

        change_list = data["Close"].iloc[:, 0].pct_change().dropna().rolling(20).sum()
        returns = data["Close"].iloc[:, 0].pct_change()

        data["Signal"] = (change_list > 0 ).astype(int)

        daily_returns = data["Signal"].dropna() * returns 
        cum_returns = (1+returns).cumprod().dropna()
        strategy = (1 + daily_returns).cumprod()

        plt.plot(cum_returns, label ="Buy and Hold")
        plt.plot(strategy, label ="Daily Return")
        plt.legend()
        plt.xlabel("Dates")
        plt.ylabel("Cumulative Return (1 = Starting Value)")
        plt.xticks(rotation=45, fontsize=8)
        plt.title(f"{Choose_stock} Momentum Strategy vs Buy and Hold")
        plt.show()
        break


