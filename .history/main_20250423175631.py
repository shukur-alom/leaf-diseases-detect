import streamlit as st
import cv2 as cv
import numpy as np
import keras


label_name = ['bacterial_leaf_blight','bacterial_leaf_streak','bacterial_panicle_blight','blast','brown_spot','dead_heart','downy_mildew','hispa','normal','tungro']

st.write("""The leaf disease detection model is built using deep learning techniques, and it uses transfer learning to leverage the pre-trained knowledge of a base model. 
The model is trained on a dataset containing images of 10 different types of rice leaf diseases. 
""")              

st.write("Please upload a leaf image of rice. Otherwise, the model may not work correctly.")

model = keras.models.load_model('Training/model/rice_disease_model.h5')


uploaded_file = st.file_uploader("Upload an image")
if uploaded_file is not None:
    image_bytes = uploaded_file.read()
    img = cv.imdecode(np.frombuffer(image_bytes, dtype=np.uint8), cv.IMREAD_COLOR)
    resized_image = cv.resize(cv.cvtColor(img, cv.COLOR_BGR2RGB), (224, 224))
    normalized_image = np.expand_dims(resized_image / 255.0, axis=0)
    predictions = model.predict(normalized_image)
    st.image(image_bytes)
    if predictions[0][np.argmax(predictions)]*100 >= 80:
        st.write(f"Result is : {label_name[np.argmax(predictions)]}")
    else:st.write(f"Try Another Image")