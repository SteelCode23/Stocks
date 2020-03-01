from _metrics import RSquared
from _stocks import *
from _indicators import indicators
from _config import start, end

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
	plt.show()
Plots()
Correlations()