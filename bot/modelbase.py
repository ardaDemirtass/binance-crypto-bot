import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from abc import ABC, abstractmethod
from sklearn.model_selection import train_test_split

class BaseModel(ABC):
    def __init__(self, input : pd.DataFrame,  output : pd.DataFrame, symbol : str):
        self.__input = input
        self.__output = output
        self.__xtrain : pd.DataFrame
        self.__xtest : pd.DataFrame
        self.__ytrain : pd.DataFrame
        self.__ytest : pd.DataFrame
        self.__sc = StandardScaler()
        self.__sc2 = StandardScaler()
        self.__GetDataReady()
        self.__isModelCreated = False
        self.__symbol = symbol

    def SetIsModelCreated(self):
        self.__isModelCreated = True

    @property
    def Symbol(self):
        return self.__symbol

    @property
    def IsModelCreated(self):
        return self.__isModelCreated

    @property
    def sc(self):
        return self.__sc
    
    @property
    def sc2(self):
        return self.__sc2

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
        self.__xtrain, self.__xtest, self.__ytrain, self.__ytest = train_test_split(self.__input, self.__output, test_size=0.33, random_state=0)
        self.__xtrain = self.__xtrain.sort_index()
        self.__ytrain = self.__ytrain.sort_index()

    def __GetDataReady(self):
        self.__CreateTrainTest()

    @abstractmethod
    def CreateModel(self):
        pass

    @abstractmethod
    def SaveModel(self):
        pass