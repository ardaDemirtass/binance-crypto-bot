import pandas as pd
from sklearn.svm import SVR
from model.modelbase import BaseModel
import pandas as pd
import os
import pickle

class SvrModel(BaseModel):
    def __init__(self, input: pd.DataFrame, output: pd.DataFrame, symbol: str):
        super().__init__(input, output, symbol)
        self.__svr = SVR(kernel="rbf") 

    def CreateModel(self):
        self.__svr.fit(self.ScaledX, self.ScaledY)
        self.SetIsModelCreated()

    def SaveModel(self):
        if not os.path.exists(f"{self.Symbol}"):
            os.mkdir(f"{self.Symbol}")
        modelFileName = f"{self.Symbol}/SVR.pickle"
        pickle.dump(self, open(modelFileName, "wb"))

    def Predict(self, pr):
        prediction = self.scy.inverse_transform(self.__svr.predict(self.scx.fit_transform(pr)).reshape(1,1))
        return prediction