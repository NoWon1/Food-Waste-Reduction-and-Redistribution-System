from sqlalchemy import create_engine
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pymysql
import warnings
warnings.filterwarnings('ignore')

try:
    
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'Mypa55word',
        'database': 'food',
    }
    connection_str = f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}?ssl=false"
    engine = create_engine(connection_str)
    
    
    with engine.connect() as conn:
        query = 'SELECT * FROM Surplus'
        data = pd.read_sql(query, con=conn)
    print("Successfully connected to database")

except Exception as e:
    print(f"Database connection failed: {e}")
    print("Using sample data instead...")
    
    
    data = pd.DataFrame({
        'waste_in_grams': np.random.randint(100, 1000, 100),
        'quantity_in_grams': np.random.randint(500, 2000, 100),
        'ingredient_count': np.random.randint(2, 10, 100),
        'food_type': np.random.choice(['Indian', 'Chinese', 'Italian', 'Mexican'], 100)
    })


print("Fetching data from the Surplus table...")
print(data.head())  
print(data.shape)   


if data.empty:
    print("Error: The Surplus table is empty. Please populate it with data and try again.")
    exit()


threshold = np.percentile(data['waste_in_grams'], 50)


data['waste_category'] = np.where(data['waste_in_grams'] > threshold, 'High', 'Low')


selected_features = ['quantity_in_grams', 'ingredient_count', 'food_type']
X = data[selected_features]
X = pd.get_dummies(X, columns=['food_type'])  
y = data['waste_category']


X_train, X_valid, y_train, y_valid = train_test_split(X, y, random_state=42)


clf = RandomForestClassifier(max_depth=3, min_samples_split=2, min_samples_leaf=1, n_estimators=60, random_state=46)
kf = KFold(n_splits=5, shuffle=True, random_state=42)


cross_val_scores = cross_val_score(clf, X, y, cv=kf)


clf.fit(X_train, y_train)


y_pred = clf.predict(X_valid)
accuracy = accuracy_score(y_valid, y_pred)
report = classification_report(y_valid, y_pred, target_names=['Low', 'High'])


print("Model training complete.")
print(f"Cross-Validated Scores: {cross_val_scores}")
print(f"Model Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(report)


def check_overfitting(clf, X, y, X_valid, y_valid, cv):
    cross_val_scores = cross_val_score(clf, X, y, cv=cv)
    clf.fit(X, y)
    y_pred = clf.predict(X_valid)
    accuracy = accuracy_score(y_valid, y_pred)
    mean_cv_score = cross_val_scores.mean()
    std_cv_score = cross_val_scores.std()

    print(f"Mean Cross-Validated Score: {mean_cv_score:.2f}")
    print(f"Standard Deviation of Cross-Validated Scores: {std_cv_score:.2f}")
    print(f"Validation Set Accuracy: {accuracy:.2f}")

    if mean_cv_score > accuracy:
        print("Warning: The model may be overfitting to the training data.")
    else:
        print("The model does not appear to be overfitting.")
