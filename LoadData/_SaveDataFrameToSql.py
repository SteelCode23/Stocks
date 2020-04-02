def SaveDataFrameToSql(test, table_name):
    from sqlalchemy import create_engine
    import pandas as pd
    engine = create_engine('mssql://DESKTOP-C3PKM76\\SQLEXPRESS01/StockSniper?trusted_connection=yes&driver=ODBC+Driver+13+for+SQL+Server')
    con = engine.connect()
    test['RecordDate'] = pd.datetime.today()
    test.reset_index().to_sql(table_name,con=engine, if_exists = 'append', index=False)
    con.close()
    