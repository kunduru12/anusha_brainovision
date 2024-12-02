import streamlit as st
import pickle


# Load your trained model
model_path = "C://Users//nagoo//Downloads//NB.pkl"
model = pickle.load(open(model_path, "rb"))


st.title("Spam Classifier")


# Text input
user_input = st.text_input("Message", "")

# Prediction
if user_input:
    
    # Predict
    prediction = model.predict([user_input])  # 1 = Spam, 0 = Not Spam
    confidence = model.predict_proba([user_input]).max() * 100

    # Display the result
    if prediction == 1:
        st.error(f"🚨 This message is SPAM with {confidence:.2f}% confidence!")
    else:
        st.success(f"✅ This message is NOT SPAM with {confidence:.2f}% confidence!")


