
from _sp import _FREDindicatorsDICT,_YAHOOindicators

def DateKey(_input_):
	'''
	A simple function to convert full dates to a DateKey
	'''
	_ = str(_input_).split(" ")[0]
	_ = _.split("-")
	_ = str(_[0]) + str(_[1]) + str(_[2]) 
	return _


def LoadFredData(indicator, agg):
	'''
	Get the Indicators data from FRED
	'''	
	from sqlalchemy import create_engine
	import pandas_datareader.data as web	
	engine = create_engine('mssql://DESKTOP-C3PKM76\\SQLEXPRESS01/StockSniper?trusted_connection=yes&driver=ODBC+Driver+13+for+SQL+Server')
	con = engine.connect()
	start = "2000-01-01"
	end = "2020-03-19"
	#from _config import start, end
	INDICATOR = web.DataReader(indicator, 'fred', start, end)
	if agg == 'MEAN':
		INDICATOR = INDICATOR.resample(rule='Q').mean()
	elif agg == 'SUM':
		INDICATOR = INDICATOR.resample(rule='Q').sum()
	else:
		INDICATOR = INDICATOR.resample(rule='Q').mean()
	INDICATOR['Indicator'] = indicator	
	INDICATOR.columns = ['Stat','Indicator']
	INDICATOR = INDICATOR.reset_index()
	INDICATOR['DateKey'] = INDICATOR['DATE'].apply(DateKey)
	INDICATOR.to_sql('FREDIndicators',con=engine, if_exists = 'append')
	con.close()


def LoadYahooData(indicator):
	'''
	Get the Indicators data from Yahoo
	'''
	from sqlalchemy import create_engine
	from pandas_datareader import data
	engine = create_engine('mssql://DESKTOP-C3PKM76\\SQLEXPRESS01/StockSniper?trusted_connection=yes&driver=ODBC+Driver+13+for+SQL+Server')
	con = engine.connect()
	start = "2000-01-01"
	end = "2020-03-19"
	_ = data.DataReader(indicator,start = start, end = end,data_source='yahoo')
	_['Indicator'] = indicator
	_ = _.reset_index()
	_['DateKey'] = _['Date'].apply(DateKey)
	_ = _[['Date','Adj Close' ,'Indicator' , 'DateKey']]
	_['Frequency'] ='D'
	_.columns = ['DATE','Stat','Indicator','DateKey','Frequency']
	_.to_sql('FREDIndicators',con=engine, if_exists = 'append')
	con.close()


def LoadAllYahoo():
	for i in _YAHOOindicators:
		LoadYahooData(i)

def LoadAllFRED():
	for key,values in _FREDindicatorsDICT.items():
		for value in values:
			print(key, value)
			LoadFredData(value,key)


def _run():
	LoadAllYahoo()
	LoadAllFRED()

_run()