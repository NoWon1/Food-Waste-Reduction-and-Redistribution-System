from sqlalchemy import create_engine
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE
import joblib
from xgboost import XGBClassifier
from urllib.parse import quote_plus


db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Aditya@06',
    'database': 'food'
}

try:
    
    password = quote_plus(db_config['password'])
    connection_str = f"mysql+pymysql://{db_config['user']}:{password}@{db_config['host']}/{db_config['database']}"
    
    
    engine = create_engine(connection_str)
    
    
    query = 'SELECT * FROM surplus'
    data = pd.read_sql(query, con=engine)
    
    
    if 'waste_in_grams' in data.columns:
        threshold = data['waste_in_grams'].median()
        data['waste_category'] = data['waste_in_grams'].apply(lambda x: 'High' if x > threshold else 'Low')
        print("Waste Category Distribution:")
        print(data['waste_category'].value_counts())
    else:
        raise ValueError("The column 'waste_in_grams' does not exist in the table")

    
    data['days_to_expiry'] = (pd.to_datetime(data['Expiry_Date']) - pd.to_datetime('today')).dt.days
    selected_features = ['quantity_in_grams', 'ingredient_count', 'food_type', 'days_to_expiry']
    X = data[selected_features]
    X = pd.get_dummies(X, columns=['food_type'])
    
    
    le = LabelEncoder()
    y = le.fit_transform(data['waste_category'])
    
    
    joblib.dump(le, 'label_encoder.pkl')

    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    
    smote = SMOTE(random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

    
    param_grid = {
        'n_estimators': [100, 200],
        'max_depth': [10, 20, None],
        'min_samples_split': [2, 5],
        'min_samples_leaf': [1, 2]
    }

    rf_clf = RandomForestClassifier(random_state=42)
    grid_search = GridSearchCV(rf_clf, param_grid, cv=5)
    grid_search.fit(X_resampled, y_resampled)
    best_model_rf = grid_search.best_estimator_

    
    y_pred_rf = best_model_rf.predict(X_test)
    
    print("\nEvaluating RandomForest model...")
    print(f"Random Forest Accuracy: {accuracy_score(y_test, y_pred_rf):.2f}")
    print("Random Forest Classification Report:")
    print(classification_report(y_test, y_pred_rf, target_names=le.classes_))

    
    print("\nTraining XGBoost model...")
    xgb_clf = XGBClassifier(random_state=42)
    xgb_clf.fit(X_resampled, y_resampled)
    
    y_pred_xgb = xgb_clf.predict(X_test)
    
    print("Evaluating XGBoost model...")
    print(f"XGBoost Accuracy: {accuracy_score(y_test, y_pred_xgb):.2f}")
    print("XGBoost Classification Report:")
    print(classification_report(y_test, y_pred_xgb, target_names=le.classes_))

    
    print("\nSaving models...")
    joblib.dump(best_model_rf, 'final_trained_model_rf.pkl')
    joblib.dump(xgb_clf, 'final_trained_model_xgb.pkl')
    print("Models saved successfully!")

except Exception as e:
    print(f"Error: {str(e)}")
    print("Please check:")
    print("1. MySQL server is running")
    print("2. Database credentials are correct") 
    print("3. Database 'food' exists")