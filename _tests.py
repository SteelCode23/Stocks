from _metrics import GetPeriodReturns
from pandas.tseries.offsets import BDay

end = pd.datetime.today() - BDay(1)

Today = (GetPeriodReturns(end - BDay(1),end))
Today.columns = ['Today']
Week = (GetPeriodReturns(end - BDay(5),end))
Week.columns = ['Week']
Month = (GetPeriodReturns(end - BDay(20),end))
Month.columns = ['Month']
YTD = (GetPeriodReturns("2020-01-02" ,end))
YTD.columns = ['YTD']
Year = (GetPeriodReturns(end - BDay(250),end))
Year.columns = ['Year']
TenYear = (GetPeriodReturns(end - BDay(2500),end))
TenYear.columns = ['TenYear']
TwentyYear = (GetPeriodReturns(end - BDay(5000),end))
TwentyYear.columns = ['TwentyYear']
