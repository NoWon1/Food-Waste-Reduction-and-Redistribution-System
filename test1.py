from sqlalchemy import create_engine
import pandas as pd
from urllib.parse import quote_plus  


db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Aditya@06',  
    'database': 'food'        
}


password = quote_plus(db_config['password'])
connection_str = f"mysql+pymysql://{db_config['user']}:{password}@{db_config['host']}/{db_config['database']}"

try:
    
    engine = create_engine(connection_str)
    
    
    with engine.connect() as conn:
        
        query = 'SELECT * FROM surplus'
        data = pd.read_sql(query, con=engine)

        
        if 'waste_in_grams' in data.columns:
            
            threshold = data['waste_in_grams'].median()
            
            
            data['waste_category'] = data['waste_in_grams'].apply(
                lambda x: 'High' if x > threshold else 'Low'
            )

            
            print(data['waste_category'].value_counts())
        else:
            print("The 'waste_in_grams' column does not exist in the surplus table.")

except Exception as e:
    print(f"Error connecting to database: {str(e)}")
    print("Please verify:")
    print("1. MySQL server is running")
    print("2. Database credentials are correct")
    print("3. Database 'food' exists")