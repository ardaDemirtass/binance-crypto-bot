import pandas as pd
from sklearn.linear_model import LinearRegression
from modelbase import BaseModel
import pickle
import os
from sklearn.preprocessing import PolynomialFeatures
from binanceapibase import binanceAPI
import matplotlib.pyplot as plt
from loadmodels import LoadModel
from sklearn.preprocessing import StandardScaler
from prmodel import PrModel

class LrModel(BaseModel):
    def __init__(self, input: pd.DataFrame, output: pd.DataFrame, symbol : str):
        super().__init__(input, output, symbol)
        self.__lr = LinearRegression()

    def CreateModel(self):
        self.__lr.fit(self.ScaledX, self.ScaledY)
        self.SetIsModelCreated()
    
    def SaveModel(self):
        if not os.path.exists(f"{self.Symbol}"):
            os.mkdir(f"{self.Symbol}")
        modelFileName = f"{self.Symbol}/LR.pickle"
        pickle.dump(self, open(modelFileName, "wb"))
    
    def Predict(self, pr):
        prediction = self.scy.inverse_transform(self.__lr.predict(self.scx.fit_transform(pr)))
        return prediction


"""
klines = binanceAPI.priceHistory("BTCBUSD")
prices = []
for kline in klines:
    prices.append(float(kline[4]))

#print(prices)
x = list(range(len(prices)))
pricesDF = pd.DataFrame(data=prices, index=x, columns=['price'])
xDF = pd.DataFrame(data=x, index=x, columns=['index'])
all = pd.concat([xDF, pricesDF], axis=1)
print(all)
lr = LrModel(xDF, pricesDF, "BTCBUSD")
lr.CreateModel()
lr.SaveModel()
lm = LoadModel("BTCBUSD", "LinearRegression")
plt.plot(xDF, pricesDF)
xxx = PolynomialFeatures(degree=2)
xx = xxx.fit_transform(xDF)
plt.scatter(xDF, lm.Model.predict(xDF))
plt.show()

"""