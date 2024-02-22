# stock_tracker/stockapp/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
import yfinance as yf
import time
import asyncio


class StockConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        symbol = text_data_json['symbol']
        while True:
            stock_data = self.get_stock_data(symbol)
            await self.send(text_data=json.dumps(stock_data))
            await asyncio.sleep(2)

    def get_stock_data(self, symbol):
        stock = yf.Ticker(symbol)
        stock_info = stock.info

        data = {
            'symbol': stock_info.get('symbol', ''),
            'name': stock_info.get('longName', ''),
            'price': stock_info.get('lastPrice', ''),
            'change': stock_info.get('regularMarketChange', ''),
            'percent_change': stock_info.get('regularMarketChangePercent', ''),
            'market_cap': stock_info.get('marketCap', ''),
            'open': stock_info.get('regularMarketOpen', ''),
            'previous_close': stock_info.get('regularMarketPreviousClose', ''),
            'bid': stock_info.get('bid', ''),
            'ask': stock_info.get('ask', ''),
            'day_range': f"{stock_info.get('dayLow', '')} - {stock_info.get('dayHigh', '')}",
            'year_range': f"{stock_info.get('fiftyTwoWeekLow', '')} - {stock_info.get('fiftyTwoWeekHigh', '')}",
        }
        return data
