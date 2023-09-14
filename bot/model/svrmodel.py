import pandas as pd
from sklearn.svm import SVR
from model.modelbase import BaseModel
import pandas as pd
import os
import pickle
import matplotlib.pyplot as plt
from xy import XY
import statsmodels as sm

class SvrModel(BaseModel):
    def __init__(self, xy : XY):
        super().__init__(xy)
        self.__svr = SVR(kernel="rbf") 

    def CreateModel(self):
        self.__svr.fit(self.ScaledX, self.ScaledY)
        self.SetIsModelCreated()

    def SaveModel(self):
        if not os.path.exists(f"savedsymbols/{self.Symbol}"):
            os.mkdir(f"savedsymbols/{self.Symbol}")
        modelFileName = f"savedsymbols/{self.Symbol}/SVR.pickle"
        if os.path.isfile(modelFileName):
            os.remove(modelFileName)
        pickle.dump(self, open(modelFileName, "wb"))

    def Predict(self, pr):
        prediction = self.scy.inverse_transform(self.__svr.predict(self.scx.transform(pr)).reshape(-1,1))
        return prediction
    
    def PredictAvg(self, x):
        sum = 0
        for i in x:
            sum+= self.Predict([[i]])
        return sum / 700
    

    
