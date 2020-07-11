import numpy as np
import os
import cv2
from PIL import Image
import tensorflow as tf
from tensorflow import keras

def hello(image, modelFileName):
	model = keras.models.load_model(modelFileName + ".h5")
	IMG_SIZE =33

	open_cv_image = np.array(image)
	array_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	array_resize = cv2.resize(array_grayscale, (IMG_SIZE, IMG_SIZE))
	img_reshape = np.array(array_resize).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
	img_reshape = img_reshape/255.0

	prediction = model.predict(img_reshape)[0][0]
	prediction = int(round(prediction, 0))

	if prediction:
		return "CHIEN"
	else:
		return "CHAT"