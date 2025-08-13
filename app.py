
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
                    st.success("Response from API:")
                    st.json(response.json())
                else:
                    st.error(f"API Error: {response.status_code}")
                    st.write(response.text)
            except Exception as e:
                st.error(f"Error: {str(e)}")
