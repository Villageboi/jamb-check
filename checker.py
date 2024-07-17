import streamlit as st
from PIL import Image

def determine_institution(score):
    if score < 1 or score > 400:
        return "Invalid score"
    elif 1<= score <= 120:
        return "You have gained Admission into a trade institution"
    elif 121 <= score <= 179:
        return "You have gained Admission into a Polytechnic"
    elif 180 <= score <= 349:
        return "congratulation you have gained admission into the University"
    elif 350 <= score <= 400:
        return "Congrats scohlars you have been give a schlarshhip into any institution of your choice"
    
st.title("Admission Determiner")

name = st.text_input("Enter your name")
score = st.number_input("Enter your score", min_value=0, max_value=400)

if st.button("Determine Admission"):
    if name:
        result = determine_institution(score)
        st.success(f"Congratulations {name}, {result.lower()}")
    else:
        st.warning("Please enter your name.")