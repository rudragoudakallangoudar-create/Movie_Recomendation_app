import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Streamlit UI
st.title("🎥 Movie Recommendation System 🎥")

user_input = st.text_input("Enter the movie name")
submit = st.button("Click here")

# Initialize Gemini model
model = genai.GenerativeModel("gemini-2.5-flash-lite")

if submit and user_input.strip():
    st.markdown(f"Movie name entered: **{user_input}**")
    
    # Generate recommendations
    response = model.generate_content(
        f"Generate 5 movie recommendations related to {user_input}. "
        "Provide a short description for each."
    )
    
    # Display response safely
    try:
        st.write("### Related Recommendations:")
        st.write(response.text)
    except AttributeError:
        st.write(response)  # fallback if .text doesn’t exist
else:
    st.write("Please enter a movie name to get recommendations.")