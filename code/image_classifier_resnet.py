import numpy as np
import matplotlib.pyplot as plt
from os import makedirs
from os.path import join, exists, expanduser

from keras.preprocessing import image
from keras.applications.resnet50 import ResNet50
from keras.applications.resnet50 import preprocess_input
from keras.applications.imagenet_utils import decode_predictions


# model = VGG16()

resnet = ResNet50(weights='imagenet')

img = image.load_img('./image/farm.jpg', target_size=(224, 224))
img = image.img_to_array(img)
plt.imshow(img / 255.)
x = preprocess_input(np.expand_dims(img.copy(), axis=0))
preds = resnet.predict(x)
label = decode_predictions(preds, top=5)

print(label[0])

# retrieve the most likely result, e.g. highest probability
label = label[0][0]

# print the classification
print('%s (%.2f%%)' % (label[1], label[2]*100))