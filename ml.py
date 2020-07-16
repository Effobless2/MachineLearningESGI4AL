import numpy as np
import os
import cv2
from PIL import Image
import tensorflow as tf
from tensorflow import keras
from imageio import imread
import io
import base64

def hello(image, modelFileName):
	print(modelFileName)

	b64_bytes = base64.b64encode(image)
	b64_string = b64_bytes.decode()
	#print(image)
	img = imread(io.BytesIO(base64.b64decode(b64_string)))
	model = keras.models.load_model(modelFileName + ".h5")
	IMG_SIZE =32

	#open_cv_image = np.array(image)
	array_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	array_resize = cv2.resize(array_grayscale, (IMG_SIZE, IMG_SIZE))
	img_reshape = np.array(array_resize).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
	img_reshape = img_reshape/255.0

	prediction = model.predict(img_reshape)[0][0]
	prediction = int(round(prediction, 0))

	if prediction:
		print('chient')
		return "CHIEN"
	else:
		print('chiat')
		return "CHAT"