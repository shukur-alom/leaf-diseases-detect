import requests
import numpy as np
from keras.preprocessing.image import load_img,img_to_array

url = 'http://127.0.0.1:5000/'

img = img_to_array(load_img('DanLeaf2.jpg',target_size=(150,150,3)))

r = requests.post(url, json={'img':img.tolist()})

print(f"\n\n{r.json()}\n\n")