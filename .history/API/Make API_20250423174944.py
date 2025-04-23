from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np

leaf_deases_model = load_model('/home/tanmoy/Brac AI Hackathon/AgriBRACUtion/rice-diseases-detect/Training/model/rice_disease_model.h5')

# label_name = ['Apple scab','Apple Black rot', 'Apple Cedar apple rust', 'Apple healthy', 'Cherry Powdery mildew',
# 'Cherry healthy','Corn Cercospora leaf spot Gray leaf spot', 'Corn Common rust', 'Corn Northern Leaf Blight','Corn healthy', 
# 'Grape Black rot', 'Grape Esca', 'Grape Leaf blight', 'Grape healthy','Peach Bacterial spot','Peach healthy', 'Pepper bell Bacterial spot', 
# 'Pepper bell healthy', 'Potato Early blight', 'Potato Late blight', 'Potato healthy', 'Strawberry Leaf scorch', 'Strawberry healthy',
# 'Tomato Bacterial spot', 'Tomato Early blight', 'Tomato Late blight', 'Tomato Leaf Mold', 'Tomato Septoria leaf spot',
# 'Tomato Spider mites', 'Tomato Target Spot', 'Tomato Yellow Leaf Curl Virus', 'Tomato mosaic virus', 'Tomato healthy']

label_name = ['bacterial_leaf_blight','bacterial_leaf_streak','bacterial_panicle_blight','blast','brown_spot','dead_heart','downy_mildew','hispa','normal','tungro']

app = Flask(__name__)

@app.route("/",methods=['POST'])
def just():
    data = request.json
    img = np.array(data['img'])
    # Ensure image is normalized
    normalized_image = img / 255.0
    pridict_image = leaf_deases_model.predict(normalized_image.reshape((1, ) + img.shape ))

    return jsonify({"Label Name":label_name[np.argmax(pridict_image)],
                  "Accuracy": pridict_image[0][np.argmax(pridict_image)]*100})

if __name__ == "__main__":
    app.run(debug=True)