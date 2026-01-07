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