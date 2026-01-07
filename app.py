import streamlit as st
import google.generativeai as genai

# 1. Setup Gemini API - Secure & Clean
# In Streamlit Cloud: Go to Settings > Secrets and add GEMINI_API_KEY = "your_key"
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    # Fallback for local testing (Replace with your actual key here temporarily)
    api_key = "AIzaSyAcYinj66KegJuvK14jCa1BEz2y_WdY5mU" 

if not api_key or api_key == "AIzaSyAcYinj66KegJuvK14jCa1BEz2y_WdY5mU":
    st.warning("⚠️ API Key missing! Please add 'GEMINI_API_KEY' to Streamlit Secrets.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.5-flash')

# 2. Modern UI Design (Trend 2026: Wide & Immersive)
st.set_page_config(page_title="YogiEats AI Nutritionist", page_icon="🧘", layout="wide")

st.markdown("""
    <style>
    /* Occupy the full width of the GitHub container */
    .block-container {
        padding-top: 2rem;
        max-width: 95%;
    }
    
    /* Clean white background to match your site */
    .stApp {
        background-color: #ffffff;
    }

    /* Style for the 'Generate' button */
    div.stButton > button:first-child {
        background-color: #ff8c00 !important; /* Siddha Orange */
        color: white !important;
        border-radius: 50px;
        width: 100%;
        height: 3.5rem;
        font-size: 20px;
        font-weight: bold;
        border: none;
    }

    /* Modern Card for the result output */
    .stMarkdown {
        background: #fdfdfd;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        border: 1px solid #f0f0f0;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. User Interface (Centered & Modern)
st.title("🧘 Siddha Diet AI Recommendation Engine")
st.write("Professional nutrition advice tailored to your yoga practice and lifestyle.")

# Use columns to make the app look "Wide" and modern
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("How old are you?", min_value=18, max_value=100, value=26)
    body_type = st.selectbox("Your Body Type (Dosha)", 
                             ["Vata (Air/Space)", "Pitta (Fire/Water)", "Kapha (Earth/Water)", "Not Sure"])

with col2:
    goal = st.selectbox("What is your Primary Goal?", 
                        ["Mental Clarity", "Physical Strength", "Weight Balance", "Better Sleep"])
    practitioner = st.toggle("Regular Yoga & Meditation practitioner?")

st.divider() # Clean visual break

# 4. Generate the Recommendation
if st.button("Generate My Personalized Siddha Plan"):
    if api_key and api_key != "PASTE_YOUR_ACTUAL_KEY_HERE":
        with st.spinner("Consulting Siddha Wisdom..."):
            prompt = f"""
            Act as an expert Siddha Nutritionist. 
            User Context: {age} years old, {body_type} body type. 
            Goal: {goal}. Practitioner: {practitioner}.

            1. Provide a 1-day Sattvic meal plan (Breakfast, Lunch, Dinner).
            2. Based on their body type ({body_type}), recommend ONE specific natural supplement or tool. 
            3. Add: 'You can find my recommended organic sources at yogieats.in/resources.'
            4. Keep the tone calm, professional, and friendly.
            """
            
            try:
                response = model.generate_content(prompt)
                st.markdown("### 🥗 Your Personalized Recommendation")
                st.write(response.text)
                st.success("Plan generated successfully! 🕉️")
            except Exception as e:
                st.error(f"Something went wrong: {e}")
    else:
        st.error("Application not ready. Please configure the API Key.")