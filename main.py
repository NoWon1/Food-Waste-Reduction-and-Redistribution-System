import predict as pred
import route
import waste_detect as detect
import waste_graph as gr
import nutri as n
import ngo
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine


DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Aditya@06',
    'database': 'food',
    'auth_plugin': 'mysql_native_password'
}

def connect_to_database():
    """Establish database connection using mysql.connector"""
    try:
        connection = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            database=DB_CONFIG['database'],
            auth_plugin=DB_CONFIG['auth_plugin']
        )
        print("Database connected successfully")
        return connection
    except mysql.connector.Error as err:
        print(f"Database connection failed: {err}")
        return None

def main():
    
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            
            engine = create_engine(f"mysql+mysqlconnector://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}/{DB_CONFIG['database']}")
            
            
            
            cursor.close()
            connection.close()
        except Exception as e:
            print(f"Error during database operations: {e}")
    else:
        print("Using sample data instead...")
        

if __name__ == "__main__":
    main()