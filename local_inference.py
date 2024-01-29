import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib

# Load the trained model
model = joblib.load('xgb_regressor_cholesterol.pkl')

# Example of new data (this should be replaced with your actual new data)
data = {
    'Age': [50],
    'Gender': ['Male'],
    'ChestPainType': ['Typical angina'],
    'RestingBloodPressure': [130],
    'FastingBloodSugar': [False],
    'RestingECG': ['ST-T wave abnormality'],
    'MaxHeartRate': [122],
    'ExerciseInducedAngina': ['No'],
    'STDepression': [0.0],
    'Slope': ['Flat'],
    'NumMajorVessels': [1],
    'Thalassemia': ['Normal'],
    'HeartDisease': [0]  # Assuming you want to include this feature as well, adjust if necessary
}

# Create a DataFrame from the new data
new_data_df = pd.DataFrame(data)

# Encode categorical variables just like in the training process
categorical_features = ['Gender', 'ChestPainType', 'FastingBloodSugar', 'RestingECG', 'ExerciseInducedAngina', 'Slope', 'Thalassemia']
for col in categorical_features:
    new_data_df[col] = LabelEncoder().fit_transform(new_data_df[col])



# Predict the cholesterol level with the trained model
predicted_cholesterol = model.predict(new_data_df)

print(f'Predicted Cholesterol Levels: {predicted_cholesterol}')