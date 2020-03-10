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


def DaysReturns(ticker):
    from pandas_datareader import data
    start = "2020-03-06"
    end = "2020-03-09"
    _ = data.DataReader(ticker,start = start, end = end,data_source='yahoo')
    output = [ticker,_.pct_change()['Adj Close'].max()]
    return output


def QuartersReturns(ticker):
    from pandas_datareader import data
    start = "2020-01-01"
    end = "2020-03-09"
    _ = data.DataReader(ticker,start = start, end = end,data_source='yahoo')
    output = [ticker,_['Adj Close'].pct_change().cumsum().last('D')[0]]
    return output


def YearsReturns(ticker):
    from pandas_datareader import data
    start = "2019-03-09"
    end = "2020-03-09"
    _ = data.DataReader(ticker,start = start, end = end,data_source='yahoo')
    output = [ticker,_['Adj Close'].pct_change().cumsum().last('D')[0]]
    return output


def TenYearsReturns(ticker):
    from pandas_datareader import data
    start = "2010-03-09"
    end = "2020-03-09"
    _ = data.DataReader(ticker,start = start, end = end,data_source='yahoo')
    output = [ticker,_['Adj Close'].pct_change().cumsum().last('D')[0]]
    return output


def ForecastStock(ticker):
    raise


def ForecastIndicator(indicator):
    ''''''
    raise

def CalculateReturnFromPortfolio(stocklist):
    '''Takes a list of stocks and returns the estimated return from the stocks.'''