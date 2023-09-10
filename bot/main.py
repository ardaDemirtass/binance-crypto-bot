def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

import pandas as pd
from lrmodel import LrModel
from prmodel import PrModel
from loadmodels import LoadModel
from binanceapibase import binanceAPI
import os
from positionsymbol import Symbol
from bot import Bot
from xy import XY
import time
import os

symbols = input("WRITE SYMBOLS (EXAMPLE:ETHBUSD,ETHBUSD) : ")
symbolList = symbols.split(',')
regtype = input("LINEAR REG or POLYNOMIAL REG (TYPE LinearRegression or PolynomialRegression) : ")

bot = Bot(symbolList, regtype)
counter = 0
while True:
    for symbol in symbolList:
        if counter == 0:
            xy = XY(symbol)#class to create x and y data of model
            xy.SetXY()
            if regtype == "LinearRegression":
                model = LrModel(xy.X, xy.Y, symbol)
            elif regtype == "PolynomialRegression":
                model = PrModel(xy.X, xy.Y, symbol, 2)
            model.CreateModel()
            model.SaveModel()
        if counter == 60:
            counter = 0
    bot.Start()
    counter += 1
    print(counter)
    time.sleep(1)
    



