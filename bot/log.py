from positionsymbol import Symbol
from datetime import datetime

class Log:
    def __init__(self, symbol : Symbol):
        self.__Symbol = symbol

    def ExitLog(self, exitPrice):
        if self.__Symbol.Buyprice < exitPrice:
            print("profit")
        else:
            print("loss")

    def EnterLog(self):
        text = f"""
***ENTER LOG***
SYMBOL : {self.__Symbol.Symbol}
ENTER PRICE : {self.__Symbol.Buyprice}
TARGET PRICE : {self.__Symbol.Sellprice}
STOP PRICE : {self.__Symbol.Stopprice}
DATE : {datetime.now()}
---------------
                """
        text_file = open("log.txt", "a")
        text_file.write(text + '\n')
        text_file.close()
    
