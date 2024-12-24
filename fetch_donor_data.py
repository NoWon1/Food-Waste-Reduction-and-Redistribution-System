from sqlalchemy import create_engine
import pandas as pd
from urllib.parse import quote_plus
import sys


db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Aditya@06',
    'database': 'food'
}

try:
    
    conn_str = f"mysql+pymysql://{db_config['user']}:{quote_plus(db_config['password'])}@{db_config['host']}/{db_config['database']}"
    engine = create_engine(conn_str)

    
    with engine.connect() as connection:
        
        query = 'SELECT * FROM Donor'
        data = pd.read_sql(query, con=engine)
        
        
        print("Fetched data from Donor table:")
        print(data.head())

except Exception as e:
    print(f"Error connecting to database: {str(e)}")
    sys.exit(1)