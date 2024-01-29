#This is to make the dataset more readable

import pandas as pd
# from colab.google import drive
# drive. mount('/content/drive')


df=pd.read_csv("heart.csv")

# Replace 'sex' column
df['sex'] = df['sex'].replace({0: 'Female', 1: 'Male'})

# Replace 'cp' column
df['cp'] = df['cp'].replace({0: 'Typical angina', 1: 'Atypical angina', 2: 'Non-anginal pain', 3: 'Asymptomatic'})

# Replace 'fbs' column
df['fbs'] = df['fbs'].replace({0: 'False', 1: 'True'})

# Replace 'restecg' column
df['restecg'] = df['restecg'].replace({0: 'Normal', 1: 'ST-T wave abnormality', 2: 'Probable or definite LV hypertrophy'})

# Replace 'exang' column
df['exang'] = df['exang'].replace({0: 'No', 1: 'Yes'})

# Replace 'slope' column
df['slope'] = df['slope'].replace({0: 'Upsloping', 1: 'Flat', 2: 'Downsloping'})

# Replace 'thal' column
df['thal'] = df['thal'].replace({1: 'Normal', 2: 'Fixed defect', 3: 'Reversible defect'})

# print(df.head())




#This is to give the columns better names. Its also a form of cleaning too



column_name_mapping = {
    'age': 'Age',
    'sex': 'Gender',
    'cp': 'ChestPainType',
    'trestbps': 'RestingBloodPressure',
    'chol': 'Cholesterol',
    'fbs': 'FastingBloodSugar',
    'restecg': 'RestingECG',
    'thalach': 'MaxHeartRate',
    'exang': 'ExerciseInducedAngina',
    'oldpeak': 'STDepression',
    'slope': 'Slope',
    'ca': 'NumMajorVessels',
    'thal': 'Thalassemia',
    'target': 'HeartDisease'
}

# Rename the columns using the dictionary
df = df.rename(columns=column_name_mapping)

df.to_csv("heart_cleaned.csv",index=False)

print(df.head())

