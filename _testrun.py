

from _metrics import * 
from _stocks import *
from _indicators import indicators
from _config import start, end
from _sp import _stocks
from pandas.tseries.offsets import BDay
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


def GetCompanies():
    from sqlalchemy import create_engine
    import pandas as pd
    engine = create_engine('mssql://DESKTOP-C3PKM76\\SQLEXPRESS01/StockSniper?trusted_connection=yes&driver=ODBC+Driver+13+for+SQL+Server')
    con = engine.connect()    
    sql = """
    SELECT * FROM Companies
    """
    _ = (pd.read_sql(sql,con))
    con.close()
    return _.set_index('Symbol')


def CalculateDayOfWeek(_input):

	return 0

def BuildColumnsForExcel():
	pd.datetime.today()


	# Yesterday = 
	# TwoDays
	# ThreeDays
	# FourDays
	# FiveDays
	'''
	This function should determine based on what day it is today, what the columns should be.

	Maybe it should be Today, Yesterday, 2 days prior, 3 days prior, 4 days prior. This is pretty much what t

	'''
	return 0


import pandas as pd
end = pd.datetime.today()
# Today = (GetPeriodReturns(end - BDay(1),end))

print("Today = ", end, end - BDay(1))
# Today.columns = ['Today']
end = pd.datetime.today() - BDay(1) 

# Thursday = (GetPeriodReturns(end - BDay(1),end))
Thursday.columns = ['Thursday']
print("Thursday = ", end, end - BDay(1))
end = pd.datetime.today() - BDay(2) 
#Wednesday = (GetPeriodReturns(end - BDay(1),end))
Wednesday.columns = ['Wednesday']
end = pd.datetime.today() - BDay(3) 
#Tuesday = (GetPeriodReturns(end - BDay(1),end))
Tuesday.columns = ['Tuesday']
print("Checkpoint 1")
end = pd.datetime.today() - BDay(4) 
#Monday = (GetPeriodReturns(end - BDay(1),end))
Monday.columns = ['Monday']
#Week = (GetPeriodReturns(end - BDay(5),end))
print("Week = ", end, end-BDay(5))
# Week.columns = ['Week']
# Month = (GetPeriodReturns(end - BDay(20),end))
# Month.columns = ['Month']
# YTD = (GetPeriodReturns("2020-01-02" ,end))
# YTD.columns = ['YTD']
# Year = (GetPeriodReturns(end - BDay(250),end))
# Year.columns = ['Year']
# print("Checkpoint 2")
# TwoYear = (GetPeriodReturns(end - BDay(500),end))
# TwoYear.columns = ['TwoYear']
# FiveYear = (GetPeriodReturns(end - BDay(1250),end))
# FiveYear.columns = ['FiveYear']
# TenYear = (GetPeriodReturns(end - BDay(2500),end))
# TenYear.columns = ['TenYear']
# TwentyYear = (GetPeriodReturns(end - BDay(5000),end))
# TwentyYear.columns = ['TwentyYear']
# Companies = GetCompanies()
# _today_  = (pd.datetime.today())- BDay(1)
# _today_ = str(_today_).split(" ")[0]
# Indicators = GetCorrelations("2019-01-02",_today_)
# output = Monday.join(Tuesday).join(Wednesday).join(Thursday).join(Today).join(Week).join(Month).join(YTD).join(Year).join(TwoYear).join(FiveYear).join(TenYear).join(TwentyYear).join(Companies).join(Indicators)

