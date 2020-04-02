def GetCompanies():
    from sqlalchemy import create_engine
    import pandas as pd
    engine = create_engine('mssql://DESKTOP-C3PKM76\\SQLEXPRESS01/StockSniper?trusted_connection=yes&driver=ODBC+Driver+13+for+SQL+Server')
    con = engine.connect()    
    sql = """
    SELECT * FROM Companies
    """
    _ = (pd.read_sql(sql,con))
    con.close()

    return _.set_index('Symbol')