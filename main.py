import image_classifier/image
import sound_classifier/sound


predator_dict = {}

file = open('update_predators.txt', "r")

for line in file.read().split('\n'):
	predator_dict[line.split('-')[0]] = line.split('-')[1].split(',')

def commonMember(a, b): 
    a_set = set(a) 
    b_set = set(b) 
    if (a_set & b_set): 
        return list(a_set & b_set) 
    else: 
        return []

def getPredatorList(image_label, audio_label):
	if image_label in predator_dict.keys() and audio_label in predator_dict.keys():
		return commonMember(predator_dict[image_label], predator_dict[audio_label])
	elif image_label in predator_dict.keys():
		return predator_dict[image_label]
	elif audio_label in predator_dict.keys():
		return predator_dict[audio_label]
	else:
		return []


def getPredator(predator_list):
	if len(predator_list) == 0:
		print('Nothing Unusual')
	else:
		print(predator_list[0])


# print()