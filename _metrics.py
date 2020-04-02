def RSquared(ticker):
    import pandas as pd
    import pandas_datareader.data as web
    from _transformations import AdjustDate
    import statsmodels.formula.api as smf
    from _config import start, end
    import numpy as np
    data = pd.read_excel("http://www.stockpup.com/data/" + ticker +"_quarterly_financial_data.xls")
    data = data.set_index('Quarter end').T.reset_index()
    data = data.set_index('index')
    OilPrices = web.DataReader('DCOILWTICO', 'fred', start, end)
    OilPrices = OilPrices.resample(rule='Y').mean()
    OilPrices = OilPrices[['DCOILWTICO']].reset_index()
    OilPrices['DATE'] = OilPrices['DATE'].apply(AdjustDate)
    OilPrices = OilPrices.set_index('DATE')
    yearsdata = data.resample(rule='Y').sum()
    _ = yearsdata[['Earnings']].reset_index()
    _['index'] = _['index'].apply(AdjustDate)
    _ = _.set_index('index')
    _ = _.join(OilPrices).dropna()
    _.columns = ['Earnings','OilPrices']
    mod = smf.ols('Earnings ~ np.log(OilPrices)', _).fit()
    return mod.rsquared

def DateKey(_input_):
    _ = str(_input_).split(" ")[0]
    _ = _.split("-")
    _ = str(_[0]) + str(_[1]) + str(_[2]) 
    return _


def ConvertDateKeyToDate(_input):
    '''Returns a date key from a date object'''
    import datetime
    _input = str(_input)
    year = _input[:4]
    month = _input[4:6]
    day = _input[-2:]
    x = datetime.datetime(int(year), int(month), int(day))
    return x


def GetDataInPeriod(ticker, start,end):
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
    StockSniper.dbo.StockPrices
    WHERE DateKey BETWEEN  '""" + str(start) + """' and  '""" + str(end) + """' and Ticker = '""" + str(ticker) +"""'
    """
    _ = (pd.read_sql(sql,con))
    _['FullDate'] = _['FullDate'].apply(ConvertDateKeyToDate)
    con.close() 
    return _.set_index("FullDate")


def ConvertDateToDateKey(_input):
    '''Returns a date from a datekey object'''    
    return str(_input).split(" ")[0].replace("-","")


def GetRiskiness(ticker, start, end):
    import pandas as pd
    _ =GetDataInPeriod(ticker,start,end)
    output_ = pd.DataFrame(columns = ['Ticker','PriceRisk','ReturnRisk','Volatility'])
    output_['PriceRisk'] = np.std(_)
    output_['ReturnRisk'] = np.std(_.pct_change())
    output_['Volatility'] = np.std(_) / np.mean(_)
    output_['Ticker'] = ticker
    return output_.set_index('Ticker')


def GetCorrelations(start,end):
    import numpy as np
    import pandas as pd
    from sqlalchemy import create_engine    
    engine = create_engine('mssql://DESKTOP-C3PKM76\\SQLEXPRESS01/StockSniper?trusted_connection=yes&driver=ODBC+Driver+13+for+SQL+Server')
    con = engine.connect()    

    start = DateKey(start)
    end = DateKey(end)    
    _ = pd.read_sql("""
    SELECT * FROM StockPrices
    WHERE DateKey BETWEEN """ + str(start) + """ and """ + str(end) + """ 
    """,con)
    table = pd.pivot_table(_, values='Adj Close', index=['DateKey'],columns=['Ticker'], aggfunc=np.mean, fill_value=0)
    _ = table.corr().reset_index()
    _.index = _['Ticker']
    test = _[["^VIX","^GSPC","GC=F","CL=F"]]
    test.columns = ['corr w/Volatilty','corr w/S%P','corr w/Gold','corr w/Oil']
    return test


def DaysReturns(ticker):
    from pandas_datareader import data
    start = "2020-03-17"
    end = "2020-03-18"
    _ = data.DataReader(ticker,start = start, end = end,data_source='yahoo')
    output = [ticker,_.pct_change()['Adj Close'].max()]
    return output


def GetLatestFundamentals():
    import pandas as pd
    from sqlalchemy import create_engine
    engine = create_engine('mssql://DESKTOP-C3PKM76\\SQLEXPRESS01/StockSniper?trusted_connection=yes&driver=ODBC+Driver+13+for+SQL+Server')
    con = engine.connect()       
    _ = pd.read_sql("""
    DECLARE @Latest DateTime
    SELECT @Latest = MAX(RecordDate) FROM StockSniper.dbo.StockFundamentals
    SELECT * FROM StockSniper.dbo.StockFundamentals WHERE RecordDate = @Latest
    """,con)
    con.close()
    return _.set_index('Ticker').drop_duplicates()


def GetStockRisk():
    import pandas as pd
    from sqlalchemy import create_engine
    engine = create_engine('mssql://DESKTOP-C3PKM76\\SQLEXPRESS01/StockSniper?trusted_connection=yes&driver=ODBC+Driver+13+for+SQL+Server')
    con = engine.connect()       
    _ = pd.read_sql("""
    DECLARE @Latest DateTime
    SELECT @Latest = MAX(RecordDate) FROM StockSniper.dbo.StockRisk
    SELECT * FROM StockSniper.dbo.StockRisk WHERE RecordDate = @Latest
    """,con)
    con.close()
    return _.set_index('index').drop_duplicates()


def GetDataInPeriod(ticker, start,end):
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
    StockSniper.dbo.StockPrices
    WHERE DateKey BETWEEN  """ + str(start) + """ and  """ + str(end) + """ and Ticker = """ + str(ticker) +"""
    """
    _ = (pd.read_sql(sql,con))
    _['FullDate'] = _['FullDate'].apply(ConvertDateKeyToDate)
    con.close() 
    return _


def GetTSXReturns(start,end):
    from pandas_datareader import data
    from pandas.tseries.offsets import BDay
    from sqlalchemy import create_engine
    import pandas as pd
    engine = create_engine('mssql://DESKTOP-C3PKM76\\SQLEXPRESS01/StockSniper?trusted_connection=yes&driver=ODBC+Driver+13+for+SQL+Server')
    con = engine.connect()    
    start = DateKey(start)
    end = DateKey(end)
    sql = """;with step1 as (
    SELECT [Adj Close], Ticker, DateKey
    FROM  [StockSniper].[dbo].[TSXStockPrices]
    WHERE DateKey = """ + str(start) + """
    ),
    step2 as (
    SELECT [Adj Close], Ticker, DateKey
    FROM  [StockSniper].[dbo].[TSXStockPrices]
    WHERE DateKey = """ + str(end) + """
    )
    SELECT
    (s2.[Adj Close] - s1.[Adj Close])/s1.[Adj Close] DaysReturn,s1.Ticker
    FROM step1 s1 join step2 s2 on s1.Ticker = s2.Ticker
    """
    _ = (pd.read_sql(sql,con))
    con.close()

    return _.set_index('Ticker').drop_duplicates()


def GetPeriodReturns(start,end):
    from pandas_datareader import data
    from pandas.tseries.offsets import BDay
    from sqlalchemy import create_engine
    import pandas as pd
    engine = create_engine('mssql://DESKTOP-C3PKM76\\SQLEXPRESS01/StockSniper?trusted_connection=yes&driver=ODBC+Driver+13+for+SQL+Server')
    con = engine.connect()    
    start = DateKey(start)
    end = DateKey(end)
    sql = """;with step1 as (
    SELECT [Adj Close], Ticker, DateKey
    FROM StockPrices
    WHERE DateKey = """ + str(start) + """
    ),
    step2 as (
    SELECT [Adj Close], Ticker, DateKey
    FROM StockPrices
    WHERE DateKey = """ + str(end) + """
    )
    SELECT
    (s2.[Adj Close] - s1.[Adj Close])/s1.[Adj Close] DaysReturn,s1.Ticker
    FROM step1 s1 join step2 s2 on s1.Ticker = s2.Ticker
    """
    _ = (pd.read_sql(sql,con))
    con.close()

    return _.set_index('Ticker').drop_duplicates()


def YesterdayReturns(ticker):
    from pandas_datareader import data
    from pandas.tseries.offsets import BDay
    from sqlalchemy import create_engine
    engine = create_engine('mssql://DESKTOP-C3PKM76\\SQLEXPRESS01/StockSniper?trusted_connection=yes&driver=ODBC+Driver+13+for+SQL+Server')
    con = engine.connect()
    start = pd.datetime.today() - BDay(2)
    start = DateKey(start)

    end = pd.datetime.today() - BDay(1)
    end = DateKey(end)    
    _ = data.DataReader(ticker,start = start, end = end,data_source='yahoo')
    sql = """
    SELECT [DateKey], [Adj Close] FROM
    StockPrices WITH (NOLOCK)
    WHERE Ticker LIKE '""" + ticker + """'
    AND [DateKey] BETWEEN '""" + str(start) + """' and '""" + str(end) + """'
    """
    print(sql)    
    _ = pd.read_sql(sql, con)
    output = [ticker,_.pct_change()['Adj Close'].max()]
    return output


def GainerDaysYTD(ticker):
    from pandas_datareader import data
    from pandas.tseries.offsets import BDay
    start = "2020-01-01"
    end_ = pd.datetime.today()
    sql = """
    SELECT [Date], [Adj Close] FROM
    StockPrices WITH (NOLOCK)
    WHERE Ticker LIKE '""" + ticker + """'
    AND [Date] BETWEEN '""" + str(start) + """' and '""" + str(end) + """'
    """
    _ = pd.read_sql(sql, con)
    output = [ticker,_['Adj Close'].pct_change().fillna(0).gt(0).sum()]
    return output


def LoserDays(ticker):
    from pandas_datareader import data
    from pandas.tseries.offsets import BDay
    start = "2020-01-15"
    end = pd.datetime.today()- BDay(1)    
    sql = """
    SELECT [Date], [Adj Close] FROM
    StockPrices WITH (NOLOCK)
    WHERE Ticker LIKE '""" + ticker + """'
    AND [Date] BETWEEN '""" + str(start) + """' and '""" + str(end) + """'
    """
    _ = pd.read_sql(sql, con)
    output = [ticker,_['Adj Close'].pct_change().fillna(0).lt(0).sum()]
    return output


def CurrentPrice(ticker):
    from pandas_datareader import data
    from pandas.tseries.offsets import BDay
    start = "2020-03-15"
    end = pd.datetime.today()- BDay(1)    
    sql = """
    SELECT [Date], [Adj Close] FROM
    StockPrices WITH (NOLOCK)
    WHERE Ticker LIKE '""" + ticker + """'
    AND [Date] BETWEEN '""" + str(start) + """' and '""" + str(end) + """'
    """
    _ = pd.read_sql(sql, con)
    output = [ticker,_['Adj Close'].last('D')[0]]
    return output


def QuartersReturns(ticker):
    from pandas_datareader import data
    from pandas.tseries.offsets import BDay
    start = "2020-01-01"
    end = pd.datetime.today()- BDay(1)    
    sql = """
    SELECT [Date], [Adj Close] FROM
    StockPrices WITH (NOLOCK)
    WHERE Ticker LIKE '""" + ticker + """'
    AND [Date] BETWEEN '""" + str(start) + """' and '""" + str(end) + """'
    """
    _ = pd.read_sql(sql, con)
    output = [ticker,_['Adj Close'].pct_change().cumsum().last('D')[0]]
    return output


def YearsReturns(ticker):
    ''' Returns YTD Return since January 1st, 2020'''
    from pandas_datareader import data
    from pandas.tseries.offsets import BDay
    start = "2020-01-01"
    end = pd.datetime.today()- BDay(1)    
    sql = """
    SELECT [Date], [Adj Close] FROM
    StockPrices WITH (NOLOCK)
    WHERE Ticker LIKE '""" + ticker + """'
    AND [Date] BETWEEN '""" + str(start) + """' and '""" + str(end) + """'
    """
    _ = pd.read_sql(sql, con)
    output = [ticker,_['Adj Close'].pct_change().cumsum().last('D')[0]]
    return output


def TenYearsReturns(ticker):
    ''' Returns 10 year Return since January 1st, 2010'''    
    from pandas_datareader import data
    from pandas.tseries.offsets import BDay
    start = "2010-01-01"
    end = pd.datetime.today()- BDay(1)
    sql = """
    SELECT [Date], [Adj Close] FROM
    StockPrices WITH (NOLOCK)
    WHERE Ticker LIKE '""" + ticker + """'
    AND [Date] BETWEEN '""" + str(start) + """' and '""" + str(end) + """'
    """
    _ = pd.read_sql(sql, con)
    output = [ticker,_['Adj Close'].pct_change().cumsum().last('D')[0]]
    return output


def FiveYearsReturns(ticker):
    ''' Returns 10 year Return since January 1st, 2010'''    
    from pandas_datareader import data
    from pandas.tseries.offsets import BDay
    start = "2010-01-01"
    end = pd.datetime.today()- BDay(1)
    sql = """
    SELECT [Date], [Adj Close] FROM
    StockPrices WITH (NOLOCK)
    WHERE Ticker LIKE '""" + ticker + """'
    AND [Date] BETWEEN '""" + str(start) + """' and '""" + str(end) + """'
    """
    _ = pd.read_sql(sql, con)
    output = [ticker,_['Adj Close'].pct_change().cumsum().last('D')[0]]
    return output

def TwentyYearsReturns(ticker):
    ''' Returns 10 year Return since January 1st, 2010'''    
    from pandas_datareader import data
    from pandas.tseries.offsets import BDay
    start = "2000-01-01"  
    end = pd.datetime.today()- BDay(1)
    sql = """
    SELECT [Date], [Adj Close] FROM
    StockPrices WITH (NOLOCK)
    WHERE Ticker LIKE '""" + ticker + """'
    AND [Date] BETWEEN '""" + str(start) + """' and '""" + str(end) + """'
    """
    _ = pd.read_sql(sql, con)
    output = [ticker,_['Adj Close'].pct_change().cumsum().last('D')[0]]
    return output


def GetDividendYieldAndPERatio(Ticker):
    import pandas as pd
    _ = data.get_quote_yahoo(Ticker)    
    _ = _[['trailingAnnualDividendRate',
    'trailingPE',
    'trailingAnnualDividendYield',
    'marketCap',
    'priceToBook',
    'forwardPE',
    'price',
    'tradeable']]
    _['marketCap Billions'] = _['marketCap'] / 1000000000
    return _ 

def BuildDivYieldForAllstocks(stocks):
    _output = pd.DataFrame(columns = ['DividendRate', 'PE','Div Yield', 'marketCap', 'priceToBook', 'forwardPE',       'price', 'tradeable', 'marketCap Billions'])

    for stock in stocks:
        _output = pd.concat([_output,GetDividendYieldAndPERatio(stock)])
    return


def GetPlotForStock(start,end, stock):
    return None