import os

from os import makedirs
from os.path import join, exists, expanduser


from image_classifier_resnet import resModel
from image_classifier_vgg import vggModel


slash = '/'
bird = './../dataset/birds'
animal = './../dataset/animals'

Tcount = 0
Fcount = 0


# for folder in os.listdir(bird):
# 	count = 0
# 	for file in os.listdir(bird + slash + folder):
# 		label = resModel(bird + slash + folder + slash + file)


# 		if label == folder:
# 			Tcount += 1
# 		else:
# 			Fcount += 1
# 			print(label)
# 			print(folder)
# 			print(file)
# 			print('\n')
# 		count += 1
# 	break


# print(Tcount)
# print(Fcount)


print(resModel('./../dataset/test/dog.jpeg'))
print(vggModel('./../dataset/test/dog.jpeg'))


# print(len(tempList))

# with open('your_file.txt', 'w') as f:
#     for item in tempList:
#         f.write("%s\n" % item)