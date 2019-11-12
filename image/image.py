import os
import utils

from os import makedirs
from os.path import join, exists, expanduser

from image_classifier_resnet import resModel
from image_classifier_vgg import vggModel

# Path
slash = '/'
subclass = './subclasses'
test = './../dataset/test'
farm = './../dataset/farm'
bird = './../dataset/birds'
animal = './../dataset/animals'

TP = 0
FP = 0
TN = 0
FN = 0

# Dictionary that stores list of subclasses of class
subclass_dict = {}
for file in os.listdir(subclass):
	tempList = utils.readFile(subclass + slash + file)
	subclass_dict[file.split('.')[0]] = tempList

false_subclass = utils.readFile('./farm.txt')


def getClass(imagePath):
	tempvgg = vggModel(imagePath)
	tempres = resModel(imagePath)

	subclass_list = []

	for tup in tempvgg:
		subclass_list.append(tup[1])

	for tup in tempres:
		subclass_list.append(tup[1])

	for key in subclass_dict.keys():
		for one_subclass in subclass_list:
			if one_subclass in subclass_dict[key] or one_subclass in subclass_dict[key]:
				return key

	return 'false'




# print(getClass(farm + slash + '1.jpeg'))
# print(getClass(test + slash + 'dog.jpeg')