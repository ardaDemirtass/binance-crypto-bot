import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import pickle

class LoadModel:
    def __init__(self, symbol, type):
        self.__Symbol = symbol
        self.__Type = type
        self.__Model = None
        self.__Load()
        
    def __Load(self):
        with open(f'savedsymbols/{self.__Symbol}/{self.__Type}.pickle', 'rb') as f:
            self.__Model = pickle.load(f)

    @property
    def Model(self):
        return self.__Model
    
    
        