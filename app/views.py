from django.shortcuts import render
import yfinance as yf
# Create your views here.


def stockPiker(request):
    stockpicker = ["ADANIPORTS.NS", "ASIANPAINT.NS", "AXISBANK.NS", "BAJAJ-AUTO.NS", "BAJFINANCE.NS", "BAJAJFINSV.NS", "BHARTIARTL.NS", "BRITANNIA.NS", "CIPLA.NS", "COALINDIA.NS", "DIVISLAB.NS", "DRREDDY.NS", "EICHERMOT.NS", "GRASIM.NS", "HCLTECH.NS", "HDFC.NS", "HDFCBANK.NS", "HEROMOTOCO.NS", "HINDALCO.NS", "HINDUNILVR.NS", "ICICIBANK.NS", "IOC.NS", "INDUSINDBK.NS",
                   "INFY.NS", "ITC.NS", "JSWSTEEL.NS", "KOTAKBANK.NS", "LT.NS", "M&M.NS", "MARUTI.NS", "NTPC.NS", "NESTLEIND.NS", "ONGC.NS", "POWERGRID.NS", "RELIANCE.NS", "SHREECEM.NS", "SBIN.NS", "SBILIFE.NS", "SUNPHARMA.NS", "TCS.NS", "TATACONSUM.NS", "TATAMOTORS.NS", "TATASTEEL.NS", "TECHM.NS", "TITAN.NS", "ULTRACEMCO.NS", "UNITDSPR.NS", "WIPRO.NS", "ZEEL.NS"]
    return render(request, 'stockPicker.html', {'stockpicker': stockpicker})


def get_stock_data(symbol):
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


def stockTracker(request):
    data = {}
    if request.method == 'POST':
        inp_list = request.POST.getlist('stockpicker')
        try:
            for inp in inp_list:
                stock_data = get_stock_data(inp)
                data[stock_data['symbol']] = stock_data
            print(data)
        except Exception as e:
            print('exception found:', e)

    return render(request, 'stockTracker.html', {'data': data})
