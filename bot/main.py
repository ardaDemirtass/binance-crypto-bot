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
from svrmodel import SvrModel

symbols = input("WRITE SYMBOLS (EXAMPLE:ETHBUSD,BTCBUSD) : ")
symbolList = symbols.split(',')
regtype = input("CHOOSE THE ALGORITHM (TYPE LR or PR or SVR) : ")

bot = Bot(symbolList, regtype)
counter = 0
while True:
    if counter == 0:
        for symbol in symbolList:
            xy = XY(symbol)#class to create x and y data of model
            xy.SetXY()
            if regtype == "LR":
                model = LrModel(xy.X, xy.Y, symbol)
            elif regtype == "PR":
                model = PrModel(xy.X, xy.Y, symbol, 2)
            elif regtype == "SVR":
                model = SvrModel(xy.X, xy.Y, symbol)
            model.CreateModel()
            model.SaveModel()
    elif counter == 60:
            counter = 0
    bot.Start()
    counter += 1
    print(counter)
    time.sleep(1)
    



