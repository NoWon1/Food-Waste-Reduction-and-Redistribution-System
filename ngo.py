import mysql.connector
from sqlalchemy import create_engine
import pandas as pd
from tabulate import tabulate

# Correct database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Aditya@06',
    'database': 'food',
    'auth_plugin': 'mysql_native_password'
}

def main():
    try:
        # Direct MySQL connection
        connection = mysql.connector.connect(**db_config)
        
        # SQLAlchemy connection
        engine = create_engine(
            f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}"
        )

        def test_connection():
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT 1")
                print("Database connection successful!")
                cursor.close()
            except Exception as e:
                print(f"Database connection failed: {e}")

        def add():
            try:
                print("\nEnter NGO Details:")
                email = input("Email ID: ")
                ngo_id = input("NGO ID: ")
                ngo_name = input("NGO Name: ")
                phone = input("Phone Number: ")
                address = input("Address: ")
                city = input("City: ")
                state = input("State: ")
                pincode = input("Pincode: ")
                quantity = input("Quantity Required (in grams): ")
                timespan = input("Redistribution Timespan (in hours): ")

                cursor = connection.cursor()
                query = """
                    INSERT INTO Recipient (
                        Email_ID, Recipient_ID, NGO_name, Phone_number,
                        Address, City, State, Pincode,
                        Quantity_required_in_grams,
                        Redistribution_time_span_in_hours
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                values = (email, ngo_id, ngo_name, phone, address, city, 
                         state, pincode, quantity, timespan)
                
                cursor.execute(query, values)
                connection.commit()
                print("NGO added successfully!")
                cursor.close()
            except Exception as e:
                print(f"Error adding NGO: {e}")

        def search_donors():
            try:
                state = input("Enter the State where your NGO is located: ")
                city = input("Enter the City where your NGO is located: ")
                
                query = """
                    SELECT Donor_ID, Name, Phone_number, Address, 
                           Quantity_in_grams, Time_span_in_hours 
                    FROM Donor 
                    WHERE State = %s AND City = %s
                """
                
                df = pd.read_sql_query(query, engine, params=(state, city))
                
                if not df.empty:
                    print("\nAvailable Donors:")
                    print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))
                else:
                    print("No donors found in the specified location.")
                    
            except Exception as e:
                print(f"Error while fetching donor data: {e}")

        while True:
            print("\nNGO Management System")
            print("1. Test Connection")
            print("2. Add NGO")
            print("3. Search Donors")
            print("4. Exit")
            
            choice = input("Enter your choice (1-4): ")
            
            if choice == '1':
                test_connection()
            elif choice == '2':
                add()
            elif choice == '3':
                search_donors()
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    except Exception as e:
        print(f"Application error: {e}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    main()