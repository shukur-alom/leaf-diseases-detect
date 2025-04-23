from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np

leaf_deases_model = load_model('/home/tanmoy/Brac AI Hackathon/AgriBRACUtion/rice-diseases-detect/Training/model/rice_disease_model.h5')


label_name = ['bacterial_leaf_blight','bacterial_leaf_streak','bacterial_panicle_blight','blast','brown_spot','dead_heart','downy_mildew','hispa','normal','tungro']

app = Flask(__name__)

@app.route("/",methods=['POST'])
def just():
    data = request.json
    img = np.array(data['img'])
    # Ensure image is normalized
    normalized_image = img / 255.0
    # pridict_image = leaf_deases_model.predict(img.reshape((1, ) + img.shape ))
    pridict_image = leaf_deases_model.predict(normalized_image.reshape((1, 224, 224, 3)))
    return jsonify({"Label Name":label_name[np.argmax(pridict_image)],
                  "Accuracy": pridict_image[0][np.argmax(pridict_image)]*100})

if __name__ == "__main__":
    app.run(debug=True)