
import streamlit as st
import requests

st.title("Leaf Disease Detection")

uploaded_file = st.file_uploader(
    "Choose an image", type=["jpg", "jpeg", "png"])

api_url = "http://leaf-diseases-detect.vercel.app"

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    files = {"file": (uploaded_file.name,
                      uploaded_file.getvalue(), uploaded_file.type)}
    if st.button("Detect Disease"):
        with st.spinner("Sending image to API..."):
            try:
                response = requests.post(
                    f"{api_url}/disease-detection-file", files=files)
                if response.status_code == 200:
                    result = response.json()
                    if result.get("disease_detected"):
                        st.success("Disease Detected!")
                        st.markdown(f"### 🦠 Disease Name: **{result.get('disease_name', 'N/A')}**")
                        st.markdown(f"**Type:** {result.get('disease_type', 'N/A')}")
                        st.markdown(f"**Severity:** {result.get('severity', 'N/A')}")
                        st.markdown(f"**Confidence:** {result.get('confidence', 'N/A')}%")
                        st.markdown("---")
                        st.markdown("#### Symptoms:")
                        for symptom in result.get("symptoms", []):
                            st.markdown(f"- {symptom}")
                        st.markdown("#### Possible Causes:")
                        for cause in result.get("possible_causes", []):
                            st.markdown(f"- {cause}")
                        st.markdown("#### Treatment:")
                        for treat in result.get("treatment", []):
                            st.markdown(f"- {treat}")
                        st.markdown("---")
                        st.markdown(f"**Analysis Timestamp:** {result.get('analysis_timestamp', 'N/A')}")
                    else:
                        st.info("No disease detected.")
                        st.json(result)
                else:
                    st.error(f"API Error: {response.status_code}")
                    st.write(response.text)
            except Exception as e:
                st.error(f"Error: {str(e)}")
