from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Aditya@06',
    'database': 'food'
}

@app.route('/insert_data', methods=['POST'])
def insert_data():
    try:
        # Get JSON data from the request
        data = request.json
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # SQL Query to insert data
        query = """
            INSERT INTO recipient (Email_ID, Recipient_ID, NGO_name, Phone_number, Address, City, State, Pincode, Quantity_required_in_grams, Redistribution_time_span_in_hours)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            data['Email_ID'], data['Recipient_ID'], data['NGO_name'], 
            data['Phone_number'], data['Address'], data['City'], 
            data['State'], data['Pincode'], data['Quantity_required_in_grams'], 
            data['Redistribution_time_span_in_hours']
        )
        cursor.execute(query, values)
        connection.commit()

        return jsonify({'message': 'Data inserted successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        connection.close()

if __name__ == '_main_':
    app.run(debug=True)
