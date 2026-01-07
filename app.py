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

# 2. Match the YogiEats Design Trend
st.set_page_config(page_title="YogiEats AI", page_icon="🧘", layout="wide")

st.markdown(f"""
    <style>
    /* Use your site's fonts */
    @import url('https://fonts.googleapis.com/css2?family=Karla:wght@400;700&family=Playfair+Display:wght@700&display=swap');

    .stApp {{
        background-color: transparent;
    }}
    
    h1, h2, h3 {{
        font-family: 'Playfair Display', serif !important;
        color: #242424 !important; /* Your e-global-color-primary */
    }}

    p, div, span, label {{
        font-family: 'Karla', sans-serif !important;
        color: #6b6b6b !important; /* Your e-global-color-text */
    }}

    /* Match your 'Get Started' button style */
    .stButton>button {{
        background-color: #ff8c00 !important; /* Your Siddha Orange */
        color: white !important;
        border-radius: 35px 0px 35px 0px !important; /* Your unique button shape */
        border: none !important;
        font-size: 22px !important;
        padding: 15px 40px !important;
        transition: 0.3s !important;
    }}

    .stButton>button:hover {{
        transform: translateY(-5px) !important;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1) !important;
    }}
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
