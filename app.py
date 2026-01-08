import streamlit as st
import google.generativeai as genai

# 1. Setup Gemini API - Secure & Clean
try:
    # Always use the label "GEMINI_API_KEY" in Streamlit Secrets
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
    @import url('https://fonts.googleapis.com/css2?family=Karla:wght@400;700&family=Playfair+Display:wght@700&display=swap');

    .stApp {{
        background-color: transparent;
    }}
    
    h1, h2, h3 {{
        font-family: 'Playfair Display', serif !important;
        color: #242424 !important;
    }}

    p, div, span, label {{
        font-family: 'Karla', sans-serif !important;
        color: #6b6b6b !important;
    }}

    /* Match your 'Get Started' button style */
    .stButton>button {{
        background-color: #ff8c00 !important;
        color: white !important;
        border-radius: 35px 0px 35px 0px !important;
        border: none !important;
        font-size: 22px !important;
        padding: 15px 40px !important;
        transition: 0.3s !important;
        width: 100%;
    }}

    .stButton>button:hover {{
        transform: translateY(-5px) !important;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1) !important;
        background-color: #e67e00 !important;
        color: white !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# 3. User Interface
st.title("🧘 Siddha Diet AI")
st.write("Professional nutrition advice tailored to your practice and body type.")

# Column layout for modern feel
col1, col2 = st.columns(2)
with col1:
    age = st.number_input("How old are you?", min_value=18, max_value=100, value=26)
    body_type = st.selectbox("Your Body Type (Dosha)", ["Vata", "Pitta", "Kapha", "Not Sure"])
with col2:
    goal = st.selectbox("Your Primary Goal", ["Mental Clarity", "Physical Strength", "Weight Balance", "Better Sleep"])
    practitioner = st.toggle("Regular Yoga & Meditation practitioner?")

st.markdown("---")

# 4. Generate Recommendation (Only ONE button now)
if st.button("Generate My Personalized Siddha Plan"):
    with st.spinner("Consulting Siddha Wisdom..."):
        # Professional, supportive prompt that drives WhatsApp leads
        prompt = f"""
        Act as an expert Siddha Nutritionist for YogiEats. 
        The user is {age} years old with a {body_type} body type. 
        Goal: {goal}. Yoga Practitioner: {practitioner}.

        1. Provide a detailed 1-day Sattvic meal plan (Breakfast, Lunch, Dinner).
        2. Recommend ONE specific natural tool or herb (like a Copper Bottle or Triphala) specifically for their {body_type} type.
        3. IMPORTANT: End the response with this exact text: 
           'For a direct recommendation of the best organic brands and local suppliers in India, visit https://yogieats.in/resources and message me on WhatsApp!'
        4. Keep the tone calm, professional, and encouraging.
        """
        
        try:
            response = model.generate_content(prompt)
            st.markdown("### 🥗 Your Personalized YogiEats Plan")
            st.write(response.text)
            st.success("Your journey to wellness begins here. 🕉️")
        except Exception as e:
            st.error(f"Something went wrong: {e}")
