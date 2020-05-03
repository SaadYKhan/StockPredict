import matplotlib.pyplot as mpl
import numpy as np
import math as m
import scipy as sci
import pandas as pd
import pandas_datareader
import pandas_datareader.data as web
import datetime
from TaFunctions import TechAnalysis

#import psycopg2 as db
#quandl.ApiConfig.api_key = "wRAHe-_x2BPhM4E1KrE4"


TA = TechAnalysis()


from scipy import stats
'''
DB Connection to Postgres
#conn = db.connect(host="localhost", database="postgres", user="postgres", password="admin")
#cursor = conn.cursor()
#cursor.copy_from(spy, 'StockData', sep=',')
'''
start_date = datetime.datetime(2019,4,18)
end_date = datetime.datetime(2020,4,17)

df = web.DataReader('AAPL','yahoo',start_date,end_date)
#aapl = web.DataReader('AAPL','yahoo',start_date,end_date)
#tesla = web.DataReader('TSLA','yahoo',start_date,end_date)

df['SMA50'] = TA.MA(df, 50)
df['SMA200'] = TA.MA(df, 200)
df['SMA20'] = TA.MA(df,20)

df['EMA200'] = TA.EMA(df,200)
df['Macd'], df['Signal'], df['Crossover'] = TA.MACD(df,12,26)
#print(df['Macd'].iloc(0))


#spy['Close'].plot(label='SPY',figsize=(10,8),title='Close Prices')
#aapl['Close'].plot(label='AAPL')
'''
Calculate Daily and Cumulative Returns of Stock
'''
#aapl['Cumulative'] = aapl['Close']/aapl['Close'].iloc[0]
#spy['Cumulative'] = spy['Close']/spy['Close'].iloc[0]

#aapl['Daily Return'] = aapl['Close'].pct_change(1)
#spy['Daily Return'] = spy['Close'].pct_change(1)
#tesla['Daily Return'] = tesla['Close'].pct_change(1)

#spy['Cumulative'].plot(label='SPY',figsize=(10,8),title='Close Prices')
#aapl['Cumulative'].plot(label='Apple')

#beta,alpha,r_value,p_value,std_err = stats.linregress(tesla['Daily Return'].iloc[1:], spy['Daily Return'].iloc[1:])
#print(aapl.tail())

#mpl.scatter(aapl['Daily Return'], spy['Daily Return'],alpha=0.25)
#gm['Close'].plot(label='GM')
#mpl.show()

#df = web.DataReader('SPY','yahoo',start_date,end_date)

#df = pd.read_csv('AAPL.CSV',index_col='Date',parse_dates=True)
#df['Date'] = pd.to_datetime(df['Date'])
#df.set_index('Date',inplace=True)
#YearEndMean = df.resample(rule='A').mean()
#df['SMA50'] = df['Adj Close'].rolling(window=50).mean()
#df['SMA200']= df['Adj Close'].rolling(window=200).mean()

df['Upper'] = df['SMA20'] + 2 * df['Close'].rolling(window=20).std()
df['Lower'] = df['SMA20'] - 2 * df['Close'].rolling(window=20).std()
df['Mac26'] = df['Adj Close'].ewm(span=26, adjust=False).mean()
df['Mac12'] = df['Adj Close'].ewm(span=12, adjust=False).mean()
#df['Macd']=df['Mac12'] - df['Mac26']
#df['Signal']=  df['Macd'].ewm(span=9, adjust=False).mean()
#df['Crossover'] = df['Macd'] - df['Signal']


df['Close'].plot()
#df[['SMA50','Close']].plot()
#df[['Close', 'SMA50', 'SMA200']].plot(figsize=(16,8))
mpl.show()

#df.to_csv('AAPLCalculated.csv')
#df1 = df[df['Signal'] > df['Macd']]





#print(df1)


#buyPrice = df.iloc[1], "Adj Close"

#print(buyPrice)

#df[['Upper','Close','Lower', 'SMA50', 'SMA200']].plot(figsize=(10,8))
#df[['Close','SMA50', 'SMA200','Macd', 'Signal']].plot(figsize=(10,8))
#df[['Close','SMA50', 'SMA200','SMA1YR', 'SMA2YR','SMA3YR','SMA4YR']].plot(figsize=(10,8))
#mpl.show()
