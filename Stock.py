
class Stock:

    def __init__(self, stock):
        self.stock = stock
    
    def Stock(self):
        '''Returns CumSum of a specific stock'''
        from pandas_datareader import data
        aapl = data.DataReader("JNJ",start='2019-1-1', 
                               end='2020-02-21', 
                               data_source='yahoo')#['Adj Close']
        import numpy as np
        plt.figure(figsize = (10,10))
        plt.title(self.stock)
        plt.legend()
        aapl2 = data.DataReader('ENB',start='2019-1-1', 
                               end='2020-02-21', 
                               data_source='yahoo')#['Adj Close']       
        
        aapl['Adj Close'].cumsum().plot()
        aapl2['Adj Close'].cumsum().plot()

	def buildSmallDataFrame():
		start = "2005-1-1"
		end = "2020-2-21"
		MMM = data.DataReader("MMM",start=start, end=end,data_source='yahoo')
		ABT = data.DataReader("ABT",start=start, end=end,data_source='yahoo')
		ABBV = data.DataReader("ABBV",start=start, end=end,data_source='yahoo')
		output = [MMM,ABT,ABBV]
		for i in output:
			MMM[str(i)] = i['Adj Close']
		return MMM

    def BuildDataframe():
		start = "2005-1-1"
		end = "2020-2-21"
		MMM = data.DataReader("MMM",start=start, end=end,data_source='yahoo')
		ABT = data.DataReader("ABT",start=start, end=end,data_source='yahoo')
		ABBV = data.DataReader("ABBV",start=start, end=end,data_source='yahoo')
		ABMD = data.DataReader("ABMD",start=start, end=end,data_source='yahoo')
		ACN = data.DataReader("ACN",start=start, end=end,data_source='yahoo')
		ATVI = data.DataReader("ATVI",start=start, end=end,data_source='yahoo')
		ADBE = data.DataReader("ADBE",start=start, end=end,data_source='yahoo')
		AMD = data.DataReader("AMD",start=start, end=end,data_source='yahoo')
		AAP = data.DataReader("AAP",start=start, end=end,data_source='yahoo')
		AES = data.DataReader("AES",start=start, end=end,data_source='yahoo')
		AFL = data.DataReader("AFL",start=start, end=end,data_source='yahoo')
		A = data.DataReader("A",start=start, end=end,data_source='yahoo')
		APD = data.DataReader("APD",start=start, end=end,data_source='yahoo')
		AKAM = data.DataReader("AKAM",start=start, end=end,data_source='yahoo')
		ALK = data.DataReader("ALK",start=start, end=end,data_source='yahoo')
		ALB = data.DataReader("ALB",start=start, end=end,data_source='yahoo')
		ARE = data.DataReader("ARE",start=start, end=end,data_source='yahoo')
		ALXN = data.DataReader("ALXN",start=start, end=end,data_source='yahoo')
		ALGN = data.DataReader("ALGN",start=start, end=end,data_source='yahoo')
		ALLE = data.DataReader("ALLE",start=start, end=end,data_source='yahoo')
		AGN = data.DataReader("AGN",start=start, end=end,data_source='yahoo')
		ADS = data.DataReader("ADS",start=start, end=end,data_source='yahoo')
		LNT = data.DataReader("LNT",start=start, end=end,data_source='yahoo')
		ALL = data.DataReader("ALL",start=start, end=end,data_source='yahoo')
		GOOGL = data.DataReader("GOOGL",start=start, end=end,data_source='yahoo')
		GOOG = data.DataReader("GOOG",start=start, end=end,data_source='yahoo')
		MO = data.DataReader("MO",start=start, end=end,data_source='yahoo')
		AMZN = data.DataReader("AMZN",start=start, end=end,data_source='yahoo')
		AMCR = data.DataReader("AMCR",start=start, end=end,data_source='yahoo')
		AEE = data.DataReader("AEE",start=start, end=end,data_source='yahoo')
		AAL = data.DataReader("AAL",start=start, end=end,data_source='yahoo')
		AEP = data.DataReader("AEP",start=start, end=end,data_source='yahoo')
		AXP = data.DataReader("AXP",start=start, end=end,data_source='yahoo')
		AIG = data.DataReader("AIG",start=start, end=end,data_source='yahoo')
		AMT = data.DataReader("AMT",start=start, end=end,data_source='yahoo')
		AWK = data.DataReader("AWK",start=start, end=end,data_source='yahoo')
		AMP = data.DataReader("AMP",start=start, end=end,data_source='yahoo')
		ABC = data.DataReader("ABC",start=start, end=end,data_source='yahoo')
		AME = data.DataReader("AME",start=start, end=end,data_source='yahoo')
		AMGN = data.DataReader("AMGN",start=start, end=end,data_source='yahoo')
		APH = data.DataReader("APH",start=start, end=end,data_source='yahoo')
		ADI = data.DataReader("ADI",start=start, end=end,data_source='yahoo')
		ANSS = data.DataReader("ANSS",start=start, end=end,data_source='yahoo')
		ANTM = data.DataReader("ANTM",start=start, end=end,data_source='yahoo')
		AON = data.DataReader("AON",start=start, end=end,data_source='yahoo')
		AOS = data.DataReader("AOS",start=start, end=end,data_source='yahoo')
		APA = data.DataReader("APA",start=start, end=end,data_source='yahoo')
		AIV = data.DataReader("AIV",start=start, end=end,data_source='yahoo')
		AAPL = data.DataReader("AAPL",start=start, end=end,data_source='yahoo')
		AMAT = data.DataReader("AMAT",start=start, end=end,data_source='yahoo')
		APTV = data.DataReader("APTV",start=start, end=end,data_source='yahoo')
		ADM = data.DataReader("ADM",start=start, end=end,data_source='yahoo')
		ARNC = data.DataReader("ARNC",start=start, end=end,data_source='yahoo')
		ANET = data.DataReader("ANET",start=start, end=end,data_source='yahoo')
		AJG = data.DataReader("AJG",start=start, end=end,data_source='yahoo')
		AIZ = data.DataReader("AIZ",start=start, end=end,data_source='yahoo')
		ATO = data.DataReader("ATO",start=start, end=end,data_source='yahoo')
		T = data.DataReader("T",start=start, end=end,data_source='yahoo')
		ADSK = data.DataReader("ADSK",start=start, end=end,data_source='yahoo')
		ADP = data.DataReader("ADP",start=start, end=end,data_source='yahoo')
		AZO = data.DataReader("AZO",start=start, end=end,data_source='yahoo')
		AVB = data.DataReader("AVB",start=start, end=end,data_source='yahoo')
		AVY = data.DataReader("AVY",start=start, end=end,data_source='yahoo')
		BKR = data.DataReader("BKR",start=start, end=end,data_source='yahoo')
		BLL = data.DataReader("BLL",start=start, end=end,data_source='yahoo')
		BAC = data.DataReader("BAC",start=start, end=end,data_source='yahoo')
		BK = data.DataReader("BK",start=start, end=end,data_source='yahoo')
		BAX = data.DataReader("BAX",start=start, end=end,data_source='yahoo')
		BDX = data.DataReader("BDX",start=start, end=end,data_source='yahoo')
		BRK.B = data.DataReader("BRK.B",start=start, end=end,data_source='yahoo')
		BBY = data.DataReader("BBY",start=start, end=end,data_source='yahoo')
		BIIB = data.DataReader("BIIB",start=start, end=end,data_source='yahoo')
		BLK = data.DataReader("BLK",start=start, end=end,data_source='yahoo')
		BA = data.DataReader("BA",start=start, end=end,data_source='yahoo')
		BKNG = data.DataReader("BKNG",start=start, end=end,data_source='yahoo')
		BWA = data.DataReader("BWA",start=start, end=end,data_source='yahoo')
		BXP = data.DataReader("BXP",start=start, end=end,data_source='yahoo')
		BSX = data.DataReader("BSX",start=start, end=end,data_source='yahoo')
		BMY = data.DataReader("BMY",start=start, end=end,data_source='yahoo')
		AVGO = data.DataReader("AVGO",start=start, end=end,data_source='yahoo')
		BR = data.DataReader("BR",start=start, end=end,data_source='yahoo')
		BF.B = data.DataReader("BF.B",start=start, end=end,data_source='yahoo')
		CHRW = data.DataReader("CHRW",start=start, end=end,data_source='yahoo')
		COG = data.DataReader("COG",start=start, end=end,data_source='yahoo')
		CDNS = data.DataReader("CDNS",start=start, end=end,data_source='yahoo')
		CPB = data.DataReader("CPB",start=start, end=end,data_source='yahoo')
		COF = data.DataReader("COF",start=start, end=end,data_source='yahoo')
		CPRI = data.DataReader("CPRI",start=start, end=end,data_source='yahoo')
		CAH = data.DataReader("CAH",start=start, end=end,data_source='yahoo')
		KMX = data.DataReader("KMX",start=start, end=end,data_source='yahoo')
		CCL = data.DataReader("CCL",start=start, end=end,data_source='yahoo')
		CAT = data.DataReader("CAT",start=start, end=end,data_source='yahoo')
		CBOE = data.DataReader("CBOE",start=start, end=end,data_source='yahoo')
		CBRE = data.DataReader("CBRE",start=start, end=end,data_source='yahoo')
		CDW = data.DataReader("CDW",start=start, end=end,data_source='yahoo')
		CE = data.DataReader("CE",start=start, end=end,data_source='yahoo')
		CNC = data.DataReader("CNC",start=start, end=end,data_source='yahoo')
		CNP = data.DataReader("CNP",start=start, end=end,data_source='yahoo')
		CTL = data.DataReader("CTL",start=start, end=end,data_source='yahoo')
		CERN = data.DataReader("CERN",start=start, end=end,data_source='yahoo')
		CF = data.DataReader("CF",start=start, end=end,data_source='yahoo')
		SCHW = data.DataReader("SCHW",start=start, end=end,data_source='yahoo')
		CHTR = data.DataReader("CHTR",start=start, end=end,data_source='yahoo')
		CVX = data.DataReader("CVX",start=start, end=end,data_source='yahoo')
		CMG = data.DataReader("CMG",start=start, end=end,data_source='yahoo')
		CB = data.DataReader("CB",start=start, end=end,data_source='yahoo')
		CHD = data.DataReader("CHD",start=start, end=end,data_source='yahoo')
		CI = data.DataReader("CI",start=start, end=end,data_source='yahoo')
		XEC = data.DataReader("XEC",start=start, end=end,data_source='yahoo')
		CINF = data.DataReader("CINF",start=start, end=end,data_source='yahoo')
		CTAS = data.DataReader("CTAS",start=start, end=end,data_source='yahoo')
		CSCO = data.DataReader("CSCO",start=start, end=end,data_source='yahoo')
		C = data.DataReader("C",start=start, end=end,data_source='yahoo')
		CFG = data.DataReader("CFG",start=start, end=end,data_source='yahoo')
		CTXS = data.DataReader("CTXS",start=start, end=end,data_source='yahoo')
		CLX = data.DataReader("CLX",start=start, end=end,data_source='yahoo')
		CME = data.DataReader("CME",start=start, end=end,data_source='yahoo')
		CMS = data.DataReader("CMS",start=start, end=end,data_source='yahoo')
		KO = data.DataReader("KO",start=start, end=end,data_source='yahoo')
		CTSH = data.DataReader("CTSH",start=start, end=end,data_source='yahoo')
		CL = data.DataReader("CL",start=start, end=end,data_source='yahoo')
		CMCSA = data.DataReader("CMCSA",start=start, end=end,data_source='yahoo')
		CMA = data.DataReader("CMA",start=start, end=end,data_source='yahoo')
		CAG = data.DataReader("CAG",start=start, end=end,data_source='yahoo')
		CXO = data.DataReader("CXO",start=start, end=end,data_source='yahoo')
		COP = data.DataReader("COP",start=start, end=end,data_source='yahoo')
		ED = data.DataReader("ED",start=start, end=end,data_source='yahoo')
		STZ = data.DataReader("STZ",start=start, end=end,data_source='yahoo')
		COO = data.DataReader("COO",start=start, end=end,data_source='yahoo')
		CPRT = data.DataReader("CPRT",start=start, end=end,data_source='yahoo')
		GLW = data.DataReader("GLW",start=start, end=end,data_source='yahoo')
		CTVA = data.DataReader("CTVA",start=start, end=end,data_source='yahoo')
		COST = data.DataReader("COST",start=start, end=end,data_source='yahoo')
		COTY = data.DataReader("COTY",start=start, end=end,data_source='yahoo')
		CCI = data.DataReader("CCI",start=start, end=end,data_source='yahoo')
		CSX = data.DataReader("CSX",start=start, end=end,data_source='yahoo')
		CMI = data.DataReader("CMI",start=start, end=end,data_source='yahoo')
		CVS = data.DataReader("CVS",start=start, end=end,data_source='yahoo')
		DHI = data.DataReader("DHI",start=start, end=end,data_source='yahoo')
		DHR = data.DataReader("DHR",start=start, end=end,data_source='yahoo')
		DRI = data.DataReader("DRI",start=start, end=end,data_source='yahoo')
		DVA = data.DataReader("DVA",start=start, end=end,data_source='yahoo')
		DE = data.DataReader("DE",start=start, end=end,data_source='yahoo')
		DAL = data.DataReader("DAL",start=start, end=end,data_source='yahoo')
		XRAY = data.DataReader("XRAY",start=start, end=end,data_source='yahoo')
		DVN = data.DataReader("DVN",start=start, end=end,data_source='yahoo')
		FANG = data.DataReader("FANG",start=start, end=end,data_source='yahoo')
		DLR = data.DataReader("DLR",start=start, end=end,data_source='yahoo')
		DFS = data.DataReader("DFS",start=start, end=end,data_source='yahoo')
		DISCA = data.DataReader("DISCA",start=start, end=end,data_source='yahoo')
		DISCK = data.DataReader("DISCK",start=start, end=end,data_source='yahoo')
		DISH = data.DataReader("DISH",start=start, end=end,data_source='yahoo')
		DG = data.DataReader("DG",start=start, end=end,data_source='yahoo')
		DLTR = data.DataReader("DLTR",start=start, end=end,data_source='yahoo')
		D = data.DataReader("D",start=start, end=end,data_source='yahoo')
		DOV = data.DataReader("DOV",start=start, end=end,data_source='yahoo')
		DOW = data.DataReader("DOW",start=start, end=end,data_source='yahoo')
		DTE = data.DataReader("DTE",start=start, end=end,data_source='yahoo')
		DUK = data.DataReader("DUK",start=start, end=end,data_source='yahoo')
		DRE = data.DataReader("DRE",start=start, end=end,data_source='yahoo')
		DD = data.DataReader("DD",start=start, end=end,data_source='yahoo')
		DXC = data.DataReader("DXC",start=start, end=end,data_source='yahoo')
		ETFC = data.DataReader("ETFC",start=start, end=end,data_source='yahoo')
		EMN = data.DataReader("EMN",start=start, end=end,data_source='yahoo')
		ETN = data.DataReader("ETN",start=start, end=end,data_source='yahoo')
		EBAY = data.DataReader("EBAY",start=start, end=end,data_source='yahoo')
		ECL = data.DataReader("ECL",start=start, end=end,data_source='yahoo')
		EIX = data.DataReader("EIX",start=start, end=end,data_source='yahoo')
		EW = data.DataReader("EW",start=start, end=end,data_source='yahoo')
		EA = data.DataReader("EA",start=start, end=end,data_source='yahoo')
		EMR = data.DataReader("EMR",start=start, end=end,data_source='yahoo')
		ETR = data.DataReader("ETR",start=start, end=end,data_source='yahoo')
		EOG = data.DataReader("EOG",start=start, end=end,data_source='yahoo')
		EFX = data.DataReader("EFX",start=start, end=end,data_source='yahoo')
		EQIX = data.DataReader("EQIX",start=start, end=end,data_source='yahoo')
		EQR = data.DataReader("EQR",start=start, end=end,data_source='yahoo')
		ESS = data.DataReader("ESS",start=start, end=end,data_source='yahoo')
		EL = data.DataReader("EL",start=start, end=end,data_source='yahoo')
		EVRG = data.DataReader("EVRG",start=start, end=end,data_source='yahoo')
		ES = data.DataReader("ES",start=start, end=end,data_source='yahoo')
		RE = data.DataReader("RE",start=start, end=end,data_source='yahoo')
		EXC = data.DataReader("EXC",start=start, end=end,data_source='yahoo')
		EXPE = data.DataReader("EXPE",start=start, end=end,data_source='yahoo')
		EXPD = data.DataReader("EXPD",start=start, end=end,data_source='yahoo')
		EXR = data.DataReader("EXR",start=start, end=end,data_source='yahoo')
		XOM = data.DataReader("XOM",start=start, end=end,data_source='yahoo')
		FFIV = data.DataReader("FFIV",start=start, end=end,data_source='yahoo')
		FB = data.DataReader("FB",start=start, end=end,data_source='yahoo')
		FAST = data.DataReader("FAST",start=start, end=end,data_source='yahoo')
		FRT = data.DataReader("FRT",start=start, end=end,data_source='yahoo')
		FDX = data.DataReader("FDX",start=start, end=end,data_source='yahoo')
		FIS = data.DataReader("FIS",start=start, end=end,data_source='yahoo')
		FITB = data.DataReader("FITB",start=start, end=end,data_source='yahoo')
		FE = data.DataReader("FE",start=start, end=end,data_source='yahoo')
		FRC = data.DataReader("FRC",start=start, end=end,data_source='yahoo')
		FISV = data.DataReader("FISV",start=start, end=end,data_source='yahoo')
		FLT = data.DataReader("FLT",start=start, end=end,data_source='yahoo')
		FLIR = data.DataReader("FLIR",start=start, end=end,data_source='yahoo')
		FLS = data.DataReader("FLS",start=start, end=end,data_source='yahoo')
		FMC = data.DataReader("FMC",start=start, end=end,data_source='yahoo')
		F = data.DataReader("F",start=start, end=end,data_source='yahoo')
		FTNT = data.DataReader("FTNT",start=start, end=end,data_source='yahoo')
		FTV = data.DataReader("FTV",start=start, end=end,data_source='yahoo')
		FBHS = data.DataReader("FBHS",start=start, end=end,data_source='yahoo')
		FOXA = data.DataReader("FOXA",start=start, end=end,data_source='yahoo')
		FOX = data.DataReader("FOX",start=start, end=end,data_source='yahoo')
		BEN = data.DataReader("BEN",start=start, end=end,data_source='yahoo')
		FCX = data.DataReader("FCX",start=start, end=end,data_source='yahoo')
		GPS = data.DataReader("GPS",start=start, end=end,data_source='yahoo')
		GRMN = data.DataReader("GRMN",start=start, end=end,data_source='yahoo')
		IT = data.DataReader("IT",start=start, end=end,data_source='yahoo')
		GD = data.DataReader("GD",start=start, end=end,data_source='yahoo')
		GE = data.DataReader("GE",start=start, end=end,data_source='yahoo')
		GIS = data.DataReader("GIS",start=start, end=end,data_source='yahoo')
		GM = data.DataReader("GM",start=start, end=end,data_source='yahoo')
		GPC = data.DataReader("GPC",start=start, end=end,data_source='yahoo')
		GILD = data.DataReader("GILD",start=start, end=end,data_source='yahoo')
		GL = data.DataReader("GL",start=start, end=end,data_source='yahoo')
		GPN = data.DataReader("GPN",start=start, end=end,data_source='yahoo')
		GS = data.DataReader("GS",start=start, end=end,data_source='yahoo')
		GWW = data.DataReader("GWW",start=start, end=end,data_source='yahoo')
		HRB = data.DataReader("HRB",start=start, end=end,data_source='yahoo')
		HAL = data.DataReader("HAL",start=start, end=end,data_source='yahoo')
		HBI = data.DataReader("HBI",start=start, end=end,data_source='yahoo')
		HOG = data.DataReader("HOG",start=start, end=end,data_source='yahoo')
		HIG = data.DataReader("HIG",start=start, end=end,data_source='yahoo')
		HAS = data.DataReader("HAS",start=start, end=end,data_source='yahoo')
		HCA = data.DataReader("HCA",start=start, end=end,data_source='yahoo')
		PEAK = data.DataReader("PEAK",start=start, end=end,data_source='yahoo')
		HP = data.DataReader("HP",start=start, end=end,data_source='yahoo')
		HSIC = data.DataReader("HSIC",start=start, end=end,data_source='yahoo')
		HSY = data.DataReader("HSY",start=start, end=end,data_source='yahoo')
		HES = data.DataReader("HES",start=start, end=end,data_source='yahoo')
		HPE = data.DataReader("HPE",start=start, end=end,data_source='yahoo')
		HLT = data.DataReader("HLT",start=start, end=end,data_source='yahoo')
		HFC = data.DataReader("HFC",start=start, end=end,data_source='yahoo')
		HOLX = data.DataReader("HOLX",start=start, end=end,data_source='yahoo')
		HD = data.DataReader("HD",start=start, end=end,data_source='yahoo')
		HON = data.DataReader("HON",start=start, end=end,data_source='yahoo')
		HRL = data.DataReader("HRL",start=start, end=end,data_source='yahoo')
		HST = data.DataReader("HST",start=start, end=end,data_source='yahoo')
		HPQ = data.DataReader("HPQ",start=start, end=end,data_source='yahoo')
		HUM = data.DataReader("HUM",start=start, end=end,data_source='yahoo')
		HBAN = data.DataReader("HBAN",start=start, end=end,data_source='yahoo')
		HII = data.DataReader("HII",start=start, end=end,data_source='yahoo')
		IEX = data.DataReader("IEX",start=start, end=end,data_source='yahoo')
		IDXX = data.DataReader("IDXX",start=start, end=end,data_source='yahoo')
		INFO = data.DataReader("INFO",start=start, end=end,data_source='yahoo')
		ITW = data.DataReader("ITW",start=start, end=end,data_source='yahoo')
		ILMN = data.DataReader("ILMN",start=start, end=end,data_source='yahoo')
		IR = data.DataReader("IR",start=start, end=end,data_source='yahoo')
		INTC = data.DataReader("INTC",start=start, end=end,data_source='yahoo')
		ICE = data.DataReader("ICE",start=start, end=end,data_source='yahoo')
		IBM = data.DataReader("IBM",start=start, end=end,data_source='yahoo')
		INCY = data.DataReader("INCY",start=start, end=end,data_source='yahoo')
		IP = data.DataReader("IP",start=start, end=end,data_source='yahoo')
		IPG = data.DataReader("IPG",start=start, end=end,data_source='yahoo')
		IFF = data.DataReader("IFF",start=start, end=end,data_source='yahoo')
		INTU = data.DataReader("INTU",start=start, end=end,data_source='yahoo')
		ISRG = data.DataReader("ISRG",start=start, end=end,data_source='yahoo')
		IVZ = data.DataReader("IVZ",start=start, end=end,data_source='yahoo')
		IPGP = data.DataReader("IPGP",start=start, end=end,data_source='yahoo')
		IQV = data.DataReader("IQV",start=start, end=end,data_source='yahoo')
		IRM = data.DataReader("IRM",start=start, end=end,data_source='yahoo')
		JKHY = data.DataReader("JKHY",start=start, end=end,data_source='yahoo')
		J = data.DataReader("J",start=start, end=end,data_source='yahoo')
		JBHT = data.DataReader("JBHT",start=start, end=end,data_source='yahoo')
		SJM = data.DataReader("SJM",start=start, end=end,data_source='yahoo')
		JNJ = data.DataReader("JNJ",start=start, end=end,data_source='yahoo')
		JCI = data.DataReader("JCI",start=start, end=end,data_source='yahoo')
		JPM = data.DataReader("JPM",start=start, end=end,data_source='yahoo')
		JNPR = data.DataReader("JNPR",start=start, end=end,data_source='yahoo')
		KSU = data.DataReader("KSU",start=start, end=end,data_source='yahoo')
		K = data.DataReader("K",start=start, end=end,data_source='yahoo')
		KEY = data.DataReader("KEY",start=start, end=end,data_source='yahoo')
		KEYS = data.DataReader("KEYS",start=start, end=end,data_source='yahoo')
		KMB = data.DataReader("KMB",start=start, end=end,data_source='yahoo')
		KIM = data.DataReader("KIM",start=start, end=end,data_source='yahoo')
		KMI = data.DataReader("KMI",start=start, end=end,data_source='yahoo')
		KLAC = data.DataReader("KLAC",start=start, end=end,data_source='yahoo')
		KSS = data.DataReader("KSS",start=start, end=end,data_source='yahoo')
		KHC = data.DataReader("KHC",start=start, end=end,data_source='yahoo')
		KR = data.DataReader("KR",start=start, end=end,data_source='yahoo')
		LB = data.DataReader("LB",start=start, end=end,data_source='yahoo')
		LHX = data.DataReader("LHX",start=start, end=end,data_source='yahoo')
		LH = data.DataReader("LH",start=start, end=end,data_source='yahoo')
		LRCX = data.DataReader("LRCX",start=start, end=end,data_source='yahoo')
		LW = data.DataReader("LW",start=start, end=end,data_source='yahoo')
		LVS = data.DataReader("LVS",start=start, end=end,data_source='yahoo')
		LEG = data.DataReader("LEG",start=start, end=end,data_source='yahoo')
		LDOS = data.DataReader("LDOS",start=start, end=end,data_source='yahoo')
		LEN = data.DataReader("LEN",start=start, end=end,data_source='yahoo')
		LLY = data.DataReader("LLY",start=start, end=end,data_source='yahoo')
		LNC = data.DataReader("LNC",start=start, end=end,data_source='yahoo')
		LIN = data.DataReader("LIN",start=start, end=end,data_source='yahoo')
		LYV = data.DataReader("LYV",start=start, end=end,data_source='yahoo')
		LKQ = data.DataReader("LKQ",start=start, end=end,data_source='yahoo')
		LMT = data.DataReader("LMT",start=start, end=end,data_source='yahoo')
		L = data.DataReader("L",start=start, end=end,data_source='yahoo')
		LOW = data.DataReader("LOW",start=start, end=end,data_source='yahoo')
		LYB = data.DataReader("LYB",start=start, end=end,data_source='yahoo')
		MTB = data.DataReader("MTB",start=start, end=end,data_source='yahoo')
		M = data.DataReader("M",start=start, end=end,data_source='yahoo')
		MRO = data.DataReader("MRO",start=start, end=end,data_source='yahoo')
		MPC = data.DataReader("MPC",start=start, end=end,data_source='yahoo')
		MKTX = data.DataReader("MKTX",start=start, end=end,data_source='yahoo')
		MAR = data.DataReader("MAR",start=start, end=end,data_source='yahoo')
		MMC = data.DataReader("MMC",start=start, end=end,data_source='yahoo')
		MLM = data.DataReader("MLM",start=start, end=end,data_source='yahoo')
		MAS = data.DataReader("MAS",start=start, end=end,data_source='yahoo')
		MA = data.DataReader("MA",start=start, end=end,data_source='yahoo')
		MKC = data.DataReader("MKC",start=start, end=end,data_source='yahoo')
		MXIM = data.DataReader("MXIM",start=start, end=end,data_source='yahoo')
		MCD = data.DataReader("MCD",start=start, end=end,data_source='yahoo')
		MCK = data.DataReader("MCK",start=start, end=end,data_source='yahoo')
		MDT = data.DataReader("MDT",start=start, end=end,data_source='yahoo')
		MRK = data.DataReader("MRK",start=start, end=end,data_source='yahoo')
		MET = data.DataReader("MET",start=start, end=end,data_source='yahoo')
		MTD = data.DataReader("MTD",start=start, end=end,data_source='yahoo')
		MGM = data.DataReader("MGM",start=start, end=end,data_source='yahoo')
		MCHP = data.DataReader("MCHP",start=start, end=end,data_source='yahoo')
		MU = data.DataReader("MU",start=start, end=end,data_source='yahoo')
		MSFT = data.DataReader("MSFT",start=start, end=end,data_source='yahoo')
		MAA = data.DataReader("MAA",start=start, end=end,data_source='yahoo')
		MHK = data.DataReader("MHK",start=start, end=end,data_source='yahoo')
		TAP = data.DataReader("TAP",start=start, end=end,data_source='yahoo')
		MDLZ = data.DataReader("MDLZ",start=start, end=end,data_source='yahoo')
		MNST = data.DataReader("MNST",start=start, end=end,data_source='yahoo')
		MCO = data.DataReader("MCO",start=start, end=end,data_source='yahoo')
		MS = data.DataReader("MS",start=start, end=end,data_source='yahoo')
		MOS = data.DataReader("MOS",start=start, end=end,data_source='yahoo')
		MSI = data.DataReader("MSI",start=start, end=end,data_source='yahoo')
		MSCI = data.DataReader("MSCI",start=start, end=end,data_source='yahoo')
		MYL = data.DataReader("MYL",start=start, end=end,data_source='yahoo')
		NDAQ = data.DataReader("NDAQ",start=start, end=end,data_source='yahoo')
		NOV = data.DataReader("NOV",start=start, end=end,data_source='yahoo')
		NTAP = data.DataReader("NTAP",start=start, end=end,data_source='yahoo')
		NFLX = data.DataReader("NFLX",start=start, end=end,data_source='yahoo')
		NWL = data.DataReader("NWL",start=start, end=end,data_source='yahoo')
		NEM = data.DataReader("NEM",start=start, end=end,data_source='yahoo')
		NWSA = data.DataReader("NWSA",start=start, end=end,data_source='yahoo')
		NWS = data.DataReader("NWS",start=start, end=end,data_source='yahoo')
		NEE = data.DataReader("NEE",start=start, end=end,data_source='yahoo')
		NLSN = data.DataReader("NLSN",start=start, end=end,data_source='yahoo')
		NKE = data.DataReader("NKE",start=start, end=end,data_source='yahoo')
		NI = data.DataReader("NI",start=start, end=end,data_source='yahoo')
		NBL = data.DataReader("NBL",start=start, end=end,data_source='yahoo')
		JWN = data.DataReader("JWN",start=start, end=end,data_source='yahoo')
		NSC = data.DataReader("NSC",start=start, end=end,data_source='yahoo')
		NTRS = data.DataReader("NTRS",start=start, end=end,data_source='yahoo')
		NOC = data.DataReader("NOC",start=start, end=end,data_source='yahoo')
		NLOK = data.DataReader("NLOK",start=start, end=end,data_source='yahoo')
		NCLH = data.DataReader("NCLH",start=start, end=end,data_source='yahoo')
		NRG = data.DataReader("NRG",start=start, end=end,data_source='yahoo')
		NUE = data.DataReader("NUE",start=start, end=end,data_source='yahoo')
		NVDA = data.DataReader("NVDA",start=start, end=end,data_source='yahoo')
		NVR = data.DataReader("NVR",start=start, end=end,data_source='yahoo')
		ORLY = data.DataReader("ORLY",start=start, end=end,data_source='yahoo')
		OXY = data.DataReader("OXY",start=start, end=end,data_source='yahoo')
		ODFL = data.DataReader("ODFL",start=start, end=end,data_source='yahoo')
		OMC = data.DataReader("OMC",start=start, end=end,data_source='yahoo')
		OKE = data.DataReader("OKE",start=start, end=end,data_source='yahoo')
		ORCL = data.DataReader("ORCL",start=start, end=end,data_source='yahoo')
		PCAR = data.DataReader("PCAR",start=start, end=end,data_source='yahoo')
		PKG = data.DataReader("PKG",start=start, end=end,data_source='yahoo')
		PH = data.DataReader("PH",start=start, end=end,data_source='yahoo')
		PAYX = data.DataReader("PAYX",start=start, end=end,data_source='yahoo')
		PAYC = data.DataReader("PAYC",start=start, end=end,data_source='yahoo')
		PYPL = data.DataReader("PYPL",start=start, end=end,data_source='yahoo')
		PNR = data.DataReader("PNR",start=start, end=end,data_source='yahoo')
		PBCT = data.DataReader("PBCT",start=start, end=end,data_source='yahoo')
		PEP = data.DataReader("PEP",start=start, end=end,data_source='yahoo')
		PKI = data.DataReader("PKI",start=start, end=end,data_source='yahoo')
		PRGO = data.DataReader("PRGO",start=start, end=end,data_source='yahoo')
		PFE = data.DataReader("PFE",start=start, end=end,data_source='yahoo')
		PM = data.DataReader("PM",start=start, end=end,data_source='yahoo')
		PSX = data.DataReader("PSX",start=start, end=end,data_source='yahoo')
		PNW = data.DataReader("PNW",start=start, end=end,data_source='yahoo')
		PXD = data.DataReader("PXD",start=start, end=end,data_source='yahoo')
		PNC = data.DataReader("PNC",start=start, end=end,data_source='yahoo')
		PPG = data.DataReader("PPG",start=start, end=end,data_source='yahoo')
		PPL = data.DataReader("PPL",start=start, end=end,data_source='yahoo')
		PFG = data.DataReader("PFG",start=start, end=end,data_source='yahoo')
		PG = data.DataReader("PG",start=start, end=end,data_source='yahoo')
		PGR = data.DataReader("PGR",start=start, end=end,data_source='yahoo')
		PLD = data.DataReader("PLD",start=start, end=end,data_source='yahoo')
		PRU = data.DataReader("PRU",start=start, end=end,data_source='yahoo')
		PEG = data.DataReader("PEG",start=start, end=end,data_source='yahoo')
		PSA = data.DataReader("PSA",start=start, end=end,data_source='yahoo')
		PHM = data.DataReader("PHM",start=start, end=end,data_source='yahoo')
		PVH = data.DataReader("PVH",start=start, end=end,data_source='yahoo')
		QRVO = data.DataReader("QRVO",start=start, end=end,data_source='yahoo')
		PWR = data.DataReader("PWR",start=start, end=end,data_source='yahoo')
		QCOM = data.DataReader("QCOM",start=start, end=end,data_source='yahoo')
		DGX = data.DataReader("DGX",start=start, end=end,data_source='yahoo')
		RL = data.DataReader("RL",start=start, end=end,data_source='yahoo')
		RJF = data.DataReader("RJF",start=start, end=end,data_source='yahoo')
		RTN = data.DataReader("RTN",start=start, end=end,data_source='yahoo')
		O = data.DataReader("O",start=start, end=end,data_source='yahoo')
		REG = data.DataReader("REG",start=start, end=end,data_source='yahoo')
		REGN = data.DataReader("REGN",start=start, end=end,data_source='yahoo')
		RF = data.DataReader("RF",start=start, end=end,data_source='yahoo')
		RSG = data.DataReader("RSG",start=start, end=end,data_source='yahoo')
		RMD = data.DataReader("RMD",start=start, end=end,data_source='yahoo')
		RHI = data.DataReader("RHI",start=start, end=end,data_source='yahoo')
		ROK = data.DataReader("ROK",start=start, end=end,data_source='yahoo')
		ROL = data.DataReader("ROL",start=start, end=end,data_source='yahoo')
		ROP = data.DataReader("ROP",start=start, end=end,data_source='yahoo')
		ROST = data.DataReader("ROST",start=start, end=end,data_source='yahoo')
		RCL = data.DataReader("RCL",start=start, end=end,data_source='yahoo')
		SPGI = data.DataReader("SPGI",start=start, end=end,data_source='yahoo')
		CRM = data.DataReader("CRM",start=start, end=end,data_source='yahoo')
		SBAC = data.DataReader("SBAC",start=start, end=end,data_source='yahoo')
		SLB = data.DataReader("SLB",start=start, end=end,data_source='yahoo')
		STX = data.DataReader("STX",start=start, end=end,data_source='yahoo')
		SEE = data.DataReader("SEE",start=start, end=end,data_source='yahoo')
		SRE = data.DataReader("SRE",start=start, end=end,data_source='yahoo')
		NOW = data.DataReader("NOW",start=start, end=end,data_source='yahoo')
		SHW = data.DataReader("SHW",start=start, end=end,data_source='yahoo')
		SPG = data.DataReader("SPG",start=start, end=end,data_source='yahoo')
		SWKS = data.DataReader("SWKS",start=start, end=end,data_source='yahoo')
		SLG = data.DataReader("SLG",start=start, end=end,data_source='yahoo')
		SNA = data.DataReader("SNA",start=start, end=end,data_source='yahoo')
		SO = data.DataReader("SO",start=start, end=end,data_source='yahoo')
		LUV = data.DataReader("LUV",start=start, end=end,data_source='yahoo')
		SWK = data.DataReader("SWK",start=start, end=end,data_source='yahoo')
		SBUX = data.DataReader("SBUX",start=start, end=end,data_source='yahoo')
		STT = data.DataReader("STT",start=start, end=end,data_source='yahoo')
		STE = data.DataReader("STE",start=start, end=end,data_source='yahoo')
		SYK = data.DataReader("SYK",start=start, end=end,data_source='yahoo')
		SIVB = data.DataReader("SIVB",start=start, end=end,data_source='yahoo')
		SYF = data.DataReader("SYF",start=start, end=end,data_source='yahoo')
		SNPS = data.DataReader("SNPS",start=start, end=end,data_source='yahoo')
		SYY = data.DataReader("SYY",start=start, end=end,data_source='yahoo')
		TMUS = data.DataReader("TMUS",start=start, end=end,data_source='yahoo')
		TROW = data.DataReader("TROW",start=start, end=end,data_source='yahoo')
		TTWO = data.DataReader("TTWO",start=start, end=end,data_source='yahoo')
		TPR = data.DataReader("TPR",start=start, end=end,data_source='yahoo')
		TGT = data.DataReader("TGT",start=start, end=end,data_source='yahoo')
		TEL = data.DataReader("TEL",start=start, end=end,data_source='yahoo')
		FTI = data.DataReader("FTI",start=start, end=end,data_source='yahoo')
		TFX = data.DataReader("TFX",start=start, end=end,data_source='yahoo')
		TXN = data.DataReader("TXN",start=start, end=end,data_source='yahoo')
		TXT = data.DataReader("TXT",start=start, end=end,data_source='yahoo')
		TMO = data.DataReader("TMO",start=start, end=end,data_source='yahoo')
		TIF = data.DataReader("TIF",start=start, end=end,data_source='yahoo')
		TJX = data.DataReader("TJX",start=start, end=end,data_source='yahoo')
		TSCO = data.DataReader("TSCO",start=start, end=end,data_source='yahoo')
		TDG = data.DataReader("TDG",start=start, end=end,data_source='yahoo')
		TRV = data.DataReader("TRV",start=start, end=end,data_source='yahoo')
		TFC = data.DataReader("TFC",start=start, end=end,data_source='yahoo')
		TWTR = data.DataReader("TWTR",start=start, end=end,data_source='yahoo')
		TSN = data.DataReader("TSN",start=start, end=end,data_source='yahoo')
		UDR = data.DataReader("UDR",start=start, end=end,data_source='yahoo')
		ULTA = data.DataReader("ULTA",start=start, end=end,data_source='yahoo')
		USB = data.DataReader("USB",start=start, end=end,data_source='yahoo')
		UAA = data.DataReader("UAA",start=start, end=end,data_source='yahoo')
		UA = data.DataReader("UA",start=start, end=end,data_source='yahoo')
		UNP = data.DataReader("UNP",start=start, end=end,data_source='yahoo')
		UAL = data.DataReader("UAL",start=start, end=end,data_source='yahoo')
		UNH = data.DataReader("UNH",start=start, end=end,data_source='yahoo')
		UPS = data.DataReader("UPS",start=start, end=end,data_source='yahoo')
		URI = data.DataReader("URI",start=start, end=end,data_source='yahoo')
		UTX = data.DataReader("UTX",start=start, end=end,data_source='yahoo')
		UHS = data.DataReader("UHS",start=start, end=end,data_source='yahoo')
		UNM = data.DataReader("UNM",start=start, end=end,data_source='yahoo')
		VFC = data.DataReader("VFC",start=start, end=end,data_source='yahoo')
		VLO = data.DataReader("VLO",start=start, end=end,data_source='yahoo')
		VAR = data.DataReader("VAR",start=start, end=end,data_source='yahoo')
		VTR = data.DataReader("VTR",start=start, end=end,data_source='yahoo')
		VRSN = data.DataReader("VRSN",start=start, end=end,data_source='yahoo')
		VRSK = data.DataReader("VRSK",start=start, end=end,data_source='yahoo')
		VZ = data.DataReader("VZ",start=start, end=end,data_source='yahoo')
		VRTX = data.DataReader("VRTX",start=start, end=end,data_source='yahoo')
		VIAC = data.DataReader("VIAC",start=start, end=end,data_source='yahoo')
		V = data.DataReader("V",start=start, end=end,data_source='yahoo')
		VNO = data.DataReader("VNO",start=start, end=end,data_source='yahoo')
		VMC = data.DataReader("VMC",start=start, end=end,data_source='yahoo')
		WRB = data.DataReader("WRB",start=start, end=end,data_source='yahoo')
		WAB = data.DataReader("WAB",start=start, end=end,data_source='yahoo')
		WMT = data.DataReader("WMT",start=start, end=end,data_source='yahoo')
		WBA = data.DataReader("WBA",start=start, end=end,data_source='yahoo')
		DIS = data.DataReader("DIS",start=start, end=end,data_source='yahoo')
		WM = data.DataReader("WM",start=start, end=end,data_source='yahoo')
		WAT = data.DataReader("WAT",start=start, end=end,data_source='yahoo')
		WEC = data.DataReader("WEC",start=start, end=end,data_source='yahoo')
		WFC = data.DataReader("WFC",start=start, end=end,data_source='yahoo')
		WELL = data.DataReader("WELL",start=start, end=end,data_source='yahoo')
		WDC = data.DataReader("WDC",start=start, end=end,data_source='yahoo')
		WU = data.DataReader("WU",start=start, end=end,data_source='yahoo')
		WRK = data.DataReader("WRK",start=start, end=end,data_source='yahoo')
		WY = data.DataReader("WY",start=start, end=end,data_source='yahoo')
		WHR = data.DataReader("WHR",start=start, end=end,data_source='yahoo')
		WMB = data.DataReader("WMB",start=start, end=end,data_source='yahoo')
		WLTW = data.DataReader("WLTW",start=start, end=end,data_source='yahoo')
		WYNN = data.DataReader("WYNN",start=start, end=end,data_source='yahoo')
		XEL = data.DataReader("XEL",start=start, end=end,data_source='yahoo')
		XRX = data.DataReader("XRX",start=start, end=end,data_source='yahoo')
		XLNX = data.DataReader("XLNX",start=start, end=end,data_source='yahoo')
		XYL = data.DataReader("XYL",start=start, end=end,data_source='yahoo')
		YUM = data.DataReader("YUM",start=start, end=end,data_source='yahoo')
		ZBRA = data.DataReader("ZBRA",start=start, end=end,data_source='yahoo')
		ZBH = data.DataReader("ZBH",start=start, end=end,data_source='yahoo')
		ZION = data.DataReader("ZION",start=start, end=end,data_source='yahoo')
		ZTS = data.DataReader("ZTS",start=start, end=end,data_source='yahoo')
		return 