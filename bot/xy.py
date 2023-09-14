import pandas as pd
import numpy as np
import requests
from binanceapi.binanceapibase import binanceAPI
from sklearn.preprocessing import StandardScaler

class XY:
    def __init__(self, symbol):
        self.__Symbol = symbol
        self.__X : pd.DataFrame
        self.__Y : pd.DataFrame
        self.__All : pd.DataFrame
        self.__SetXY()

    def __SetXY(self):
        klines = binanceAPI.priceHistory(self.__Symbol)
        prices = []
        for kline in klines:
            prices.append(float(kline[4]))

        x = list(range(len(prices)))
        pricesDF = pd.DataFrame(data=prices, index=x, columns=['price'])
        xDF = pd.DataFrame(data=x, index=x, columns=['index'])
        all = pd.concat([xDF, pricesDF], axis=1)
        self.__All = all
        self.__X = all.iloc[:,0:1]
        self.__Y = all.iloc[:,1:2]

    @property
    def Symbol(self):
        return self.__Symbol

    @property
    def X(self):
        return self.__X
    
    @property
    def Y(self):
        return self.__Y
    
    @property
    def All(self):
        return self.__All
    