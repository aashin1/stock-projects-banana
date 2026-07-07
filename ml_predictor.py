import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


choose_stock =input("What stock? ")

def get_stock(ticker):
    data=yf.download(ticker, period="5y")
    return data

data = get_stock(choose_stock)
Returns = data["Close"].iloc[:, 0].pct_change().dropna()
MA20 = data["Close"].iloc[:, 0].rolling(window=20).mean() # of returns
MA50 = data["Close"].iloc[:, 0].rolling(window=50).mean() # of returns
Volatility = data["Close"].iloc[:, 0].rolling(window=20).std()
Volume = data["Volume"].iloc[:, 0].pct_change()
data["Signal"] = (MA20 > MA50).astype(int)
data["MA20"] = MA20
data["MA50"] = MA50
data["Target"] = ((Returns.shift(-1)) > 0).astype(int)
data["Volume"] = Volume
data["Volatility"] = Volatility

data = data[["Signal", "MA20", "MA50","Target", "Volume", "Volatility"]].dropna()


x = data[["Signal", "MA20", "MA50","Volume","Volatility"]]
y = data["Target"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size =.2, shuffle=False )
model = RandomForestClassifier()
model.fit(x_train, y_train)
predictions = model.predict(x_test) 
print("Confidence of:", accuracy_score(y_test, predictions))


