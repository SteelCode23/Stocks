

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


def GetTSXCompanies():
    from sqlalchemy import create_engine
    import pandas as pd
    engine = create_engine('mssql://DESKTOP-C3PKM76\\SQLEXPRESS01/StockSniper?trusted_connection=yes&driver=ODBC+Driver+13+for+SQL+Server')
    con = engine.connect()    
    sql = """
    SELECT * FROM TSX
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

def GetRiskiness(ticker, start, end):
    import pandas as pd
    _ =GetTSXData(ticker,start,end)
    output_ = pd.DataFrame(columns = ['Ticker','PriceRisk','ReturnRisk','Volatility'])
    output_['PriceRisk'] = np.std(_)
    output_['ReturnRisk'] = np.std(_.pct_change())
    output_['Volatility'] = np.std(_) / np.mean(_)
    output_['Ticker'] = ticker
    return output_.set_index('Ticker')


def GetTSXData(ticker, start,end):
    from pandas_datareader import data
    from pandas.tseries.offsets import BDay
    from sqlalchemy import create_engine
    import pandas as pd
    engine = create_engine('mssql://DESKTOP-C3PKM76\\SQLEXPRESS01/StockSniper?trusted_connection=yes&driver=ODBC+Driver+13+for+SQL+Server')
    con = engine.connect()    
    start = DateKey(start)
    end = DateKey(end)
    sql = """SELECT [Adj Close], DateKey FullDate
    FROM
    StockSniper.dbo.[TSXStockPrices]
    WHERE DateKey BETWEEN  '""" + str(start) + """' and  '""" + str(end) + """' and Ticker = '""" + str(ticker) +"""'
    """
    _ = (pd.read_sql(sql,con))
    _['FullDate'] = _['FullDate'].apply(ConvertDateKeyToDate)
    con.close() 
    return _.set_index("FullDate")


def GetBulkRiskiness(stocks, start, end):
    import pandas as pd
    start_ = pd.DataFrame(columns = ['PriceRisk', 'ReturnRisk', 'Volatility'])
    for stock in stocks:
        _ = GetRiskiness(stock, start, end)
        start_ = pd.concat([start_,_])
    return start_    

import pandas as pd
_days_of_week = {
	0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday"
}

end = pd.datetime.today() - BDay(1)

#risk = GetBulkRiskiness(_stocks, start = pd.datetime.today() - BDay(60), end = pd.datetime.today())

try:
	risk = pd.read_excel("Risk.xlsx")
	risk.to_excel("Risk.xlsx")
except Exception:
	pass
import pandas as pd
end = pd.datetime.today() - BDay(1)
Today = (GetTSXReturns(end - BDay(1),end))
Today.columns = ["Monday"]
end = pd.datetime.today() - BDay(2) 
Thursday = (GetTSXReturns(end - BDay(1),end))
Thursday.columns = ["Friday"]
end = pd.datetime.today() - BDay(3) 
Wednesday = (GetTSXReturns(end - BDay(1),end))
Wednesday.columns = ["Thursday"]
end = pd.datetime.today() - BDay(4) 
Tuesday = (GetTSXReturns(end - BDay(1),end))
Tuesday.columns = ["Wednesday"]
print("Checkpoint 1")
end = pd.datetime.today() - BDay(5) 
Monday = (GetTSXReturns(end - BDay(1),end))
Monday.columns =["Tuesday"]


#Reset End Date to mean yesterday.
end = pd.datetime.today() - BDay(1)
Week = (GetTSXReturns(end - BDay(5),end))
Week.columns = ['Week']
Month = (GetTSXReturns(end - BDay(20),end))
Month.columns = ['Month']
YTD = (GetTSXReturns("2020-01-02" ,end))
YTD.columns = ['YTD']
Year = (GetTSXReturns(end - BDay(250),end))
Year.columns = ['Year']
print("Checkpoint 2")
TwoYear = (GetTSXReturns(end - BDay(500),end))
TwoYear.columns = ['TwoYear']
FiveYear = (GetTSXReturns(end - BDay(1250),end))
FiveYear.columns = ['FiveYear']
TenYear = (GetTSXReturns(end - BDay(2500),end))
TenYear.columns = ['TenYear']
TwentyYear = (GetTSXReturns(end - BDay(5000),end))
TwentyYear.columns = ['TwentyYear']
Companies = GetTSXCompanies()
_today_  = (pd.datetime.today())- BDay(1)
_today_ = str(_today_).split(" ")[0]
#Indicators = GetCorrelations("2019-01-02",_today_)
fundamentals = GetLatestFundamentals()

print(Monday)
print(Tuesday)
print(Wednesday)
import pdb
try:
	output = Monday.join(Tuesday).join(Wednesday).join(Thursday).join(Today).join(Week).join(Month).join(risk).join(YTD).join(Year).join(TwoYear).join(FiveYear).join(TenYear).join(TwentyYear).join(Companies)
except Exception:
	pdb.set_trace()

print("Checkpoint 3")
try:
	output.drop_duplicates().to_excel("C:/Users/Steel/TSX.xlsx")
except Exception:
	output.to_excel("C:/Users/Steel/TSX3" + str(_today_) + ".xlsx")
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

# _score = {}
# #_stocks = ['MSFT','AAPL']
# _err = []
# for stock in _stocks:
# 	try:
# 		output = GainerDays(stock)
# 		_score[output[0]] = output[1]
# 	except Exception as e:
# 		_err.append(e)

# _try_ = pd.DataFrame.from_dict(_score, orient='index')
# _try_.to_excel('GainerDays.xlsx')



# _score = {}
# #_stocks = ['MSFT','AAPL']
# _err = []
# for stock in _stocks:
# 	try:
# 		output = LoserDays(stock)
# 		_score[output[0]] = output[1]
# 	except Exception as e:
# 		_err.append(e)

# _try_ = pd.DataFrame.from_dict(_score, orient='index')
# _try_.to_excel('LoserDays.xlsx')



# _score = {}
# #_stocks = ['MSFT','AAPL']
# _err = []
# for stock in _stocks:
# 	try:
# 		output = DaysReturns(stock)
# 		_score[output[0]] = output[1]
# 	except Exception as e:
# 		print(e)
# 		_err.append(e)

# _try_ = pd.DataFrame.from_dict(_score, orient='index')
# _try_.to_excel('DailyReturnsEOD.xlsx')




# _score = {}
# #_stocks = ['MSFT','AAPL']
# _err = []
# for stock in _stocks:
# 	try:
# 		output = TenYearsReturns(stock)
# 		_score[output[0]] = output[1]
# 	except Exception as e:
# 		_err.append(e)

# _try_ = pd.DataFrame.from_dict(_score, orient='index')
# _try_.to_excel('TenYearsReturns.xlsx')
# print(_err)

