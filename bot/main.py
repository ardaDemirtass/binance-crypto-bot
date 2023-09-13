def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

import pandas as pd
from model.lrmodel import LrModel
from model.prmodel import PrModel
from model.loadmodels import LoadModel
from binanceapi.binanceapibase import binanceAPI
import os
from position.positionsymbol import Symbol
from bot import Bot
from xy import XY
import time
import os
from model.svrmodel import SvrModel
from model.graph import DrawGraph
import numpy as np

print("type **help for commands")
while True:
    command = input('->')
    commandSplit = command.split('-')
    if commandSplit[0] == "**drawgraph":
        xy = XY(commandSplit[1])#class to create x and y data of model
        lrmodel = LrModel(xy, commandSplit[1])
        svrmodel = SvrModel(xy, commandSplit[1])
        prmodel = PrModel(xy, commandSplit[1], 4)
        lrmodel.CreateModel()
        svrmodel.CreateModel()
        prmodel.CreateModel()
        arr1 = xy.X.values
        arr2 = np.array(range(len(arr1), len(arr1) + 700))
        arrconc = np.append(arr1, arr2)
        arrconcdf = pd.DataFrame(data=arrconc, index=arrconc, columns=['x'])
        DrawGraph(xy, arrconcdf, [lrmodel.Predict(arrconcdf),prmodel.Predict(arrconcdf),svrmodel.Predict(arrconcdf)], commandSplit[1])

    if commandSplit[0] == "**runbot":
        break

    if commandSplit[0] == "**help":
        print("to draw graph, type **drawgraph-SYMBOL-ALGORITH(example:**drawgraph-ETHBUSD-LR)")
        print("to run bot, type **runbot")

symbols = input("WRITE SYMBOLS (EXAMPLE:ETHBUSD,BTCBUSD) : ")
symbolList = symbols.split(',')
regtype = input("CHOOSE THE ALGORITHM (TYPE LR or PR or SVR) : ")

bot = Bot(symbolList, regtype)
counter = 0
while True:
    if counter == 0:
        for symbol in symbolList:
            xy = XY(symbol)#class to create x and y data of model
            if regtype == "LR":
                model = LrModel(xy, symbol)
            elif regtype == "PR":
                model = PrModel(xy, symbol, 4)
            elif regtype == "SVR":
                model = SvrModel(xy, symbol)
            model.CreateModel()
            model.SaveModel()
        bot.SetModels()
    bot.Start()
    counter += 1
    print(counter)
    if counter == 10:
        counter = 0
    time.sleep(1)
    



