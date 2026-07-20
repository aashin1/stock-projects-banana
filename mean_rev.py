import yfinance as yf
import pandas as pd 
import matplotlib.pyplot as plt
from scipy import stats



stock = "MSFT"

def get_stock(ticker):
    data = yf.download(ticker, period= "5y" )
    return data 
data = get_stock(stock)
close = data["Close"].squeeze()
RM = close.rolling(window = 30).mean()
RAW = close
RSTD = close.rolling(window = 30).std()
data["Z Score"] = (RAW - RM) / RSTD
DR = close.pct_change()



positions = []
for z in data["Z Score"]:
    if z >= 2:
        positions.append(-1)
    elif z <= -2:
            positions.append(1)
    else:
        positions.append(0)



data["Position"] = positions
PC = data["Position"].shift(1) * DR
pct = 1 + PC
cum = pct.cumprod()
bh = (1+DR).cumprod()
fig, axes = plt.subplots(3, 1, sharex=True, figsize=(12, 9))

axes[0].plot(data.index, cum, label="Strategy")
axes[0].plot(data.index, bh, label="Buy & Hold")
axes[0].set_ylabel("Growth of $1")
axes[0].legend()

axes[1].plot(data.index, data["Z Score"], label="Z Score")
axes[1].axhline(y=2, color='r')
axes[1].axhline(y=-2, color='r')
axes[1].axhline(y=0, color='gray', linewidth=0.5)
axes[1].set_ylabel("Z Score")

axes[2].step(data.index, data["Position"], label="Position")
axes[2].set_ylabel("Position")

plt.tight_layout()
plt.show()


# print(RM)
# print(RSTD)

