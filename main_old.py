# Assignment: Custom API Based Website
"""
Build a custom website using an API that you find interesting.

Using what you have learnt about HTTP request and REST APIs, in today's project you will build a website that uses data from a public API.
For example, previously we create a rain alert app using a weather API. We also created an ISS tracker and looking into Bitcoin prices, all using a public API.
Today, you get to work on an API that you find interesting and build a service or website based on that API.

Here are some example APIs:
New York Subway Data
Elephant Data
Barcode Generator/Recognition
Stock Market Data
Harry Potter Data
Art Data
Dictionary API
ESPN Data
Food Facts API
Brewery Data
Spelling and Grammar Check API
Sound Effects API
Lord of the Rings API
"""
# TASKS
"""
After obtaining API Data,
1. (D) Populate website with relevant data
2.Add Flask Form for user to choose input (date/stock/# of entry)
    >> Multiple Flask forms on one page-- harder to implement (need to retrieve data values seperately)
3. (D) Plot graph in HTML (How to plot graph in HTML using python?)  
    >>Use matplotlib then insert img
    ### STONKS! Overview --- can use JS to have an interactive graph where users can check specific values of date/price
        GRAPH CAN BE VASTLY IMPROVED USING JAVASCRIPT(instead of static image)... BUT PROJECT DONE USING FLASK
        and stock market prices can be showed along with cursor selection
    https://www.w3schools.com/ai/ai_chartjs.asp -->Javascript

-(FIXED) Insert image with fixed dimension HTML
https://stackoverflow.com/questions/46730667/how-to-display-image-of-any-size-in-a-fixed-size-100x100-div
-(FIXED) Date: Slicing strings (not split)
-(FIXED) url_for not working for html image
-(FIXED) HOW TO ACCESS IMMUTABLE DICT? 
    https://stackoverflow.com/questions/24892035/how-can-i-get-the-named-parameters-from-a-url-using-flask
    https://werkzeug.palletsprojects.com/en/2.1.x/datastructures/#werkzeug.datastructures.MultiDict.get
-(FIXED) Flask HTML image not updating on refresh/IMAGE NOT UPDATING IN HTML AFTER PAGE REFRESH - How to force hard reload on HTML image using python?
 How to clear cache flask?
 Reload HTML image flask 
 >>>INTRODUCED SWITCH TO RELOAD HTML ELEMENT MANUALLY BASED ON CONDITIONAL-- Works only for 1st reload; subsequently will cache current image
 >>>ADDED FILE NAME FOR DIFFERENT STOCK NAMES TO IMAGE PATH
 
 flask form use button name as button value
 how to setup flaskform with click to submit value?
 how to setup flaskform with dynamic buttons
 
#IMPROVEMENTS: (Limited bcos of free API usage; dont want to incur charges)
----------------------------------------------------------------------------------------------
STONKS! Outlook can be rendered with dynamic data from API; then display bar according to 
% profit; if >10%-green; 10%<x<15% teal; etc
% risk; 
% values madeup arbitrarily

Stock Market Data
https://marketstack.com/quickstart
Website layout reference:
https://startbootstrap.com/theme/sb-admin-2
"""
import requests
import datetime
from flask import Flask, render_template, request, url_for, redirect
import pandas as pd
import matplotlib.pyplot as plt

MARKET_STACK_API_KEY = "2dd0348b20401fe647477669fda207f0"  # can store as environment variable for security but just leaving it here for convenience

# ALLOW USER TO CHOOSE INTERESTED PROPERTIES FROM FLASK FORM- then use request.get from form...
SYMBOLS = ""

date_x = []
monthly_average = 0
monthly_average_low = 0
stonks_reload = False
filename = ""
entry_count = 0
date_range = 0


def api_call_plot_graph(symbol, entry_count, date_range):
    global SYMBOLS, monthly_average, monthly_average_low, date_x, stonks_reload, filename
    # RETURNED API DATA --- RENDER TO WEBSITE & VOILA

    # SYMBOLS = "AAPL"
    # SYMBOLS = "MSFT"

    try:
        SYMBOLS = symbol
    except:
        SYMBOLS = "GOOGL"

    TODAY = datetime.datetime.now()
    TODAY = TODAY.strftime("%Y-%m-%d")
    if int(date_range) == 1:
        THAT_DAY = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month,
                                     datetime.datetime.now().day - date_range)
    elif int(datetime.datetime.now().day) - int(date_range) > 0:
        THAT_DAY = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month,
                                     datetime.datetime.now().day - date_range)
    elif int(datetime.datetime.now().day) - int(date_range) < 0:
        THAT_DAY = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month - 1,
                                     31 + (int(datetime.datetime.now().day) - int(date_range)))
    elif int(date_range) == 30:
        THAT_DAY = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month - 1,
                                     datetime.datetime.now().day)
    else:
        THAT_DAY = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month,
                                     datetime.datetime.now().day)
    THAT_DAY = THAT_DAY.strftime("%Y-%m-%d")
    print(TODAY)
    print(THAT_DAY)

    URL_ENDPOINT = "http://api.marketstack.com/v1/eod"
    parameters = {
        "access_key": MARKET_STACK_API_KEY,
        "symbols": SYMBOLS,
        "date_from": THAT_DAY,
        "date_to": TODAY,
        "limit": entry_count,  # "30",
    }
    # FREE - 100 REQUESTS/MTH (commented out to prevent further API calls)
    # response = requests.get(URL_ENDPOINT, params=parameters)
    # response.raise_for_status()
    # data = response.json()
    # print(data)
    API_DATA_AAPL = {'pagination': {'limit': 30, 'offset': 0, 'count': 18, 'total': 18},
                     'data':
                         [
                             {'open': 139.9, 'high': 141.91, 'low': 139.77, 'close': 141.66, 'volume': 89047400.0,
                              'adj_high': None,
                              'adj_low': None, 'adj_close': 141.66, 'adj_open': None, 'adj_volume': None,
                              'split_factor': 1.0,
                              'dividend': 0.0,
                              'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-06-24T00:00:00+0000'},
                             {'open': 136.82, 'high': 138.59, 'low': 135.63, 'close': 138.27, 'volume': 72330300.0,
                              'adj_high': None,
                              'adj_low': None, 'adj_close': 138.27, 'adj_open': None, 'adj_volume': None,
                              'split_factor': 1.0,
                              'dividend': 0.0,
                              'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-06-23T00:00:00+0000'},
                             {'open': 134.79, 'high': 137.755, 'low': 133.91, 'close': 135.35, 'volume': 73165480.0,
                              'adj_high': None,
                              'adj_low': None, 'adj_close': 135.35, 'adj_open': None, 'adj_volume': None,
                              'split_factor': 1.0,
                              'dividend': 0.0,
                              'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-06-22T00:00:00+0000'},
                             {'open': 133.42, 'high': 137.06, 'low': 133.32, 'close': 135.87, 'volume': 80785400.0,
                              'adj_high': None,
                              'adj_low': None, 'adj_close': 135.87, 'adj_open': None, 'adj_volume': None,
                              'split_factor': 1.0,
                              'dividend': 0.0,
                              'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-06-21T00:00:00+0000'},
                             {'open': 130.07, 'high': 133.08, 'low': 129.81, 'close': 131.56, 'volume': 134118500.0,
                              'adj_high': None,
                              'adj_low': None, 'adj_close': 131.56, 'adj_open': None, 'adj_volume': None,
                              'split_factor': 1.0,
                              'dividend': 0.0,
                              'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-06-17T00:00:00+0000'},
                             {'open': 132.08, 'high': 132.39, 'low': 129.07, 'close': 130.06, 'volume': 107961508.0,
                              'adj_high': None,
                              'adj_low': None, 'adj_close': 130.06, 'adj_open': None, 'adj_volume': None,
                              'split_factor': 1.0,
                              'dividend': 0.0,
                              'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-06-16T00:00:00+0000'},
                             {'open': 134.29, 'high': 137.34, 'low': 132.16, 'close': 135.43, 'volume': 91352700.0,
                              'adj_high': None,
                              'adj_low': None, 'adj_close': 135.43, 'adj_open': None, 'adj_volume': None,
                              'split_factor': 1.0,
                              'dividend': 0.0,
                              'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-06-15T00:00:00+0000'},
                             {'open': 133.13, 'high': 133.89, 'low': 131.48, 'close': 132.76, 'volume': 84545000.0,
                              'adj_high': None,
                              'adj_low': None, 'adj_close': 132.76, 'adj_open': None, 'adj_volume': None,
                              'split_factor': 1.0,
                              'dividend': 0.0,
                              'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-06-14T00:00:00+0000'},
                             {'open': 132.87, 'high': 135.2, 'low': 131.4401, 'close': 131.88, 'volume': 121893720.0,
                              'adj_high': None,
                              'adj_low': None, 'adj_close': 131.88, 'adj_open': None, 'adj_volume': None,
                              'split_factor': 1.0,
                              'dividend': 0.0,
                              'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-06-13T00:00:00+0000'},
                             {'open': 140.28, 'high': 140.76, 'low': 137.06, 'close': 137.13, 'volume': 91437900.0,
                              'adj_high': None,
                              'adj_low': None, 'adj_close': 137.13, 'adj_open': None, 'adj_volume': None,
                              'split_factor': 1.0,
                              'dividend': 0.0,
                              'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-06-10T00:00:00+0000'},
                             {'open': 147.08, 'high': 147.95, 'low': 142.53, 'close': 142.64, 'volume': 69367400.0,
                              'adj_high': None,
                              'adj_low': None, 'adj_close': 142.64, 'adj_open': None, 'adj_volume': None,
                              'split_factor': 1.0,
                              'dividend': 0.0,
                              'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-06-09T00:00:00+0000'},
                             {'open': 148.58, 'high': 149.87, 'low': 147.46, 'close': 147.96, 'volume': 53895900.0,
                              'adj_high': None,
                              'adj_low': None, 'adj_close': 147.96, 'adj_open': None, 'adj_volume': None,
                              'split_factor': 1.0,
                              'dividend': 0.0,
                              'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-06-08T00:00:00+0000'},
                             {'open': 144.35, 'high': 149.0, 'low': 144.1, 'close': 148.71, 'volume': 67713600.0,
                              'adj_high': None,
                              'adj_low': None, 'adj_close': 148.71, 'adj_open': None, 'adj_volume': None,
                              'split_factor': 1.0,
                              'dividend': 0.0,
                              'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-06-07T00:00:00+0000'},
                             {'open': 147.03, 'high': 148.5689, 'low': 144.9, 'close': 146.14, 'volume': 70931362.0,
                              'adj_high': None,
                              'adj_low': None, 'adj_close': 146.14, 'adj_open': None, 'adj_volume': None,
                              'split_factor': 1.0,
                              'dividend': 0.0,
                              'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-06-06T00:00:00+0000'},
                             {'open': 146.9, 'high': 147.97, 'low': 144.46, 'close': 145.38, 'volume': 88471400.0,
                              'adj_high': None,
                              'adj_low': None, 'adj_close': 145.38, 'adj_open': None, 'adj_volume': None,
                              'split_factor': 1.0,
                              'dividend': 0.0,
                              'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-06-03T00:00:00+0000'},
                             {'open': 147.83, 'high': 151.27, 'low': 146.86, 'close': 151.21, 'volume': 72232000.0,
                              'adj_high': None,
                              'adj_low': None, 'adj_close': 151.21, 'adj_open': None, 'adj_volume': None,
                              'split_factor': 1.0,
                              'dividend': 0.0,
                              'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-06-02T00:00:00+0000'},
                             {'open': 149.9, 'high': 151.74, 'low': 147.68, 'close': 148.71, 'volume': 74143400.0,
                              'adj_high': None,
                              'adj_low': None, 'adj_close': 148.71, 'adj_open': None, 'adj_volume': None,
                              'split_factor': 1.0,
                              'dividend': 0.0,
                              'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-06-01T00:00:00+0000'},
                             {'open': 149.07, 'high': 150.66, 'low': 146.84, 'close': 148.84, 'volume': 93971235.0,
                              'adj_high': None,
                              'adj_low': None, 'adj_close': 148.84, 'adj_open': None, 'adj_volume': None,
                              'split_factor': 1.0,
                              'dividend': 0.0,
                              'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2022-05-31T00:00:00+0000'}
                         ]}
    API_DATA_MSFT = {'pagination': {'limit': 30, 'offset': 0, 'count': 18, 'total': 18}, 'data': [
        {'open': 261.81, 'high': 267.98, 'low': 261.72, 'close': 267.7, 'volume': 33900700.0, 'adj_high': None,
         'adj_low': None, 'adj_close': 267.7, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
         'dividend': 0.0,
         'symbol': 'MSFT', 'exchange': 'XNAS', 'date': '2022-06-24T00:00:00+0000'},
        {'open': 255.57, 'high': 259.37, 'low': 253.63, 'close': 258.86, 'volume': 25844400.0, 'adj_high': None,
         'adj_low': None, 'adj_close': 258.86, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
         'dividend': 0.0,
         'symbol': 'MSFT', 'exchange': 'XNAS', 'date': '2022-06-23T00:00:00+0000'},
        {'open': 251.89, 'high': 257.17, 'low': 250.38, 'close': 253.13, 'volume': 25931728.0, 'adj_high': None,
         'adj_low': None, 'adj_close': 253.13, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
         'dividend': 0.0,
         'symbol': 'MSFT', 'exchange': 'XNAS', 'date': '2022-06-22T00:00:00+0000'},
        {'open': 250.26, 'high': 254.75, 'low': 249.51, 'close': 253.74, 'volume': 29913000.0, 'adj_high': None,
         'adj_low': None, 'adj_close': 253.74, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
         'dividend': 0.0,
         'symbol': 'MSFT', 'exchange': 'XNAS', 'date': '2022-06-21T00:00:00+0000'},
        {'open': 244.7, 'high': 250.5, 'low': 244.03, 'close': 247.65, 'volume': 42800400.0, 'adj_high': None,
         'adj_low': None, 'adj_close': 247.65, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
         'dividend': 0.0,
         'symbol': 'MSFT', 'exchange': 'XNAS', 'date': '2022-06-17T00:00:00+0000'},
        {'open': 245.98, 'high': 247.4174, 'low': 243.03, 'close': 244.97, 'volume': 31118528.0, 'adj_high': None,
         'adj_low': None, 'adj_close': 244.97, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
         'dividend': 0.0,
         'symbol': 'MSFT', 'exchange': 'XNAS', 'date': '2022-06-16T00:00:00+0000'},
        {'open': 248.31, 'high': 255.3, 'low': 246.42, 'close': 251.76, 'volume': 33073500.0, 'adj_high': None,
         'adj_low': None, 'adj_close': 251.76, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
         'dividend': 0.0,
         'symbol': 'MSFT', 'exchange': 'XNAS', 'date': '2022-06-15T00:00:00+0000'},
        {'open': 243.86, 'high': 245.74, 'low': 241.51, 'close': 244.49, 'volume': 28616700.0, 'adj_high': None,
         'adj_low': None, 'adj_close': 244.49, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
         'dividend': 0.0,
         'symbol': 'MSFT', 'exchange': 'XNAS', 'date': '2022-06-14T00:00:00+0000'},
        {'open': 245.11, 'high': 249.02, 'low': 241.53, 'close': 242.26, 'volume': 46135788.0, 'adj_high': None,
         'adj_low': None, 'adj_close': 242.26, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
         'dividend': 0.0,
         'symbol': 'MSFT', 'exchange': 'XNAS', 'date': '2022-06-13T00:00:00+0000'},
        {'open': 260.58, 'high': 260.58, 'low': 252.53, 'close': 252.99, 'volume': 31422800.0, 'adj_high': None,
         'adj_low': None, 'adj_close': 252.99, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
         'dividend': 0.0,
         'symbol': 'MSFT', 'exchange': 'XNAS', 'date': '2022-06-10T00:00:00+0000'},
        {'open': 267.78, 'high': 272.71, 'low': 264.63, 'close': 264.79, 'volume': 26425500.0, 'adj_high': None,
         'adj_low': None, 'adj_close': 264.79, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
         'dividend': 0.0,
         'symbol': 'MSFT', 'exchange': 'XNAS', 'date': '2022-06-09T00:00:00+0000'},
        {'open': 271.71, 'high': 273.0, 'low': 269.61, 'close': 270.41, 'volume': 17369700.0, 'adj_high': None,
         'adj_low': None, 'adj_close': 270.41, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
         'dividend': 0.0,
         'symbol': 'MSFT', 'exchange': 'XNAS', 'date': '2022-06-08T00:00:00+0000'},
        {'open': 266.64, 'high': 273.13, 'low': 265.94, 'close': 272.5, 'volume': 22838600.0, 'adj_high': None,
         'adj_low': None, 'adj_close': 272.5, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
         'dividend': 0.0,
         'symbol': 'MSFT', 'exchange': 'XNAS', 'date': '2022-06-07T00:00:00+0000'},
        {'open': 272.06, 'high': 274.17, 'low': 267.245, 'close': 268.75, 'volume': 22400342.0, 'adj_high': None,
         'adj_low': None, 'adj_close': 268.75, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
         'dividend': 0.0,
         'symbol': 'MSFT', 'exchange': 'XNAS', 'date': '2022-06-06T00:00:00+0000'},
        {'open': 270.31, 'high': 273.45, 'low': 268.41, 'close': 270.02, 'volume': 28048000.0, 'adj_high': None,
         'adj_low': None, 'adj_close': 270.02, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
         'dividend': 0.0,
         'symbol': 'MSFT', 'exchange': 'XNAS', 'date': '2022-06-03T00:00:00+0000'},
        {'open': 264.45, 'high': 274.65, 'low': 261.6, 'close': 274.58, 'volume': 43976900.0, 'adj_high': None,
         'adj_low': None, 'adj_close': 274.58, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
         'dividend': 0.0,
         'symbol': 'MSFT', 'exchange': 'XNAS', 'date': '2022-06-02T00:00:00+0000'},
        {'open': 275.2, 'high': 277.69, 'low': 270.04, 'close': 272.42, 'volume': 25273400.0, 'adj_high': None,
         'adj_low': None, 'adj_close': 272.42, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
         'dividend': 0.0,
         'symbol': 'MSFT', 'exchange': 'XNAS', 'date': '2022-06-01T00:00:00+0000'},
        {'open': 272.53, 'high': 274.77, 'low': 268.94, 'close': 271.87, 'volume': 37589536.0, 'adj_high': None,
         'adj_low': None, 'adj_close': 271.87, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
         'dividend': 0.0,
         'symbol': 'MSFT', 'exchange': 'XNAS', 'date': '2022-05-31T00:00:00+0000'}]}
    API_DATA_GOOGL = {'pagination': {'limit': 30, 'offset': 0, 'count': 19, 'total': 19}, 'data': [
        {'open': 2365.46, 'high': 2371.5901, 'low': 2303.5901, 'close': 2316.6699, 'volume': 1819800.0,
         'adj_high': None, 'adj_low': None, 'adj_close': 2316.6699, 'adj_open': None, 'adj_volume': None,
         'split_factor': 1.0, 'dividend': 0.0, 'symbol': 'GOOGL', 'exchange': 'XNAS',
         'date': '2022-06-27T00:00:00+0000'},
        {'open': 2259.8999, 'high': 2361.5801, 'low': 2259.05, 'close': 2359.5, 'volume': 2054600.0, 'adj_high': None,
         'adj_low': None, 'adj_close': 2359.5, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
         'dividend': 0.0, 'symbol': 'GOOGL', 'exchange': 'XNAS', 'date': '2022-06-24T00:00:00+0000'},
        {'open': 2244.6299, 'high': 2254.8501, 'low': 2210.01, 'close': 2244.8401, 'volume': 1415600.0,
         'adj_high': None, 'adj_low': None, 'adj_close': 2244.8401, 'adj_open': None, 'adj_volume': None,
         'split_factor': 1.0, 'dividend': 0.0, 'symbol': 'GOOGL', 'exchange': 'XNAS',
         'date': '2022-06-23T00:00:00+0000'},
        {'open': 2211.13, 'high': 2266.93, 'low': 2207.6475, 'close': 2229.75, 'volume': 1537149.0, 'adj_high': None,
         'adj_low': None, 'adj_close': 2229.75, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
         'dividend': 0.0, 'symbol': 'GOOGL', 'exchange': 'XNAS', 'date': '2022-06-22T00:00:00+0000'},
        {'open': 2178.5901, 'high': 2249.7849, 'low': 2172.3101, 'close': 2230.8799, 'volume': 1967850.0,
         'adj_high': None, 'adj_low': None, 'adj_close': 2230.8799, 'adj_open': None, 'adj_volume': None,
         'split_factor': 1.0, 'dividend': 0.0, 'symbol': 'GOOGL', 'exchange': 'XNAS',
         'date': '2022-06-21T00:00:00+0000'},
        {'open': 2120.6699, 'high': 2173.99, 'low': 2100.9199, 'close': 2142.8701, 'volume': 2555300.0,
         'adj_high': None, 'adj_low': None, 'adj_close': 2142.8701, 'adj_open': None, 'adj_volume': None,
         'split_factor': 1.0, 'dividend': 0.0, 'symbol': 'GOOGL', 'exchange': 'XNAS',
         'date': '2022-06-17T00:00:00+0000'},
        {'open': 2144.4199, 'high': 2172.97, 'low': 2103.6577, 'close': 2120.6699, 'volume': 2442044.0,
         'adj_high': None, 'adj_low': None, 'adj_close': 2120.6699, 'adj_open': None, 'adj_volume': None,
         'split_factor': 1.0, 'dividend': 0.0, 'symbol': 'GOOGL', 'exchange': 'XNAS',
         'date': '2022-06-16T00:00:00+0000'},
        {'open': 2170.8999, 'high': 2228.47, 'low': 2153.3899, 'close': 2195.29, 'volume': 1978500.0, 'adj_high': None,
         'adj_low': None, 'adj_close': 2195.29, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
         'dividend': 0.0, 'symbol': 'GOOGL', 'exchange': 'XNAS', 'date': '2022-06-15T00:00:00+0000'},
        {'open': 2130.7, 'high': 2158.49, 'low': 2116.0, 'close': 2134.3101, 'volume': 1681900.0, 'adj_high': None,
         'adj_low': None, 'adj_close': 2134.3101, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
         'dividend': 0.0, 'symbol': 'GOOGL', 'exchange': 'XNAS', 'date': '2022-06-14T00:00:00+0000'},
        {'open': 2135.73, 'high': 2174.9399, 'low': 2122.3835, 'close': 2127.8501, 'volume': 2247986.0,
         'adj_high': None, 'adj_low': None, 'adj_close': 2127.8501, 'adj_open': None, 'adj_volume': None,
         'split_factor': 1.0, 'dividend': 0.0, 'symbol': 'GOOGL', 'exchange': 'XNAS',
         'date': '2022-06-13T00:00:00+0000'},
        {'open': 2248.8999, 'high': 2265.5801, 'low': 2207.3201, 'close': 2223.23, 'volume': 2072600.0,
         'adj_high': None, 'adj_low': None, 'adj_close': 2223.23, 'adj_open': None, 'adj_volume': None,
         'split_factor': 1.0, 'dividend': 0.0, 'symbol': 'GOOGL', 'exchange': 'XNAS',
         'date': '2022-06-10T00:00:00+0000'},
        {'open': 2326.55, 'high': 2365.9799, 'low': 2295.52, 'close': 2296.71, 'volume': 1289898.0, 'adj_high': None,
         'adj_low': None, 'adj_close': 2296.71, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
         'dividend': 0.0, 'symbol': 'GOOGL', 'exchange': 'XNAS', 'date': '2022-06-09T00:00:00+0000'},
        {'open': 2335.23, 'high': 2371.4099, 'low': 2332.0, 'close': 2343.8799, 'volume': 1304800.0, 'adj_high': None,
         'adj_low': None, 'adj_close': 2343.8799, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
         'dividend': 0.0, 'symbol': 'GOOGL', 'exchange': 'XNAS', 'date': '2022-06-08T00:00:00+0000'},
        {'open': 2309.6101, 'high': 2353.55, 'low': 2301.04, 'close': 2342.99, 'volume': 1486056.0, 'adj_high': None,
         'adj_low': None, 'adj_close': 2342.99, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
         'dividend': 0.0, 'symbol': 'GOOGL', 'exchange': 'XNAS', 'date': '2022-06-07T00:00:00+0000'},
        {'open': 2334.0901, 'high': 2386.9399, 'low': 2323.28, 'close': 2336.4099, 'volume': 1601028.0,
         'adj_high': None, 'adj_low': None, 'adj_close': 2336.4099, 'adj_open': None, 'adj_volume': None,
         'split_factor': 1.0, 'dividend': 0.0, 'symbol': 'GOOGL', 'exchange': 'XNAS',
         'date': '2022-06-06T00:00:00+0000'},
        {'open': 2321.25, 'high': 2326.4299, 'low': 2270.3701, 'close': 2290.8201, 'volume': 1305900.0,
         'adj_high': None, 'adj_low': None, 'adj_close': 2290.8201, 'adj_open': None, 'adj_volume': None,
         'split_factor': 1.0, 'dividend': 0.0, 'symbol': 'GOOGL', 'exchange': 'XNAS',
         'date': '2022-06-03T00:00:00+0000'},
        {'open': 2280.0, 'high': 2357.99, 'low': 2258.9299, 'close': 2352.45, 'volume': 1895600.0, 'adj_high': None,
         'adj_low': None, 'adj_close': 2352.45, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
         'dividend': 0.0, 'symbol': 'GOOGL', 'exchange': 'XNAS', 'date': '2022-06-02T00:00:00+0000'},
        {'open': 2297.1001, 'high': 2342.03, 'low': 2265.0, 'close': 2277.8401, 'volume': 1826900.0, 'adj_high': None,
         'adj_low': None, 'adj_close': 2277.8401, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
         'dividend': 0.0, 'symbol': 'GOOGL', 'exchange': 'XNAS', 'date': '2022-06-01T00:00:00+0000'},
        {'open': 2254.9299, 'high': 2314.7, 'low': 2241.6799, 'close': 2275.24, 'volume': 2179830.0, 'adj_high': None,
         'adj_low': None, 'adj_close': 2275.24, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0,
         'dividend': 0.0, 'symbol': 'GOOGL', 'exchange': 'XNAS', 'date': '2022-05-31T00:00:00+0000'}]}
    date_x = []
    daily_average = []
    high_y = []
    low_y = []
    open_y = []
    close_y = []

    # NEED TO REORDER DATA--- Returned data is in descending order (latest date first)
    #                     --- Want earliest date first
    # how to flip list indexes?
    # for loop list from last index
    # list iteration in reverse order python
    # https://stackoverflow.com/questions/529424/traverse-a-list-in-reverse-order-in-python

    if SYMBOLS == "AAPL":
        stock_list = API_DATA_AAPL["data"]
    elif SYMBOLS == "MSFT":
        stock_list = API_DATA_MSFT["data"]
    else:
        # SHOULD BE API CALL - BUT DEFAULT TO GOOGL TO PREVENT UNNECCESSARY API CALLS
        # stock_list = data["data"]
        stock_list = API_DATA_GOOGL["data"]

    # API CALL
    # for item in reversed(data["data"]): #API CALL
    # LOCAL FILE API CALL
    # for item in reversed(API_DATA_AAPL["data"]):
    # for item in reversed(API_DATA_MSFT["data"]):
    for item in reversed(stock_list):
        daily_average_oc = (item["open"] + item["close"]) / 2
        daily_average.append(daily_average_oc)
        high_y.append(item["high"])
        low_y.append(item["low"])
        open_y.append(item["open"])
        close_y.append(item["close"])
        date_x.append(item["date"][0:10])

    # RESTRICT # OF ENTRIES (SINCE CANT DO DURING API CALL)
    print(f"entry_count before graph plot: {entry_count}")
    # entry_count = 5
    daily_average = daily_average[0:entry_count - 1]
    high_y = high_y[0:entry_count - 1]
    low_y = low_y[0:entry_count - 1]
    open_y = open_y[0:entry_count - 1]
    close_y = close_y[0:entry_count - 1]
    date_x = date_x[0:entry_count - 1]

    monthly_total = 0
    for item in daily_average:
        monthly_total += item
    monthly_average = monthly_total / len(daily_average)
    print(monthly_average)

    monthly_total_low = 0
    for item in low_y:
        monthly_total_low += item
    monthly_average_low = monthly_total_low / len(low_y)

    print("High", high_y)
    print("Low", low_y)
    print("Open", open_y)
    print("Close", close_y)
    print("Average", daily_average)
    print("Date", date_x)
    print(len(date_x))
    print(f"{len(API_DATA_AAPL['data'])}/30 days returned")

    # matplotlib - How to prevent overlapping axis?
    # label graph matplotlib- https://www.w3schools.com/python/matplotlib_labels.asp
    # label cut off from display
    # label individual graph matplotlib
    # matplotlib - set minimum canvas size? https://stackoverflow.com/questions/6774086/how-to-adjust-padding-with-cutoff-or-overlapping-labels
    fig, ax = plt.subplots()
    # plt.tight_layout()
    font = {'family': 'courier', 'color': 'darkred', 'size': 25}
    font_axis = {'family': 'courier', 'color': 'darkred', 'size': 15}
    # set x,y label position matplotlib
    ax.set_xlabel("Date", fontdict=font_axis, loc="left")
    ax.set_ylabel("$$$", fontdict=font_axis)
    ax.plot(date_x, daily_average, 'b', label="Daily Average")
    ax.hlines(xmin=0, xmax=len(date_x), y=monthly_average, color='#42f5e6', label="Monthly Average")
    ax.plot(date_x, open_y, 'y', label="Open")
    ax.plot(date_x, close_y, '0.8', label="Close")

    # Plot high/low as box chart,plot/floating column/? (top and bottom line indicator)
    # https://developers.google.com/chart/image/docs/gallery/chart_gall?csw=1
    ax.plot(date_x, high_y, 'g', label="High")
    ax.plot(date_x, low_y, 'r', label="Low")

    for i in range(len(date_x)):
        data = [high_y[i], low_y[i]]
        box_i = ax.boxplot(data, positions=[i])

    # https://stackoverflow.com/questions/11373610/save-matplotlib-file-to-a-directory
    ax.set_title(f'{SYMBOLS} STONKS!???', fontdict=font)
    ax.set_xticklabels(date_x)
    plt.setp(ax.get_xticklabels(), rotation=25, horizontalalignment='right')
    plt.legend(loc='upper right')
    print(f"stonks_reload : {stonks_reload}")
    if stonks_reload == False:
        fig.savefig('static/img/stonks.png', bbox_inches='tight')
        filename = f'img/stonks.png'
    elif stonks_reload == True:
        fig.savefig(f'static/img/stonks_{SYMBOLS}_{entry_count}.png', bbox_inches='tight')
        filename = f'img/stonks_{SYMBOLS}_{entry_count}.png'
        # stonks_reload = False
        print(f"stonks_reload set to: {stonks_reload}")

    # s = pd.Series([1, 2, 3, 4])
    # fig, ax = plt.subplots()
    # s.plot.bar()
    # fig.savefig('my_plot.png')


# from flask_caching import Cache
# cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
app = Flask(__name__)


# app.config["CACHE_TYPE"] = "null"


@app.route('/', methods=["GET", "POST"])
def home():
    global monthly_average, monthly_average_low, SYMBOLS, date_x, filename
    # cache.init_app(app)
    # cache.clear()
    date_range = request.args.get('date_range')
    print(f"date_range: {date_range}")
    entry_count = request.args.get('entry_count')
    print(entry_count)

    print(f"SYMBOLS-home-previous: {SYMBOLS}")
    # DON'T RESET STOCK NAME IF STOCK NAME NOT ENTERED IN SEARCH BAR
    if request.args.get('symbol', type=str) != None:
        SYMBOLS = request.args.get('symbol', type=str)
    try:
        if entry_count == None and date_range == None:
            api_call_plot_graph(SYMBOLS, 20, 30)
        elif entry_count == None:
            api_call_plot_graph(SYMBOLS, 20, int(date_range))
        elif date_range == None:
            api_call_plot_graph(SYMBOLS, int(entry_count), 30)
        else:
            api_call_plot_graph(SYMBOLS, int(entry_count), int(date_range))
        filename = filename
    except TypeError:
        api_call_plot_graph("GOOGL", 30, 30)
        filename = filename

    # cache.init_app(app)
    # cache.clear()
    print(f"stonks_reload : {stonks_reload}")
    print(f"SYMBOLS-home: {SYMBOLS}")

    date = date_x[0][0:7]
    date_end = date_x[len(date_x) - 1][0:7]
    monthly_average = round(monthly_average, 3)
    potential_profits = round((monthly_average - monthly_average_low), 3)
    INV_AMOUNT = 10000
    stocks_bought = INV_AMOUNT / monthly_average
    # https://www.investopedia.com/articles/stocks/11/calculating-risk-reward.asp
    # Somehow the risk and returns/potential_profits is the same %...
    risk = round((((potential_profits * stocks_bought) / INV_AMOUNT) * 100), 2)

    returns_average = round(((potential_profits / monthly_average) * 100), 2)

    return render_template("index.html", date=date, date_end=date_end, symbols=SYMBOLS,
                           risk=risk, monthly_average=monthly_average, potential_profits=potential_profits,
                           returns_average=returns_average, stonks_reload=stonks_reload, filename=filename)


@app.route('/symbol', methods=["POST"])
def receive_data():
    global SYMBOLS, stonks_reload
    print("receive_data()")

    SYMBOLS = request.form["symbols"]
    print(f"SYMBOLS-try: {SYMBOLS}")
    stonks_reload = True
    print(f"stonks_reload set to: {stonks_reload}")

    return redirect(url_for("home", symbol=SYMBOLS))


@app.route('/date/<int:duration>', methods=["POST"])
def receive_date(duration):
    global date_range
    date_range = int(duration)
    return redirect(url_for("home", date_range=date_range))


@app.route('/entry/<int:ecount>', methods=["POST"])
def receive_entry(ecount):
    global entry_count
    entry_count = int(ecount)
    print(f"entry_count: {entry_count}")
    return redirect(url_for("home", entry_count=entry_count))


@app.route('/send_all_form_entries', methods=["POST"])
def send_all():
    global entry_count, date_range, SYMBOLS
    SYMBOLS = SYMBOLS
    entry_count = 3
    date_range = 30
    return redirect(url_for("home", entry_count=entry_count, symbol=SYMBOLS, date_range=date_range))


if __name__ == "__main__":
    app.run(debug=True)
