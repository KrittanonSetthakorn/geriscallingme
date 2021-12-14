import mplfinance as mpf
import pandas as pd
import requests
import tkinter as tk
from datetime import datetime 

def get_candles(start_time, base_currency, compare_currency, interval):
    url = f'https://dev-api.shrimpy.io/v1/exchanges/binance/candles'
    payload = {'interval': interval, 'baseTradingSymbol': base_currency, 'quoteTradingSymbol': compare_currency, 'startTime': start_time}
    response = requests.get(url, params = payload)
    data = response.json()

    open_price = []
    close_price = []
    high_price = []
    low_price = []
    time_price = []

    for candle in data:
        open_price.append(float(candle['open'])) 
        high_price.append(float(candle['high']))
        low_price.append(float(candle['low']))
        close_price.append(float(candle['close']))
        time_price.append(candle['time'])

    raw_data = {'Date': pd.DatetimeIndex(time_price),
                'Open': open_price,
                'High': high_price,
                'Low': low_price,
                'Close': close_price}
    
    df = pd.DataFrame(raw_data).set_index('Date')

    print(df)

    mpf.plot(df, type = 'candle', style = 'charles', title =  base_currency, ylabel = f'Price in {compare_currency}')
    mpf.show()

    return df

def checkBitcoin():
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY.EUR"
    response = requests.get(url).json()
    price = response["USD"] 
    time = datetime.now().strftime("%H:%M:%S")

    labelPrice.config(text = str(price) + "$")
    labelTime.config(text = "Updated at: " + time)

    canvas.after(1000, checkBitcoin)


canvas = tk.Tk()
canvas.geometry("400x500")
canvas.title("Bitcoin price checker")

f1 = ("poppins", 24 ,"bold")
f2 = ("poppins", 22 ,"bold")
f3 = ("poppins", 18 ,"normal")

label = tk.Label(canvas, text = "Bitcoin Price" ,font = f1)
label.pack(pady = 20)

labelPrice = tk.Label(canvas, font = f2)
labelPrice.pack(pady = 20)

labelTime = tk.Label(canvas, font = f3)
labelTime.pack(pady = 20)

checkBitcoin()
canvas.mainloop()
get_candles(start_time = '2021-11-25', base_currency = 'BTC', compare_currency = 'EUR', interval = '1H' )
