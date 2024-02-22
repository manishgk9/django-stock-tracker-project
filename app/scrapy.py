import yfinance as yf
stockpicker = ["ADANIPORTS.NS", "ASIANPAINT.NS", "AXISBANK.NS", "BAJAJ-AUTO.NS", "BAJFINANCE.NS", "BAJAJFINSV.NS", "BHARTIARTL.NS", "BRITANNIA.NS", "CIPLA.NS", "COALINDIA.NS", "DIVISLAB.NS", "DRREDDY.NS", "EICHERMOT.NS", "GRASIM.NS", "HCLTECH.NS", "HDFC.NS", "HDFCBANK.NS", "HEROMOTOCO.NS", "HINDALCO.NS", "HINDUNILVR.NS", "ICICIBANK.NS", "IOC.NS", "INDUSINDBK.NS",
               "INFY.NS", "ITC.NS", "JSWSTEEL.NS", "KOTAKBANK.NS", "LT.NS", "M&M.NS", "MARUTI.NS", "NTPC.NS", "NESTLEIND.NS", "ONGC.NS", "POWERGRID.NS", "RELIANCE.NS", "SHREECEM.NS", "SBIN.NS", "SBILIFE.NS", "SUNPHARMA.NS", "TCS.NS", "TATACONSUM.NS", "TATAMOTORS.NS", "TATASTEEL.NS", "TECHM.NS", "TITAN.NS", "ULTRACEMCO.NS", "UNITDSPR.NS", "WIPRO.NS", "ZEEL.NS"]


def stockTracker(data):
    stock = yf.Ticker(data)
    stock_info = stock.info
    data = {
        'symbol': stock_info.get('symbol', ''),
        'name': stock_info.get('longName', ''),
        'price': stock_info.get('price', ''),
        'change': stock_info.get('regularMarketChange', ''),
        # 'volume': stock.history('id'),
        'market_cap': stock_info.get('marketCap', ''),
        'open': stock_info.get('regularMarketOpen', ''),
        'previous_close': stock_info.get('regularMarketPreviousClose', ''),
        'bid': stock_info.get('bid', ''),
        'ask': stock_info.get('ask', ''),
        'day_range': f"{stock_info.get('dayLow', '')} - {stock_info.get('dayHigh', '')}",
        'year_range': f"{stock_info.get('fiftyTwoWeekLow', '')} - {stock_info.get('fiftyTwoWeekHigh', '')}",
    }
    # print(data)
    # print(stock.history('id')['volume'])
    # print(stock_info)


stockTracker('RELIANCE.NS')
