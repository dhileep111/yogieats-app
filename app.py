import streamlit as st
import google.generativeai as genai

# 1. Setup Gemini API - Security Fix
# Use 'GEMINI_API_KEY' as the name in your Streamlit Secrets dashboard
try:
    api_key = st.secrets["AIzaSyAcYinj66KegJuvK14jCa1BEz2y_WdY5mU"]
except Exception:
    api_key = "AIzaSyAcYinj66KegJuvK14jCa1BEz2y_WdY5mU" 

if not api_key or api_key == "AIzaSyAcYinj66KegJuvK14jCa1BEz2y_WdY5mU":
    st.warning("Please add 'GEMINI_API_KEY' to your Streamlit Secrets!")

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.5-flash')

# 2. Modern UI with "Glassmorphism" Style
st.set_page_config(page_title="YogiEats AI", page_icon="🧘", layout="wide")

st.markdown("""
    <style>
    /* Remove padding to let the app occupy the full width */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        max-width: 95%; /* Makes the app occupy more horizontal space */
    }
    
    .stApp {
        background-color: transparent;
    }

    /* Modern clean inputs */
    div[data-baseweb="select"] > div, div[data-baseweb="input"] > div {
        border-radius: 12px;
        border: 1px solid #e0e0e0;
        background-color: #ffffff;
    }

    /* Centered output card */
    .stMarkdown {
        background: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        border: 1px solid #f0f0f0;
        margin-top: 20px;
    }
    
    /* Make the button big and centered */
    .stButton button {
        width: 100%;
        border-radius: 12px;
        height: 3em;
        background-color: #ff8c00 !important;
        color: white !important;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Main Page Content (No Sidebar for a cleaner trend)
st.title("🧘 Siddha Diet AI")
st.write("Get your personalized Sattvic plan instantly.")

# Organize inputs into columns to save vertical space
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=18, max_value=100, value=26)
    body_type = st.selectbox("Body Type (Dosha)", ["Vata (Air/Space)", "Pitta (Fire/Water)", "Kapha (Earth/Water)", "Not Sure"])

with col2:
    goal = st.selectbox("Primary Goal", ["Mental Clarity", "Physical Strength", "Weight Balance", "Better Sleep"])
    practitioner = st.toggle("Regular Yoga & Meditation practitioner?")

# 4. Generate Recommendation
if st.button("Generate My Siddha Plan"):
    if api_key and api_key != "YOUR_LOCAL_KEY_HERE":
        with st.spinner("Consulting Siddha Wisdom..."):
            prompt = f"""
            Act as an expert Siddha Nutritionist. 
            User: {age} years old, {body_type} body type. 
            Goal: {goal}. Practitioner: {practitioner}.

            1. Provide a 1-day Sattvic meal plan.
            2. Recommend ONE natural supplement/tool for {body_type}. 
            3. Add: 'Find recommended organic sources at yogieats.in/resources.'
            4. Keep the tone friendly and supportive."""
            
            try:
                response = model.generate_content(prompt)
                st.markdown("---")
                st.write(response.text)
                st.success("Plan generated! Your journey to wellness begins here. 🕉️")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.error("API Key is missing. Check Streamlit Secrets.")

