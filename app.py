import streamlit as st
import google.generativeai as genai

# 1. Setup Gemini API 
# This looks for a Secret named "AIzaSyAcYinj66KegJuvK14jCa1BEz2y_WdY5mU" in the Streamlit Dashboard
try:
    api_key = st.secrets["AIzaSyAcYinj66KegJuvK14jCa1BEz2y_WdY5mU"]
except Exception:
    # If running locally, it will look here (Replace with your NEW key for local testing only)
    api_key = "AIzaSyAcYinj66KegJuvK14jCa1BEz2y_WdY5mU" 

if not api_key or api_key == "AIzaSyAcYinj66KegJuvK14jCa1BEz2y_WdY5mU":
    st.warning("Please add your Gemini API Key to Streamlit Secrets!")

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.5-flash')

# 2. Modern UI with "Glassmorphism" Style
st.set_page_config(page_title="YogiEats AI", page_icon="🧘", layout="wide") # 'wide' uses the full screen

st.markdown("""
    <style>
    /* Remove the 'padding' at the top of the page */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    
    /* Make the background perfectly match your GitHub site */
    .stApp {
        background-color: transparent;
    }

    /* Style the input fields to be modern and 'clean' */
    div[data-baseweb="select"] > div {
        border-radius: 12px;
        border: 1px solid #e0e0e0;
    }

    /* MODERN TREND: Use a centered card for the output */
    .stMarkdown {
        background: rgba(255, 255, 255, 0.8);
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border: 1px solid #f0f0f0;
    }
    </style>
    """, unsafe_allow_html=True)

# Move your inputs to the main page instead of the sidebar for a "Chat" vibe
st.title("🧘 Siddha Diet AI")
col1, col2 = st.columns(2)
with col1:
    age = st.number_input("Age", min_value=18, max_value=100, value=26)
    body_type = st.selectbox("Body Type (Dosha)", ["Vata (Air/Space)", "Pitta (Fire/Water)", "Kapha (Earth/Water)", "Not Sure"])
with col2:
    goal = st.selectbox("Primary Goal", ["Mental Clarity", "Physical Strength", "Weight Balance", "Better Sleep"])
    practitioner = st.toggle("Regular Yoga Practitioner?")

# 3. User Inputs
with st.sidebar:
    st.header("Your Profile")
    age = st.number_input("Age", min_value=18, max_value=100, value=25)
    body_type = st.selectbox("Body Type (Dosha)", ["Vata (Air/Space)", "Pitta (Fire/Water)", "Kapha (Earth/Water)", "Not Sure"])
    goal = st.selectbox("Primary Goal", ["Mental Clarity", "Physical Strength", "Weight Balance", "Better Sleep"])
    practitioner = st.toggle("Are you a regular Yoga & Meditation practitioner?")

# 4. Generate Recommendation
if st.button("Generate My Siddha Plan"):
    if api_key and api_key != "PASTE_YOUR_NEW_KEY_HERE_FOR_LOCAL_TESTING":
        with st.spinner("Consulting Siddha Wisdom..."):
            prompt = f"""
            Act as an expert Siddha Nutritionist. 
            The user is {age} years old with a {body_type} body type. 
            Goal: {goal}. Practitioner: {practitioner}.

            1. Provide a 1-day Sattvic meal plan (Breakfast, Lunch, Dinner).
            2. For their body type ({body_type}), recommend ONE specific natural supplement or tool. 
            3. After the recommendation, add: 'Find recommended organic sources at yogieats.in/resources.'
            4. Keep the tone friendly and supportive."""
            
            try:
                response = model.generate_content(prompt)
                st.markdown("---")
                st.write(response.text)
                st.success("Plan generated! Your journey to wellness begins here. 🕉️")
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:

        st.error("API Key is missing. Go to Streamlit Settings > Secrets and add GEMINI_API_KEY.")

