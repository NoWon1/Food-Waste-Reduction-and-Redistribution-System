from sqlalchemy import create_engine
import pandas as pd
from urllib.parse import quote_plus

try:
    
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': quote_plus('Aditya@06'),  
        'database': 'food'
    }

    
    connection_str = f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}"
    
    
    engine = create_engine(connection_str)
    
    
    with engine.connect() as connection:
        
        query = 'SELECT * FROM Recipient'
        data = pd.read_sql(query, con=engine)
        
        
        print("Fetched data from Recipient table:")
        print(f"Total rows in Recipient table: {len(data)}")
        print(data)

except Exception as e:
    print(f"Error connecting to database: {str(e)}")
    print("Please verify:")
    print("1. MySQL server is running")
    print("2. Database credentials are correct")
    print("3. Database 'food' exists")