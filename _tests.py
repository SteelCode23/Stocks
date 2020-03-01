from pandas_datareader import data
start = "2005-1-1"
end = "2020-2-21"
MMM = data.DataReader("MMM",start=start, end=end,data_source='yahoo')
ABT = data.DataReader("ABT",start=start, end=end,data_source='yahoo')
ABBV = data.DataReader("ABBV",start=start, end=end,data_source='yahoo')
S_AND_P = {'MMM':MMM,'ABT':ABT,'ABBV':ABBV}
for key, values in S_AND_P.items():
	print(key, values)
	MMM[key] = values['Adj Close']
MMM.to_excel("C:/Data/Output.xlsx")

