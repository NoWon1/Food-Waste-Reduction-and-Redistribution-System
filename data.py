import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Aditya@06',
    'database': 'food',  # Replace with your database name
}

# Connect to the database
connection = mysql.connector.connect(**db_config)
if connection.is_connected():
    print("Connected to MySQL database")


query="""INSERT INTO Recipient(Email_ID,Recipient_ID,
NGO_name,Phone_number,Address,City,State,Pincode,
Quantity_required_in_grams,Redistribution_time_span_in_hours)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

new_rows_data = [
    (41, 'Gravy food', 41, 'butter chicken', 750, '2023-11-05', '2023-10-25',
     'Chicken,Butter,Heavy Cream,Tomato Sauce,Spices', 5,
     'Contains dairy dietary', 'Non-Vegetarian', 'store in cold place', 'Available', 36),
    (42, 'Rice', 42, 'saffron rice', 600, '2023-11-08', '2023-10-30',
     'Basmati Rice,Saffron Threads,Onions,Ghee,Spices', 5,
     'None', 'Vegetarian', 'store in dry place', 'Available', 16),
    (43, 'Pasta', 43, 'carbonara', 450, '2023-11-12', '2023-11-01',
     'Spaghetti,Heavy Cream,Eggs,Bacon,Parmesan Cheese,Black Pepper', 6,
     'Contains dairy dietary', 'Non-Vegetarian', 'keep refrigerated', 'Available', 20),
    (44, 'Seafood', 44, 'grilled shrimp', 550, '2023-11-18', '2023-11-10',
     'Shrimp,Garlic,Butter,Lemon Juice,Parsley', 5,
     'None', 'Non-Vegetarian', 'store in cold place', 'Available', 15),
    (45, 'Salad', 45, 'Greek salad', 400, '2023-11-22', '2023-11-15',
     'Cucumber,Tomato,Olives,Feta Cheese,Olive Oil', 5,
     'None', 'Vegetarian', 'keep refrigerated', 'Available', 10),
    (46, 'Rice', 46, 'fried rice', 800, '2023-11-28', '2023-11-20',
     'Rice,Shrimp,Peas,Carrots,Eggs,Soy Sauce', 6,
     'None', 'Non-Vegetarian', 'store in cold place', 'Available', 30),
    (47, 'Pasta', 47, 'alfredo pasta', 500, '2023-12-02', '2023-11-25',
     'Fettuccine Pasta,Heavy Cream,Butter,Parmesan Cheese,Garlic', 5,
     'Contains dairy dietary', 'Non-Vegetarian', 'keep refrigerated', 'Available', 22),
    (48, 'Gravy food', 48, 'beef stew', 700, '2023-12-08', '2023-12-01',
     'Beef,Carrots,Potatoes,Onions,Beef Broth,Flour', 6,
     'None', 'Non-Vegetarian', 'store in cold place', 'Available', 25),
    (49, 'Dry food', 49, 'couscous salad', 350, '2023-12-12', '2023-12-05',
     'Couscous,Cherry Tomatoes,Cucumbers,Parsley,Red Onion', 5,
     'None', 'Vegetarian', 'store in dry place', 'Available', 10),
    (50, 'Salad', 50, 'spinach salad', 450, '2023-12-18', '2023-12-10',
     'Baby Spinach,Strawberries,Goat Cheese,Walnuts,Balsamic Vinaigrette', 5,
     'Contains nuts', 'Vegetarian', 'keep refrigerated', 'Available', 18),
    (51, 'Pasta', 51, 'lasagna', 600, '2023-12-22', '2023-12-15',
     'Lasagna Noodles,Ground Beef,Ricotta Cheese,Mozzarella Cheese,Tomato Sauce', 6,
     'Contains dairy dietary', 'Non-Vegetarian', 'keep refrigerated', 'Available', 32),
    (52, 'Rice', 52, 'mushroom rice', 500, '2023-12-28', '2023-12-20',
     'Rice,Mushrooms,Onions,Chicken Broth,Butter', 5,
     'Contains dairy dietary', 'Non-Vegetarian', 'keep refrigerated', 'Available', 14),
    (53, 'Gravy food', 53, 'lamb curry', 750, '2024-01-02', '2023-12-25',
     'Lamb,Onions,Tomatoes,Garlic,Ginger,Spices', 6,
     'None', 'Non-Vegetarian', 'store in cold place', 'Available', 38),
    (54, 'Chicken', 54, 'chicken curry', 700, '2024-01-08', '2024-01-01',
     'Chicken,Onions,Tomatoes,Garlic,Ginger,Spices', 6,
     'None', 'Non-Vegetarian', 'store in cold place', 'Available', 35),
    (55, 'Salad', 55, 'fruit salad', 600, '2024-01-12', '2024-01-05',
     'Apple,Banana,Orange,Grapes,Honey,Nuts', 6,
     'None', 'Vegetarian', 'keep refrigerated', 'Available', 28),
    (56, 'Rice', 56, 'sushi rice', 450, '2024-01-18', '2024-01-10',
     'Sushi Rice,Rice Vinegar,Sugar,Salt', 4,
     'None', 'Vegetarian', 'store in dry place', 'Available', 12),
    (57, 'Pasta', 57, 'mac and cheese', 500, '2024-01-22', '2024-01-15',
     'Elbow Macaroni,Cheddar Cheese,Butter,Flour,Milk', 5,
     'Contains dairy dietary', 'Vegetarian', 'keep refrigerated', 'Available', 22),
    (58, 'Gravy food', 58, 'beef stroganoff', 750, '2024-01-28', '2024-01-20',
     'Beef,Onions,Mushrooms,Beef Broth,Sour Cream', 5,
     'Contains dairy dietary', 'Non-Vegetarian', 'keep refrigerated', 'Available', 30),
    (59, 'Rice', 59, 'jambalaya', 600, '2024-02-02', '2024-01-25',
     'Rice,Chicken,Shrimp,Andouille Sausage,Onions,Celery,Bell Peppers', 7,
     'None', 'Non-Vegetarian', 'store in cold place', 'Available', 45),
    (60, 'Pasta', 60, 'ravioli', 400, '2024-02-08', '2024-02-01',
     'Ravioli (Cheese Filling),Marinara Sauce,Parmesan Cheese', 4,
     'Contains dairy dietary', 'Vegetarian', 'keep refrigerated', 'Available', 18),
]



# Create a cursor to execute SQL statements
cursor = connection.cursor()

# SQL statement to insert rows
insert_query = """
INSERT INTO Surplus (Food_id, food_type, donor_id, food_name, quantity_in_grams, Expiry_Date, Packaging_Date, ingredients, ingredient_count, Allergen_Info, Dietary_Info, storage_remarks, status, waste_in_grams)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

try:
    # Insert the new rows into the table
    cursor.executemany(insert_query, new_rows_data)

    # Commit the changes
    connection.commit()
    print(f"Inserted {len(new_rows_data)} rows successfully.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    # Rollback the transaction if an error occurs
    connection.rollback()
finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()


'''
# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '@MYsql23!',
    'database': 'Food',  # Replace with your database name
}

# Connect to the database
connection = mysql.connector.connect(**db_config)

if connection.is_connected():
    print("Connected to MySQL database")

# Define the data for the 25 new rows (modify as needed)
# Define the data for the 25 new rows (modify as needed)
# Additional rows of data starting from the 41st row
new_rows_data = [
    (41, 'Gravy food', 41, 'butter chicken', 750, '2023-11-05', '2023-10-25',
     'Chicken,Butter,Heavy Cream,Tomato Sauce,Spices', 5,
     'Contains dairy dietary', 'Non-Vegetarian', 'store in cold place', 'Available', 36),
    (42, 'Rice', 42, 'saffron rice', 600, '2023-11-08', '2023-10-30',
     'Basmati Rice,Saffron Threads,Onions,Ghee,Spices', 5,
     'None', 'Vegetarian', 'store in dry place', 'Available', 16),
    (43, 'Pasta', 43, 'carbonara', 450, '2023-11-12', '2023-11-01',
     'Spaghetti,Heavy Cream,Eggs,Bacon,Parmesan Cheese,Black Pepper', 6,
     'Contains dairy dietary', 'Non-Vegetarian', 'keep refrigerated', 'Available', 20),
    (44, 'Seafood', 44, 'grilled shrimp', 550, '2023-11-18', '2023-11-10',
     'Shrimp,Garlic,Butter,Lemon Juice,Parsley', 5,
     'None', 'Non-Vegetarian', 'store in cold place', 'Available', 15),
    (45, 'Salad', 45, 'Greek salad', 400, '2023-11-22', '2023-11-15',
     'Cucumber,Tomato,Olives,Feta Cheese,Olive Oil', 5,
     'None', 'Vegetarian', 'keep refrigerated', 'Available', 10),
    (46, 'Rice', 46, 'fried rice', 800, '2023-11-28', '2023-11-20',
     'Rice,Shrimp,Peas,Carrots,Eggs,Soy Sauce', 6,
     'None', 'Non-Vegetarian', 'store in cold place', 'Available', 30),
    (47, 'Pasta', 47, 'alfredo pasta', 500, '2023-12-02', '2023-11-25',
     'Fettuccine Pasta,Heavy Cream,Butter,Parmesan Cheese,Garlic', 5,
     'Contains dairy dietary', 'Non-Vegetarian', 'keep refrigerated', 'Available', 22),
    (48, 'Gravy food', 48, 'beef stew', 700, '2023-12-08', '2023-12-01',
     'Beef,Carrots,Potatoes,Onions,Beef Broth,Flour', 6,
     'None', 'Non-Vegetarian', 'store in cold place', 'Available', 25),
    (49, 'Dry food', 49, 'couscous salad', 350, '2023-12-12', '2023-12-05',
     'Couscous,Cherry Tomatoes,Cucumbers,Parsley,Red Onion', 5,
     'None', 'Vegetarian', 'store in dry place', 'Available', 10),
    (50, 'Salad', 50, 'spinach salad', 450, '2023-12-18', '2023-12-10',
     'Baby Spinach,Strawberries,Goat Cheese,Walnuts,Balsamic Vinaigrette', 5,
     'Contains nuts', 'Vegetarian', 'keep refrigerated', 'Available', 18),
    (51, 'Pasta', 51, 'lasagna', 600, '2023-12-22', '2023-12-15',
     'Lasagna Noodles,Ground Beef,Ricotta Cheese,Mozzarella Cheese,Tomato Sauce', 6,
     'Contains dairy dietary', 'Non-Vegetarian', 'keep refrigerated', 'Available', 32),
    (52, 'Rice', 52, 'mushroom rice', 500, '2023-12-28', '2023-12-20',
     'Rice,Mushrooms,Onions,Chicken Broth,Butter', 5,
     'Contains dairy dietary', 'Non-Vegetarian', 'keep refrigerated', 'Available', 14),
    (53, 'Gravy food', 53, 'lamb curry', 750, '2024-01-02', '2023-12-25',
     'Lamb,Onions,Tomatoes,Garlic,Ginger,Spices', 6,
     'None', 'Non-Vegetarian', 'store in cold place', 'Available', 38),
    (54, 'Chicken', 54, 'chicken curry', 700, '2024-01-08', '2024-01-01',
     'Chicken,Onions,Tomatoes,Garlic,Ginger,Spices', 6,
     'None', 'Non-Vegetarian', 'store in cold place', 'Available', 35),
    (55, 'Salad', 55, 'fruit salad', 600, '2024-01-12', '2024-01-05',
     'Apple,Banana,Orange,Grapes,Honey,Nuts', 6,
     'None', 'Vegetarian', 'keep refrigerated', 'Available', 28),
    (56, 'Rice', 56, 'sushi rice', 450, '2024-01-18', '2024-01-10',
     'Sushi Rice,Rice Vinegar,Sugar,Salt', 4,
     'None', 'Vegetarian', 'store in dry place', 'Available', 12),
    (57, 'Pasta', 57, 'mac and cheese', 500, '2024-01-22', '2024-01-15',
     'Elbow Macaroni,Cheddar Cheese,Butter,Flour,Milk', 5,
     'Contains dairy dietary', 'Vegetarian', 'keep refrigerated', 'Available', 22),
    (58, 'Gravy food', 58, 'beef stroganoff', 750, '2024-01-28', '2024-01-20',
     'Beef,Onions,Mushrooms,Beef Broth,Sour Cream', 5,
     'Contains dairy dietary', 'Non-Vegetarian', 'keep refrigerated', 'Available', 30),
    (59, 'Rice', 59, 'jambalaya', 600, '2024-02-02', '2024-01-25',
     'Rice,Chicken,Shrimp,Andouille Sausage,Onions,Celery,Bell Peppers', 7,
     'None', 'Non-Vegetarian', 'store in cold place', 'Available', 45),
    (60, 'Pasta', 60, 'ravioli', 400, '2024-02-08', '2024-02-01',
     'Ravioli (Cheese Filling),Marinara Sauce,Parmesan Cheese', 4,
     'Contains dairy dietary', 'Vegetarian', 'keep refrigerated', 'Available', 18),
]



# Create a cursor to execute SQL statements
cursor = connection.cursor()

# SQL statement to insert rows
insert_query = """
INSERT INTO Surplus (Food_id, food_type, donor_id, food_name, quantity_in_grams, Expiry_Date, Packaging_Date, ingredients, ingredient_count, Allergen_Info, Dietary_Info, storage_remarks, status, waste_in_grams)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

try:
    # Insert the new rows into the table
    cursor.executemany(insert_query, new_rows_data)

    # Commit the changes
    connection.commit()
    print(f"Inserted {len(new_rows_data)} rows successfully.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    # Rollback the transaction if an error occurs
    connection.rollback()
finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()
'''