import mysql.connector
from mysql.connector import Error


db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Aditya@06',
    'database': 'food',
    'auth_plugin': 'mysql_native_password'  
}

def connect_to_database():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def get_ngos():
    connection = connect_to_database()
    if not connection:
        return
    
    try:
        cursor = connection.cursor()
        query = "SELECT DISTINCT NGO_name FROM Recipient"
        cursor.execute(query)
        ngos = cursor.fetchall()
        
        print("List of NGOs in the database:")
        for ngo in ngos:
            print(f"- {ngo[0]}")
            
    except Error as e:
        print(f"Error fetching NGOs: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    get_ngos()