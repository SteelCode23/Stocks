

def DoRegression(regressor_, Stock):    
    X_ = np.array(regressor_)   
    Y_ = np.array(Stock)
    X_train = X_[:-20]
    X_test = X_[-20:]
    # Split the targets into training/testing sets
    Y_train = Y_[:-20]
    Y_test = Y_[-20:]
    regr = linear_model.LinearRegression()
    regr.fit(X_train, Y_train)
    y_pred = regr.predict(X_test)
    # The coefficients
    print('Coefficients: \n', regr.coef_)
    # The mean squared error
    print('Mean squared error: %.2f'
          % mean_squared_error(diabetes_y_test, diabetes_y_pred))
    # The coefficient of determination: 1 is perfect prediction
    print('Coefficient of determination: %.2f'
          % r2_score(diabetes_y_test, diabetes_y_pred))
    return r2_score(diabetes_y_test, diabetes_y_pred)


'''I think I need to pass a dictionary of lists in order to make this work'''
Indicator1 = regressor['CL=F'].tolist()
Indicator2 = regressor['UNRATE'].tolist()
Stock = regressor['MSFT'].tolist()
regressor = regressor.dropna()
regressor_ = []

for counter, i in enumerate(regressor.index):
    regressor_.append([Stock[counter],Indicator1[counter],Indicator2[counter]])


DoRegression(regressor,Stock)


start = "20000101"  
end = "20200320" 
def getStock(ticker, start, end):
    from sqlalchemy import create_engine
    from pandas_datareader import data
    engine = create_engine('mssql://DESKTOP-C3PKM76\\SQLEXPRESS01/StockSniper?trusted_connection=yes&driver=ODBC+Driver+13+for+SQL+Server')
    con = engine.connect()
    sql = """
    SELECT DISTINCT [DateKey], [Adj Close] FROM
    StockPrices WITH (NOLOCK)
    WHERE Ticker LIKE '""" + ticker + """'
    AND [DateKey] BETWEEN '""" + str(start) + """' and '""" + str(end) + """'
    """
    _ = pd.read_sql(sql, con)
    _ = _.set_index('DateKey')
    _.columns = [ticker]
    con.close()
    return _

def GetIndicator(ticker):
    from sqlalchemy import create_engine
    from pandas_datareader import data
    engine = create_engine('mssql://DESKTOP-C3PKM76\\SQLEXPRESS01/StockSniper?trusted_connection=yes&driver=ODBC+Driver+13+for+SQL+Server')
    con = engine.connect()    
    sql = """
    SELECT DISTINCT CAST(DateKey AS INT) DateKey, Stat
    FROM FREDIndicators
    WHERE Indicator = 'UNRATE'
    """
    _ = pd.read_sql(sql, con)
    _ = _.set_index('DateKey')
    _.columns = [ticker]
    con.close()
    return _



def ForecastStockTest(StockDataFrame, ticker, targetdate):
    X_test = ConvertADateToTheNumberNeededForPrediction(targetdate, StockDataFrame)
    X_test = int(X_test) + int(StockDataFrame.reset_index().index.max())
    X_ = []

    #This should contain multiple indicators.
    for counter, i in enumerate(StockDataFrame.index.tolist()):
        X_.append([i])
    X_ = np.array(X_)
    Y_ = np.array(StockDataFrame[ticker].tolist())
    X_train = X_
    # Split the targets into training/testing sets
    Y_train = Y_
    regr = linear_model.LinearRegression() 
    regr.fit(X_train, Y_train)
    y_pred = regr.predict(np.array([[X_test]]))
    print("I predict the price will be ", y_pred)
    return y_pred



def ForecastStock(ticker):
    '''I wonder if there's a way to do something along the lines of predicting a stock price based on that same stock price plus unemployment.'''
    '''
        I believe all that is required is to add a list to a list then the regressor works
    array([[-0.07816532,  0.05068012,  0.07786339,  0.05285819,  0.07823631]])
    '''

    from sklearn.linear_model import LinearRegression

    model = LinearRegression()
    model.fit(diabetes_X_train, diabetes_y_train)
    diabetes_y_pred = regr.predict(diabetes_X_test)


def ConvertDateKeyToDate(_input):
    '''Returns a date key from a date object'''
    import datetime
    _input = str(_input)
    year = _input[:4]
    month = _input[5:7]
    day = _input[-2:]
    x = datetime.datetime(int(year), int(month), int(day))
    return x



def ConvertDateToDateKey(_input):
    '''Returns a date from a datekey object'''    
    return str(_input).split(" ")[0].replace("-","")



def ConvertADateToTheNumberNeededForPrediction(target, indexobject): 
    '''This should take in a target as well an index list from the stock object and
    return a number to use to pass into the prediction object'''
    mindate = indexobject.index.max()
    maxdate = target

    return GetBusinessDaysBetweenTwoDates(mindate, maxdate)



def GetBusinessDaysBetweenTwoDates(start,end):
    _ =pd.read_sql("""SELECT dbo.fn_GetBusinessDays('""" + start + """','""" + end + """') 'Days'""",con)['Days'].tolist()[0]
    return _


def ConvertDataFrameIndexToDateFromDateKey(data2)
    data2['Date'] = data2.index
    data2['Date'] = data2['Date'].apply(ConvertDateKeyToDate)
    data2 = data2.set_index('Date')
    return data2


def GetLastDayFromDataFrame():
    return _


def ForecastStockBasedOnFutureUnemployment():
    return 0


def ForecastStock2(StockDataFrame, ticker, targetdate):
    X_test = ConvertADateToTheNumberNeededForPrediction(targetdate, StockDataFrame)
    X_ = np.array(StockDataFrame.reset_index().index.tolist())
    Y_ = np.array(StockDataFrame[ticker].tolist())
    X_train = X_
    # Split the targets into training/testing sets
    Y_train = Y_
    Y_test = Y_[-20:]
    regr = linear_model.LinearRegression()
    regr.fit(X_train, Y_train)
    y_pred = regr.predict(X_test)
    # The coefficients
    print('Coefficients: \n', regr.coef_)
    # The mean squared error
    print('Mean squared error: %.2f'
          % mean_squared_error(diabetes_y_test, diabetes_y_pred))
    # The coefficient of determination: 1 is perfect prediction
    print('Coefficient of determination: %.2f'
          % r2_score(diabetes_y_test, diabetes_y_pred))
    return r2_score(diabetes_y_test, diabetes_y_pred)


def ForecastIndicator(indicator):
    '''
    To do this, I think you simply need to do a regression vs time and then predict using a future time variable.
    '''

    raise


def ReturnCorrelatedIndicators():

    '''
    This Function Returns the Available Indicators with the Highest R2 score
    compared with the stock.
    '''
    return 0


def CalculateReturnFromPortfolio(stocklist):
    '''Takes a list of stocks and returns the estimated return from the stocks.'''
    return 0