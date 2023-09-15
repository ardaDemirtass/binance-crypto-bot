import pandas as pd
from sklearn.linear_model import LinearRegression
from model.modelbase import BaseModel
import pickle
import os
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
from model.loadmodels import LoadModel
from sklearn.preprocessing import StandardScaler
from model.prmodel import PrModel
from xy import XY
import numpy as np
import statsmodels as sm

class LrModel(BaseModel):
    def __init__(self, xy : XY):
        super().__init__(xy)
        self.__lr = LinearRegression()

    def CreateModel(self):
        self.__lr.fit(self.ScaledX, self.ScaledY)
        self.SetIsModelCreated()
    
    def SaveModel(self):
        if not os.path.exists(f"savedsymbols/{self.Symbol}"):
            os.mkdir(f"savedsymbols/{self.Symbol}")
        modelFileName = f"savedsymbols/{self.Symbol}/LR.pickle"
        if os.path.isfile(modelFileName):
            os.remove(modelFileName)
        pickle.dump(self, open(modelFileName, "wb"))
    
    def Predict(self, pr):
        #prediction = self.scy.inverse_transform(self.__lr.predict(self.scx.fit_transform(pr)))
        #return prediction
        prediction = self.scy.inverse_transform(self.__lr.predict(self.scx.transform(pr)))
        return prediction
    
    def PredictAvg(self, x):
        sum = 0
        for i in x:
            sum+= self.Predict([[i]])
        return sum / 700
    



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