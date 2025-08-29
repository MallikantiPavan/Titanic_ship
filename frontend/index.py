
import streamlit as st
import requests

st.title("Titanic Survival Prediction")

# User input
Pclass = st.selectbox("Passenger Class", [1, 2, 3])
Age = st.number_input("Age", 0, 100)
SibSp = st.number_input("Siblings/Spouses aboard", 0, 10)
Parch = st.number_input("Parents/Children aboard", 0, 10)
Fare = st.number_input("Fare", 0.0, 500.0)
Sex = st.selectbox("Sex", ["female", "male"])
Embarked = st.selectbox("Embarked", ["C", "Q", "S"])

# Convert categorical inputs to match one-hot encoding
Sex_male = 1 if Sex == "male" else 0
Embarked_Q = 1 if Embarked == "Q" else 0
Embarked_S = 1 if Embarked == "S" else 0

if st.button("Predict"):
    passenger_data = {
        "Pclass": Pclass,
        "Age": Age,
        "SibSp": SibSp,
        "Parch": Parch,
        "Fare": Fare,
        "Sex_male": Sex_male,
        "Embarked_Q": Embarked_Q,
        "Embarked_S": Embarked_S
    }
    
    response = requests.post("http://127.0.0.1:8000/predict", json=passenger_data)
    
    if response.status_code == 200:
        result = response.json()
        pred=result['prediction']
        if pred==0:
            st.warning(f"Not Survived,probability:{result['probability']}")
        elif pred==1:
            st.success(f'Survived,probability:{result["probability"]}')
       