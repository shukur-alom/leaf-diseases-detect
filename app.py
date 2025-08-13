

import streamlit as st
import requests

import streamlit as st
import requests

# Set Streamlit theme to light and wide mode
st.set_page_config(page_title="Leaf Disease Detection", layout="wide")

# Custom CSS for modern look
st.markdown("""
    <style>
    .main {
        background-color: #f7f9fa;
    }
    .stApp {
        background-color: #f7f9fa;
    }
    .result-card {
        background: white;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.07);
        padding: 2em;
        margin-top: 1em;
    }
    .disease-title {
        color: #2e7d32;
        font-size: 2em;
        font-weight: bold;
        margin-bottom: 0.5em;
    }
    .section-title {
        color: #1565c0;
        font-size: 1.2em;
        margin-top: 1em;
        margin-bottom: 0.5em;
    }
    .timestamp {
        color: #616161;
        font-size: 0.9em;
        margin-top: 1em;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #1565c0;'>🌿 Leaf Disease Detection</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #616161;'>Upload a leaf image to detect diseases and get expert recommendations.</p>", unsafe_allow_html=True)

api_url = "http://leaf-diseases-detect.vercel.app"

col1, col2 = st.columns([1,2])
with col1:
    uploaded_file = st.file_uploader("Upload Leaf Image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Preview", use_column_width=True)

with col2:
    if uploaded_file is not None:
        if st.button("🔍 Detect Disease", use_container_width=True):
            with st.spinner("Analyzing image and contacting API..."):
                try:
                    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                    response = requests.post(f"{api_url}/disease-detection-file", files=files)
                    if response.status_code == 200:
                        result = response.json()
                        if result.get("disease_detected"):
                            st.markdown("<div class='result-card'>", unsafe_allow_html=True)
                            st.markdown(f"<div class='disease-title'>🦠 {result.get('disease_name', 'N/A')}</div>", unsafe_allow_html=True)
                            st.markdown(f"<b>Type:</b> <span style='color:#2e7d32'>{result.get('disease_type', 'N/A')}</span>", unsafe_allow_html=True)
                            st.markdown(f"<b>Severity:</b> <span style='color:#ef6c00'>{result.get('severity', 'N/A')}</span>", unsafe_allow_html=True)
                            st.markdown(f"<b>Confidence:</b> <span style='color:#1565c0'>{result.get('confidence', 'N/A')}%</span>", unsafe_allow_html=True)
                            st.markdown("<div class='section-title'>Symptoms</div>", unsafe_allow_html=True)
                            for symptom in result.get("symptoms", []):
                                st.markdown(f"- {symptom}")
                            st.markdown("<div class='section-title'>Possible Causes</div>", unsafe_allow_html=True)
                            for cause in result.get("possible_causes", []):
                                st.markdown(f"- {cause}")
                            st.markdown("<div class='section-title'>Treatment</div>", unsafe_allow_html=True)
                            for treat in result.get("treatment", []):
                                st.markdown(f"- {treat}")
                            st.markdown(f"<div class='timestamp'>🕒 {result.get('analysis_timestamp', 'N/A')}</div>", unsafe_allow_html=True)
                            st.markdown("</div>", unsafe_allow_html=True)
                        else:
                            st.info("No disease detected.")
                            st.json(result)
                    else:
                        st.error(f"API Error: {response.status_code}")
                        st.write(response.text)
                except Exception as e:
                    st.error(f"Error: {str(e)}")
