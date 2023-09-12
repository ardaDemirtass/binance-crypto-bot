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

print("type **help for commands")
while True:
    command = input('->')
    commandSplit = command.split('-')
    if commandSplit[0] == "**drawgraph":
        xyz = XY(commandSplit[1])#class to create x and y data of model
        if commandSplit[2] == "PR":
            model = PrModel(xyz, commandSplit[1], 2)
        elif commandSplit[2] == "LR":
            model = LrModel(xyz,commandSplit[1])
        elif commandSplit[2] == "SVR":
            model = SvrModel(xyz, commandSplit[1])
        model.CreateModel()
        model.DrawGraph()

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
                model = PrModel(xy, symbol, 2)
            elif regtype == "SVR":
                model = SvrModel(xy, symbol)
            model.CreateModel()
            model.SaveModel()
    elif counter == 60:
            counter = 0
    bot.Start()
    counter += 1
    print(counter)
    time.sleep(1)
    



