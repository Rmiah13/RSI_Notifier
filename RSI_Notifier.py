#!/usr/bin/env python3
# Create a tool that notifies me whenever one of my stocks has a low RSI (Relative Strength Index)
import pandas as pd
from alpha_vantage.techindicators import TechIndicators
import os, time, schedule
import numpy as np
from matplotlib import style
style.use('ggplot')

api_key = 'ENTER API KEY HERE' #Get your API Key here - https://www.alphavantage.co

def RSI_Buy():
    #Pull The Data
    print("Please provide a list of tickers you want an RSI for separated by commas and no spaces, e.g. TSLA,MSFT,AAPL")
    user_input = input()
    a_list = list(map(str,user_input.split(',')))
    print('Wait 11 seconds for each stock as I can only make 5 requests a minute due to using a free API...')
    for i in a_list:
        ti = TechIndicators(key=api_key, output_format='pandas')
        time.sleep(11)
        data, meta_data = ti.get_rsi(symbol=i,interval = 'daily', time_period=120, series_type='close')

        if not os.path.exists('RSI_file.csv'):
            df = data.tail(1)
            df.to_csv('RSI_file.csv')
        else:
            df = data.tail(1)
            df.to_csv('RSI_file.csv')

        df.reset_index(inplace=True)
        df.set_index('RSI',inplace=True)

        RSI = df.index[0]
        

    #Determine whether RSI is below 30 or above 70

        if RSI < 30:
            print(i,' BUY - ',RSI)
        elif RSI > 70:
            print(i,' SELL - ',RSI)
        else:
            print(i,' HOLD - ',RSI)

RSI_Buy()
