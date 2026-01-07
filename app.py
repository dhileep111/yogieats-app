import streamlit as st
import google.generativeai as genai

# 1. Setup Gemini API - The "Secret" way is the ONLY way for public repos
try:
    # Use the LABEL "GEMINI_API_KEY", not the actual key here!
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    api_key = None 

if not api_key:
    st.error("⚠️ API Key missing! Add 'GEMINI_API_KEY' to your Streamlit Cloud Secrets.")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.5-flash')

# 2. Modern trend UI (Immersive & Wide)
st.set_page_config(page_title="YogiEats AI", page_icon="🧘", layout="wide")

st.markdown("""
    <style>
    /* Force the app to use the full width of your GitHub site container */
    .block-container {
        max-width: 100% !important;
        padding: 1rem 2rem !important;
    }
    
    /* Clean white background */
    .stApp { background-color: #ffffff; }

    /* Modern centered inputs */
    div[data-baseweb="select"] > div, div[data-baseweb="input"] > div {
        border-radius: 15px;
        border: 1px solid #e0e0e0;
    }

    /* Siddha Orange Button */
    .stButton button {
        width: 100%;
        border-radius: 50px;
        background-color: #ff8c00 !important;
        color: white !important;
        font-weight: bold;
        height: 3.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. User Interface
st.title("🧘 Siddha Diet AI")
st.write("Professional nutrition advice tailored to your practice.")

col1, col2 = st.columns(2)
with col1:
    age = st.number_input("Age", min_value=18, max_value=100, value=26)
    body_type = st.selectbox("Body Type", ["Vata", "Pitta", "Kapha", "Not Sure"])
with col2:
    goal = st.selectbox("Goal", ["Mental Clarity", "Physical Strength", "Weight Balance", "Better Sleep"])
    practitioner = st.toggle("Regular Yoga & Meditation practitioner?")

if st.button("Generate My Siddha Plan"):
    with st.spinner("Consulting Siddha Wisdom..."):
        prompt = f"Expert Siddha Nutritionist plan for {age}yo, {body_type}, goal: {goal}. Add: 'Find sources at yogieats.in/resources.'"
        try:
            response = model.generate_content(prompt)
            st.markdown("---")
            st.write(response.text)
            st.success("Plan generated! 🕉️")
        except Exception as e:
            st.error(f"Error: {e}")
