# Leaf Disease Detection Web App

A modern Streamlit web application for detecting leaf diseases from images using an AI-powered API.

## Features
- Upload leaf images and get instant disease analysis
- Beautiful, professional, and user-friendly interface
- Displays disease name, type, severity, confidence, symptoms, causes, and treatment

## How to Run
1. Install requirements:
   ```
   pip install -r requirements.txt
   ```
2. Start the main:
   ```
   streamlit run main.py
   ```
3. Upload a leaf image and view the results

## API Endpoint
- The app sends images to: `http://leaf-diseases-detect.vercel.app/disease-detection-file`
- Make sure your backend API is running and accessible

## Customization
- Edit `app.py` to change the API URL or UI styling

## License
MIT