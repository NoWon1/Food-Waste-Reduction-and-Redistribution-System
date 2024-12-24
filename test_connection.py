from sqlalchemy import create_engine
import pymysql
from urllib.parse import quote_plus


db_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'Aditya@06',
    'database': 'food'
}


encoded_password = quote_plus(db_config['password'])

try:
    
    conn = pymysql.connect(**db_config)
    print("Basic MySQL connection successful!")
    conn.close()

    
    connection_str = (
        f"mysql+pymysql://{db_config['user']}:{encoded_password}"
        f"@{db_config['host']}:{db_config['port']}/{db_config['database']}"
    )
    engine = create_engine(connection_str)
    
    with engine.connect() as connection:
        print("SQLAlchemy connection successful!")
        
except Exception as e:
    print(f"Connection error: {str(e)}")
    print(f"Connection string: {connection_str}")