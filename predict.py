import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import mysql.connector
from sklearn.metrics import classification_report

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'database': 'food',
    'user': 'root',
    'password': 'Aditya@06',
    'auth_plugin': 'mysql_native_password'
}

def load_data():
    try:
        # Try database connection
        conn = mysql.connector.connect(**DB_CONFIG)
        query = "SELECT waste_in_grams, quantity_in_grams, ingredient_count, food_type FROM Surplus"
        data = pd.read_sql(query, conn)
        conn.close()
        print("Data loaded from database successfully")
        return data
    except Exception as e:
        print(f"Database connection failed: {e}")
        print("Using sample data instead...")
        # Generate sample data
        np.random.seed(42)
        n_samples = 100
        data = pd.DataFrame({
            'waste_in_grams': np.random.randint(100, 1000, n_samples),
            'quantity_in_grams': np.random.randint(1000, 2000, n_samples),
            'ingredient_count': np.random.randint(2, 8, n_samples),
            'food_type': np.random.choice(['Indian', 'Chinese', 'Italian', 'Mexican'], n_samples)
        })
        return data

def prepare_data(data):
    # Create waste category based on median
    median_waste = data['waste_in_grams'].median()
    data['waste_category'] = ['High' if x > median_waste else 'Low' for x in data['waste_in_grams']]
    
    # One-hot encode food type
    data_encoded = pd.get_dummies(data, columns=['food_type'])
    
    # Prepare features and target
    X = data_encoded.drop(['waste_in_grams', 'waste_category'], axis=1)
    y = data_encoded['waste_category']
    
    return X, y

def train_model(X, y):
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    
    # Train model
    clf = RandomForestClassifier(random_state=42)
    clf.fit(X_train, y_train)
    
    # Evaluate model
    cv_scores = cross_val_score(clf, X, y, cv=5)
    print("Cross-Validated Scores:", cv_scores)
    
    # Test predictions
    y_pred = clf.predict(X_test)
    print(f"Model Accuracy: {clf.score(X_test, y_test):.2f}")
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    
    return clf, X_train

def predict_waste_category(user_quantity_in_grams, user_ingredient_count, user_food):
    user_input = pd.DataFrame({
        'quantity_in_grams': [user_quantity_in_grams],
        'ingredient_count': [user_ingredient_count],
    })
    
    # One-hot encode food type
    for food_type in data['food_type'].unique():
        user_input[f'food_type_{food_type}'] = 0
    if user_food in data['food_type'].unique():
        user_input[f'food_type_{user_food}'] = 1
    
    # Ensure all columns match training data
    missing_cols = set(X.columns) - set(user_input.columns)
    for col in missing_cols:
        user_input[col] = 0
    
    user_input = user_input[X_train.columns]
    
    user_prediction = clf.predict(user_input)
    
    if user_prediction[0] == 'High':
        return "This food item is producing high waste. Consider reducing the number of ingredients used or the quantity in which this food item is being prepared."
    else:
        return "Relax, this food item is producing low waste. You can go ahead preparing it. No changes required."

# Main execution
if __name__ == "__main__":
    print("Fetching data from the Surplus table...")
    data = load_data()
    print(data.shape)
    
    # Prepare and train model
    X, y = prepare_data(data)
    clf, X_train = train_model(X, y)
    print("Model training complete.")