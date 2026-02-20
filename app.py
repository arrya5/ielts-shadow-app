import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import time
import json

load_dotenv()

# Check if API key is available
api_key = os.getenv("GOOGLE_API_KEY")
USE_MOCK = not api_key or api_key == "your_gemini_key_here"

if not USE_MOCK:
    genai.configure(api_key=api_key)
    # Using the standard flash alias which usually maps to the most stable free tier model
    try:
        model = genai.GenerativeModel('gemini-flash-latest')
    except Exception:
        model = genai.GenerativeModel('gemini-1.5-flash-latest')

# --- CONFIGURATION & STYLING ---
st.set_page_config(page_title="Leap AI-Shadow", page_icon="🎓", layout="wide")

# Custom CSS for a "Pro" look
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stTextArea textarea {
        background-color: #ffffff;
        border: 1px solid #ddd;
        border-radius: 10px;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        height: 50px;
        font-weight: bold;
    }
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# --- UI HEADER ---
col1, col2 = st.columns([1, 4])
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712035.png", width=80) 
with col2:
    st.title("Internship AI-Shadow Examiner")
    st.caption("🚀 Leap Finance | IELTS Speaking Module Prototype | Built by **Arrya Thakur**")

st.divider()

if USE_MOCK:
    st.warning("⚠️ Running in DEMO MODE. Add OpenAI API Key to .env for live AI grading.")

# --- SIDEBAR DASHBOARD ---
with st.sidebar:
    st.header("👤 Candidate Profile")
    st.markdown("---")
    
    # Fake progress stats
    st.metric(label="Overall Band Score", value="6.5", delta="Target: 7.5")
    
    st.subheader("🔥 Streak: 4 Days")
    st.progress(0.8, text="Daily Goal: 80%")
    
    st.markdown("### 📚 Weak Areas")
    st.code("• Complex Sentences\n• Pronunciation\n• Collocations", language=None)
    
    st.markdown("---")
    if st.button("🔄 Generate New Topics"):
        st.session_state.prompt = "Describe a traditional festival in your country."
        st.rerun()

    st.markdown("---")
    st.caption("👨‍💻 Developed by **Arrya Thakur**")
    st.caption("© 2026 AI Prototype")

# --- MAIN APP LOGIC ---

# 1. Challenge Section
if 'prompt' not in st.session_state:
    st.session_state.prompt = "Describe a piece of technology you find difficult to use."

st.subheader("🎙️ Speaking Challenge (Part 2)")
st.info(f"**Topic:** {st.session_state.prompt}")

# --- MAIN APP LOGIC ---

# 1. Challenge Section
if 'prompt' not in st.session_state:
    st.session_state.prompt = "Describe a piece of technology you find difficult to use."

st.subheader("🎙️ Speaking Challenge (Part 2)")
st.info(f"**Topic:** {st.session_state.prompt}")

# NEW: Unified Audio Logic with direct-to-grading
st.write("🔴 **Record your answer:**")
audio_val = st.audio_input("Record Answer")

# Mock data helper
def get_mock_evaluation(text, is_audio=False):
    feedback_text = "Good attempt with reasonable vocabulary."
    return {
        "band": "6.5",
        "lexical": "Good use of tech vocabulary.",
        "grammar": "Sentences are mostly simple.",
        "coherence": "Flow is logical.",
        "fix": "Use 'However' to connect ideas.",
        "transcript": "Partial transcript unavailable in mock mode."
    }

if audio_val:
    with st.spinner("🤖 Shadow is listening & analyzing..."):
        if USE_MOCK:
             time.sleep(1.5)
             data = get_mock_evaluation("", is_audio=True)
             transcript = "I find smart home devices difficult to use..."
        else:
            try:
                # FAST MODE: Send audio directly to Gemini for grading (Multimodal)
                audio_bytes = audio_val.read()
                
                # We ask for transcript AND grade in ONE call to save time
                prompt = """
                You are an expert IELTS Examiner. Listen to this audio response for the provided topic.
                
                Task 1: Transcribe the speech verbatim (key: 'transcript').
                Task 2: Evaluate based on Lexical Resource, Grammar, and Coherence.
                
                Return strictly VALID JSON with no markdown formatting. Keys: transcript, band, lexical, grammar, coherence, fix.
                """
                
                response = model.generate_content([
                    prompt,
                    {"mime_type": "audio/wav", "data": audio_bytes}
                ])
                
                # Parse Response
                raw_text = response.text.replace("```json", "").replace("```", "").strip()
                data = json.loads(raw_text)
                transcript = data.get("transcript", "")
                
            except Exception as e:
                st.error(f"Analysis Error: {e}")
                data = get_mock_evaluation("", is_audio=True)
                transcript = "Error retrieving transcript."

    # Display Results Immediately
    st.markdown("---")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.success("✅ Analysis Complete!")
        st.text_area("Your Transcript:", value=transcript, height=100)

    st.subheader("📊 Performance Report")
    
    # Score Cards
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Band Score", str(data.get("band", "N/A")))
    m2.metric("Lexical", "Good")
    m3.metric("Grammar", "Fair")
    m4.metric("Fluency", "Strong")

    # Detailed Feedback
    st.info(f"**Vocab:** {data.get('lexical', 'N/A')}")
    st.warning(f"**Grammar:** {data.get('grammar', 'N/A')}")
    st.error(f"🎯 **Fix:** {data.get('fix', 'Practice more!')}")

# Text Fallback
elif not audio_val:
    user_input = st.text_area("Or type your answer here:")
    if st.button("Analyze Text"):
        st.info("Please record audio for the best experience!")
        st.button("Save to Progress Tracker")
