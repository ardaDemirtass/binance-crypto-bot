import pandas as pd
from sklearn.linear_model import LinearRegression
from model.modelbase import BaseModel
import pickle
import os
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
from xy import XY

class PrModel(BaseModel):
    def __init__(self, xy : XY, degree : int):
        super().__init__(xy)
        self.__lr = LinearRegression()
        self.__pf = PolynomialFeatures(degree=degree)

    def CreateModel(self):
        x_poly = self.__pf.fit_transform(self.Xtrain)
        self.__lr.fit(x_poly, self.Ytrain)
        self.SetIsModelCreated()

    def SaveModel(self):
        if not os.path.exists(f"savedsymbols/{self.Symbol}"):
            os.mkdir(f"savedsymbols/{self.Symbol}")
        filename = f"savedsymbols/{self.Symbol}/PR.pickle"
        if os.path.isfile(filename):
            os.remove(filename)
        pickle.dump(self, open(filename, "wb"))

    def Predict(self, pr):
        x_poly = self.__pf.fit_transform(pr)
        prediction = self.__lr.predict(x_poly)
        return prediction
    
    def PredictAvg(self, x):
        sum = 0
        for i in x:
            sum+= self.Predict([[i]])
        return sum / 700
