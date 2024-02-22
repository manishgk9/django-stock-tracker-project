from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/stocks/', consumers.StockConsumer.as_asgi(), name='ws_stock_consumer'),
]
