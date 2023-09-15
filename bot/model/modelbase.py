import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from abc import ABC, abstractmethod
from sklearn.model_selection import train_test_split
from xy import XY

class BaseModel(ABC):
    def __init__(self, xy : XY):
        self.__input = xy.X
        self.__output = xy.Y
        self.__xtrain : pd.DataFrame
        self.__xtest : pd.DataFrame
        self.__ytrain : pd.DataFrame
        self.__ytest : pd.DataFrame
        self.__scx = StandardScaler()
        self.__scy = StandardScaler()
        self.__scaledx = None
        self.__scaledy = None
        self.__GetDataReady()
        self.__isModelCreated = False
        self.__symbol = xy.Symbol

    def SetIsModelCreated(self):
        self.__isModelCreated = True

    @property
    def Symbol(self):
        return self.__symbol

    @property
    def ScaledX(self):
        return self.__scaledx
    
    @property
    def ScaledY(self):
        return self.__scaledy

    @property
    def Symbol(self):
        return self.__symbol

    @property
    def IsModelCreated(self):
        return self.__isModelCreated

    @property
    def scx(self):
        return self.__scx
    
    @property
    def scy(self):
        return self.__scy

    @property
    def Xtrain(self):
        return self.__xtrain
    
    @property
    def Xtest(self):
        return self.__xtest
    
    @property
    def Ytrain(self):
        return self.__ytrain
    
    @property
    def Ytest(self):
        return self.__ytest

    @property
    def Input(self):
        return self.__input
    
    @property
    def Output(self):
        return self.__output
    
    @property
    def AllData(self):
        return pd.concat([self.__input, self.__output], axis=1)

    def __CreateTrainTest(self):
        self.__xtrain, self.__xtest, self.__ytrain, self.__ytest = train_test_split(self.__input.values, self.__output.values, test_size=0.3, random_state=0)
        self.__scaledx = self.__scx.fit_transform(self.__xtrain)
        self.__scaledy = self.__scy.fit_transform(self.__ytrain)

    def __GetDataReady(self):
        self.__CreateTrainTest()

    @abstractmethod
    def CreateModel(self):
        pass

    @abstractmethod
    def SaveModel(self):
        pass

    @abstractmethod
    def Predict(self, pr):
        pass

    @abstractmethod
    def PredictAvg(self, x):
        pass
