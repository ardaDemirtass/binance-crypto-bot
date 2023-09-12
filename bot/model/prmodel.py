import pandas as pd
from sklearn.linear_model import LinearRegression
from model.modelbase import BaseModel
import pickle
import os
from sklearn.preprocessing import PolynomialFeatures

class PrModel(BaseModel):
    def __init__(self, input: pd.DataFrame, output: pd.DataFrame, symbol: str, degree : int):
        super().__init__(input, output, symbol)
        self.__lr = LinearRegression()
        self.__pf = PolynomialFeatures(degree=degree)

    def CreateModel(self):
        x_poly = self.__pf.fit_transform(self.ScaledX)
        self.__lr.fit(x_poly, self.ScaledY)
        self.SetIsModelCreated()

    def SaveModel(self):
        if not os.path.exists(f"{self.Symbol}"):
            os.mkdir(f"{self.Symbol}")
        filename = f"{self.Symbol}/PR.pickle"
        pickle.dump(self, open(filename, "wb"))

    def Predict(self, pr):
        x_poly = self.__pf.fit_transform(pr)
        prediction = self.scy.inverse_transform(self.__lr.predict(self.scx.fit_transform(x_poly)))
        return prediction
    