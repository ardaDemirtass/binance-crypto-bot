import pandas as pd
from sklearn.linear_model import LinearRegression
from modelbase import BaseModel
import pickle
import os
from sklearn.preprocessing import PolynomialFeatures

class PrModel(BaseModel):
    def __init__(self, input: pd.DataFrame, output: pd.DataFrame, symbol: str, degree : int):
        super().__init__(input, output, symbol)
        self.__lr = LinearRegression()
        self.__pf = PolynomialFeatures(degree=degree)

    def CreateModel(self):
        x_poly = self.__pf.fit_transform(self.Input)
        self.__lr.fit(x_poly, self.Output)
        self.SetIsModelCreated()

    def SaveModel(self):
        if not os.path.exists(f"{self.Symbol}"):
            os.mkdir(f"{self.Symbol}")
        filename = f"{self.Symbol}/PolynomialRegression.pickle"
        pickle.dump(self.__lr, open(filename, "wb"))