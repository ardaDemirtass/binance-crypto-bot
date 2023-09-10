class Symbol:
    def __init__(self, symbol : str, buyprice : int, sellprice : int, stopprice : int):
        self.__symbol = symbol
        self.__buyprice = buyprice
        self.__sellprice = sellprice
        self.__stopprice = stopprice

    @property
    def Symbol(self):
        return self.__symbol
    
    @property
    def Buyprice(self):
        return self.__buyprice
    
    @property
    def Sellprice(self):
        return self.__sellprice
    
    @property
    def Stopprice(self):
        return self.__stopprice