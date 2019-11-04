# Image Classifier

import os

from keras.applications.vgg16 import VGG16
from keras.utils.vis_utils import plot_model
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions


# load vgg16 model
vggmodel = VGG16()


def predictLabel(image_path):

	# load an image from file
	image = load_img(image_path, target_size=(224, 224))

	# convert the image pixels to a numpy array
	image = img_to_array(image)

	# reshape data for the model
	image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))

	# prepare the image for the VGG model
	image = preprocess_input(image)

	# predict the probability across all output classes
	yhat = vggmodel.predict(image)

	# convert the probabilities to class labels
	label = decode_predictions(yhat)

	# retrieve the most likely result, e.g. highest probability
	label = label[0][0]

	# print the classification
	# print('%s (%.2f%%)' % (label[1], label[2]*100))
	return label[1]



# -------------------------


# predictLabel('./../dataset/test/pig.jpg')

slash = '/'
bird = './../dataset/birds'
animal = './../dataset/animals'

Tcount = 0
Fcount = 0

for folder in os.listdir(animal):
	for file in os.listdir(animal + slash + folder):
		label = predictLabel(animal + slash + folder + slash + file)
		if label == folder:
			Tcount += 1
		else:
			Fcount += 1
			print(label)
			print(folder)
			print(file)
			print('\n\n')
	# break


print(Tcount)
print(Fcount)