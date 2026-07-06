import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, kurtosis, skew 
import yfinance as yf

while True:
    Choose_stock = input("Which stock? ")

    stocks = [Choose_stock]
    def get_stock(ticker):
        data = yf.download(ticker, start = '2024-01-01', end = '2026-01-01') 
        return data

    data = get_stock(Choose_stock)
    if data.empty:
        print("That one does not exist!")
    else:
        returns = data["Close"].iloc[:, 0].pct_change().dropna()

        mu, std = norm.fit(returns)
        excess_kurtosis = kurtosis(returns, fisher=True)
        skewness = skew(returns)
        x = np.linspace(returns.min(), returns.max(), 500)
        y = norm.pdf(x, loc = mu, scale = std)
        minimum = returns.min()
        maximum = returns.max()
        plt.suptitle(f"{Choose_stock} Daily Returns vs Theorical Normal Model")
        plt.title(f"Kurtosis of {excess_kurtosis:.3f} + skewness of {skewness:.3f}") 
        plt.hist(returns, bins=50, density=True, label="Actual Returns")
        plt.plot(x, y, label="Theoretical Returns")
        plt.axvline(x=mu, label=f"Average Return:{mu:.3f}", color="red")
        plt.xlabel("Daily Return")
        plt.ylabel("Density")
        plt.legend()
        plt.show()

        break
