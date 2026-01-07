import streamlit as st
import google.generativeai as genai

# 1. Setup Gemini API - Use secrets for security when deploying
# Locally, replace "YOUR_API_KEY" with your real key from Google AI Studio
try:
    api_key = st.secrets["AIzaSyAcYinj66KegJuvK14jCa1BEz2y_WdY5mU"]
except:
    api_key = "YOUR_API_KEY_HERE" 

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.5-flash')

# 2. Website UI
st.set_page_config(page_title="YogiEats AI Nutritionist", page_icon="🧘")
st.title("🧘 Siddha Diet AI Recommendation Engine")
st.subheader("Personalized Sattvic nutrition based on your lifestyle.")

# 3. User Inputs
with st.sidebar:
    st.header("Your Profile")
    age = st.number_input("Age", min_value=18, max_value=100, value=25)
    body_type = st.selectbox("Body Type (Dosha)", ["Vata (Air/Space)", "Pitta (Fire/Water)", "Kapha (Earth/Water)", "Not Sure"])
    goal = st.selectbox("Primary Goal", ["Mental Clarity", "Physical Strength", "Weight Balance", "Better Sleep"])
    # Changed from specific Kundalini/Kaya Kalpa wordings
    practitioner = st.toggle("Are you a regular Yoga & Meditation practitioner?")

# 4. Generate Recommendation
if st.button("Generate My Siddha Plan"):
    with st.spinner("Consulting Siddha Wisdom..."):
        # The System Prompt (Tells AI how to behave)
        prompt = f"""
        Act as an expert Siddha Nutritionist. 
        The user is {age} years old with a {body_type} body type. 
        Their goal is {goal}. Yoga Practitioner: {practitioner}.
        
        Provide a 1-day Sattvic meal plan (Breakfast, Lunch, Dinner).
        Focus on Siddha principles like 'Food is Medicine'.
        Include one 'Digital Wellness' tip for the day.
        Keep the tone calm, professional, and encouraging.
        """
        
        try:
            response = model.generate_content(prompt)
            st.markdown("---")
            st.write(response.text)
            st.success("Plan generated! Your journey to wellness begins here. 🕉️")
        except Exception as e:
            st.error("Make sure your API Key is correct in the code or Streamlit Secrets!")