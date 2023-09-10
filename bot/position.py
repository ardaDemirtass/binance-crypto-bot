import pandas as pd
import numpy as np
from positionsymbol import Symbol
from datetime import datetime
from binanceapibase import binanceAPI

class Position:
    def __init__(self, symbol : Symbol):
        self.__Symbol = symbol
        self.__Date = datetime.now() 
        self.__InPosition = False
        binanceAPI.apiKey = "s5GgONkYNu9Vdzhw9A0Q0YiPPVWJN96huS3VSMRWVyuwwj4xjPln4Aic3EUPf9gA"
        binanceAPI.apiSecret = "4scsNT2GvO1KR6jLn9zPv9yfqarnhlt3lNNvEBxdMHdWZAN9dasGtrvlyatf3iF8"
        
    @property
    def Date(self):
        return self.__Date
    
    @property
    def PositionDetails(self):
        return self.__Symbol
    
    def StartPosition(self):
        if self.__InPosition:
            print("you cannot call start position function when you are in position")
        else:
            #binanceAPI.buy(self.__Symbol.Symbol)
            pass

    def ExitPosition(self):
        if not self.__InPosition:
            print("you cannot call exit position function when you are not in position")
        else:
            #binanceAPI.sell(self.__Symbol.Symbol)
            pass
