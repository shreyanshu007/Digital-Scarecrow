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


def testImage():

	TP = 0
	FP = 0
	TN = 0
	FN = 0

	for folder in os.listdir(animal):
		count = 0
		for file in os.listdir(animal + slash + folder):
			if count > 5:
				break
			if getClass(animal + slash + folder + slash + file) == folder:
				TP += 1
			else:
				FN += 1
			count += 1

	for folder in os.listdir(bird):
		count = 0
		for file in os.listdir(bird + slash + folder):
			if count > 2:
				break
			if getClass(bird + slash + folder + slash + file) == 'bird':
				TP += 1
			else:
				FN += 1
			count += 1

	for file in os.listdir(farm):
		if getClass(farm + slash + file) == 'false':
			TN += 1
		else:
			FP += 1


	print('\nTP')
	print(TP)
	print('\nTN')
	print(TN)
	print('\nFP')
	print(FP)
	print('\nFN')
	print(FN)




testImage()



'''
TP
627

TN
13

FP
7

FN
63
'''

# Accuracy = 90.14

# Precision = 98.95

# Recall = 90.86

