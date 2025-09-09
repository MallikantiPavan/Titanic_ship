import streamlit as st
import requests

st.set_page_config(page_title="Titanic Survival Prediction", layout="centered")


image_url = "https://media.istockphoto.com/id/503132519/photo/titanic-and-iceberg.jpg?s=612x612&w=0&k=20&c=cO71OMKsceiSj07heG1jhOiNRNGevD-XrACWis2RdQ4="

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{image_url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    .reportview-container {{
        background: rgba(255, 255, 255, 0.85);
        padding: 20px;
        border-radius: 12px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🚢 Titanic Survival Prediction")

col1,col2,col3=st.columns([1,1,2])

with col1:
    Pclass = st.selectbox("Passenger Class", [1, 2, 3])
    Age = st.number_input("Age", 0, 100, 30)  
with col2:
    SibSp = st.number_input("Siblings/Spouses aboard", 0, 10, 0)
    Parch = st.number_input("Parents/Children aboard", 0, 10, 0)
with col3:
    Fare = st.number_input("Fare", 0.0, 500.0, 32.2) 
    Sex = st.selectbox("Sex", ["female", "male"])
    Embarked = st.selectbox("Embarked", ["C", "Q", "S"])

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

    try:
        response = requests.post("https://titanic-ship.onrender.com/predict", json=passenger_data)
        response.raise_for_status()
        result = response.json()

        # Format probability as percentage
        prob = round(result["probability"] , 2) if isinstance(result["probability"], float) else result["probability"]
        pred = result["prediction"]

        if pred == 0:
            st.markdown(
                f"""
                <div style='background-color: #e74c3c; padding: 13px; border-radius: 10px; color: white; font-weight: bold; font-size: 16px;'>
                    ⚠️ Not Survived<br>
                    Probability: {prob}%
                </div>
                """,
                unsafe_allow_html=True
            )
        elif pred == 1:
            st.markdown(
                f"""
                <div style='background-color: #2ecc71; padding: 13px; border-radius: 10px; color: white; font-weight: bold; font-size: 16px;'>
                    ✅ Survived<br>
                    Probability: {prob}%
                </div>
                """,
                unsafe_allow_html=True
            )

    except requests.exceptions.RequestException as e:
        st.error(f"❌ API request failed: {e}")
