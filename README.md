# Food Waste Reduction and Redistribution System

A Python-based system designed to efficiently manage and redistribute surplus food to those in need while minimizing food waste.

## Features

### Database Management: 
Uses MySQL for storing and managing food surplus, donor, and recipient data
### User Authentication:
Secure login system for donors and NGOs
### Food Waste Prediction: 
ML-based prediction model for food waste estimation
### Automated Matching: 
Intelligent matching of food donors with recipient NGOs
### Nutritional Analysis: 
Integration with USDA API for nutritional information
### Real-time Updates: 
Live tracking of food availability and redistribution status

## Tech Stack
1. Python 3.11
2. MySQL Database
3. SQLAlchemy ORM
4. Machine Learning Libraries
5. USDA Food Data API


## Setup
### 1. Clone the repository
### 2. Install dependencies:

```bash
pip install -r requirements.txt
```
### 3. Configure database settings in main.py:

```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'food'
}
```
## Project Structure
### main.py: 
Main application entry point and database configuration
### data.py: 
Data processing and management
### predict.py: 
ML model for waste prediction
### route.py: 
Route optimization for food distribution
### nutri.py: 
Nutritional analysis integration
### SQL files: 
Database schema and queries

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
