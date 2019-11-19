import image
import sound

import sounddevice as sd
import soundfile as sf

predator_dict = {}

file = open('./../update_predators.txt', "r")

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
		print('Perdator Sound will be -> ' + predator_list[0])
		data, fs = sf.read('./../predator_sounds/' + predator_list[0] + '.wav', dtype = 'float32')
		sd.play(data, fs)
		status = sd.wait()


farm_image = './../dataset/test/temp/13.jpeg'
cow_image = './../dataset/test/temp/cow_10016.jpg'
deer_image = './../dataset/test/temp/deer_10021.jpg'
buffalo_image = './../dataset/test/temp/buffalo_10016.jpg'


cow_audio = './../sound_classifier/cow_test.wav'
deer_audio = './../sound_classifier/sikabuck3.wav'
wolf_audio = './../sound_classifier/redwolf.wav'




def printPredator(image_path, audio_path):
	image_label = image.getClass(image_path)
	audio_label = sound.getClass(audio_path)
	print('\n\n')
	print('Animal detected by image model -> ' + image_label)
	print('Animal detected by audio model -> ' + audio_label)
	getPredator(getPredatorList(image_label, audio_label))



printPredator(farm_image, cow_audio)
printPredator(farm_image, deer_audio)
# printPredator(deer_image, deer_audio)

