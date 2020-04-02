start = "2000-01-01"
end = "2020-03-01"


from sqlalchemy import create_engine
engine = create_engine('mssql://DESKTOP-C3PKM76\\SQLEXPRESS01/StockSniper?trusted_connection=yes&driver=ODBC+Driver+13+for+SQL+Server')
con = engine.connect()
