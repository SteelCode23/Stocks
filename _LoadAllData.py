from _sp import _stocks,_YAHOOindicators

def DateKey(_input_):
	_ = str(_input_).split(" ")[0]
	_ = _.split("-")
	_ = str(_[0]) + str(_[1]) + str(_[2]) 
	return _


def LoadStockReturns(ticker):
	from sqlalchemy import create_engine
	engine = create_engine('mssql://DESKTOP-C3PKM76\\SQLEXPRESS01/StockSniper?trusted_connection=yes&driver=ODBC+Driver+13+for+SQL+Server')
	con = engine.connect()
	from pandas_datareader import data
	start = "2020-03-21"
	end = "2020-03-24"
	_ = data.DataReader(ticker,start = start, end = end,data_source='yahoo')
	_['Ticker'] = ticker
	_ = _.reset_index()
	_['DateKey'] = _['Date'].apply(DateKey)
	_.to_sql('StockPrices',con=engine, if_exists = 'append')
	con.close()


def BulkLoadStockReturns(ticker):
	import datetime
	from sqlalchemy import create_engine
	engine = create_engine('mssql://DESKTOP-C3PKM76\\SQLEXPRESS01/StockSniper?trusted_connection=yes&driver=ODBC+Driver+13+for+SQL+Server')
	con = engine.connect()
	from pandas_datareader import data
	start = "2020-03-23"
	end = "2020-03-28"
	_ = data.DataReader(ticker,start = start, end = end,data_source='yahoo')
	_['Ticker'] = ticker
	_ = _.reset_index()
	_['DateKey'] = _['Date'].apply(DateKey)
	_ =_[['DateKey', 'High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close', 'Ticker']]
	_.set_index('DateKey').to_sql('StockPrices',con=engine, if_exists = 'append')
	con.close()


# for i in _stocks:
# 	try:
# 		BulkLoadStockReturns(i)
# 		print("Success")
# 	except Exception as e:
# 		print(e,i)
for counter, stock in enumerate(_stocks):	
	try:
	# try:
		BulkLoadStockReturns(stock)
	except Exception as e:
		print(e)