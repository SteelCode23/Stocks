

from _metrics import RSquared, DaysReturns,QuartersReturns,YearsReturns,TenYearsReturns
from _stocks import *
from _indicators import indicators
from _config import start, end
from _sp import _stocks
from datetime import datetime
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from pandas_datareader import wb
from datetime import datetime
import pandas as pd
_all = [portfolio,payments,retailers,FAANG,big_banks,speculative,big_three,energy]

#Correlation with indicators
def Correlations():
	for stock in _all:
	    for ticker in stock:
	        try:
	            print(ticker, RSquared(ticker))
	        except Exception as e:
	            print(e)

def SimpleCalc(ticker):
	return (ticker, RSquared(ticker))

#Plots
def Plots():
	import pandas_datareader.data as web
	import matplotlib.pyplot as plt

	from pandas_datareader import data
	f = plt.figure(figsize=(20,10))
	plt.title("S&P 500")
	start='2008-01-01'
	end='2020-01-01'
	inflation = web.DataReader(['CPILFESL'], 'fred', start, end)
	ax = plt.subplot(2, 3, 1)
	plt.title('Inflation')
	inflation.pct_change().plot(ax=f.gca())
	plt.subplot(2, 3, 2)
	plt.title('S&P Return')
	SP = data.DataReader("^GSPC",start = start, end = end,data_source='yahoo')
	#SP['Adj Close'].resample(rule='Y').mean().pct_change().plot(ax=f.gca())
	SP['Adj Close'].resample(rule='M').mean().pct_change().plot(ax=f.gca())
	interest_rate = web.DataReader(['FEDFUNDS'], 'fred', start, end)
	ax = plt.subplot(2, 3, 3)
	plt.title('Interest Rates')
	interest_rate.pct_change().plot(ax=f.gca())
	gdp = web.DataReader(['GDP'], 'fred', start, end)
	ax = plt.subplot(2, 3, 4)
	plt.title('GDP')
	gdp.pct_change().plot(ax=f.gca())
	gdp = web.DataReader(['POPTOTUSA647NWDB'], 'fred', start, end)
	ax = plt.subplot(2, 3, 4)
	plt.title('Population')
	gdp.pct_change().plot(ax=f.gca())	
	plt.show()
#Plots()
#Correlations()
# _score = {}
# #_stocks = ['MSFT','AAPL']
# _err = []
# for stock in _stocks:
# 	try:
# 		output = YearsReturns(stock)
# 		_score[output[0]] = output[1]
# 	except Exception as e:
# 		_err.append(e)

# _try_ = pd.DataFrame.from_dict(_score, orient='index')
# _try_.to_excel('YearsReturns.xlsx')

_score = {}
#_stocks = ['MSFT','AAPL']
_err = []
for stock in _stocks:
	try:
		output = YearsReturns(stock)
		_score[output[0]] = output[1]
	except Exception as e:
		_err.append(e)

_try_ = pd.DataFrame.from_dict(_score, orient='index')
_try_.to_excel('YearsReturns.xlsx')
print(_err)


_score = {}
#_stocks = ['MSFT','AAPL']
_err = []
for stock in _stocks:
	try:
		output = TenYearsReturns(stock)
		_score[output[0]] = output[1]
	except Exception as e:
		_err.append(e)

_try_ = pd.DataFrame.from_dict(_score, orient='index')
_try_.to_excel('TenYearsReturns.xlsx')
print(_err)

