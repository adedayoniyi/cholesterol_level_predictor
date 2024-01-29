import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

df = pd.read_csv('heart_cleaned.csv')

# Encode categorical variables
categorical_features = ['Gender', 'ChestPainType', 'FastingBloodSugar', 'RestingECG', 'ExerciseInducedAngina', 'Slope', 'Thalassemia']
for col in categorical_features:
    df[col] = LabelEncoder().fit_transform(df[col])

# Split data into X and y
X = df.drop('Cholesterol', axis=1)
y = df['Cholesterol']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the XGBoost regressor
model = XGBRegressor(objective='reg:squarederror', n_estimators=100)
model.fit(X_train, y_train)

# Save the trained model to a file
joblib.dump(model, 'xgb_regressor_cholesterol.pkl')

# Optionally, load the model
model = joblib.load('xgb_regressor_cholesterol.pkl')

y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'R-squared Score: {r2}')