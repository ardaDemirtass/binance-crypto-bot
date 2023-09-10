from binance.client import Client
from abc import ABC, abstractclassmethod
import json
import requests
import pandas as pd

class binanceAPI(object):
    api = pd.read_csv('api.csv')
    apiKey = str(api.iloc[:,0:1].values)
    apiSecret = str(api.iloc[:,1:2].values)
    client = Client(api_key=apiKey, api_secret=apiSecret)

    @classmethod
    def quantity(cls, symbol):
        return float(cls.assetBalance("BUSD")) / float(cls.currentPrice(symbol))

    @classmethod
    def assetBalance(cls, symbol):
        return cls.client.get_asset_balance(asset=symbol)
    
    @classmethod
    def priceHistory(cls, symbol):
        return cls.client.get_historical_klines(symbol, Client.KLINE_INTERVAL_1MINUTE, "12 hours ago UTC")

    @classmethod
    def marketDepth(cls, symbol):
        return cls.client.get_order_book(symbol=symbol)

    @classmethod
    def currentPrice(cls, symbol):
        key = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        data = requests.get(key)
        data = data.json()
        return float(data['price'])
    
    @classmethod
    def buy(cls, symbol):
        order = cls.client.order_market_buy(
            symbol=symbol,
            quantity=cls.quantity
        )
        return order

    @classmethod
    def sell(cls, symbol):
        order = cls.client.order_market_sell(
            symbol=symbol,
            quantity=cls.quantity,
        )
        return order

    @classmethod
    def stop(cls, symbol):
        order = cls.client.order_market_sell(
            symbol = symbol,
            quantity=cls.quantity,
        )
        return order
