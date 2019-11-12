import librosa 
from scipy.io import wavfile as wav
import numpy as np

Dict = {'cow': 0, 'deer':1, 'lion':2, 'wolf':3} 

filename = './cow/2605.wav' 

librosa_audio, librosa_sample_rate = librosa.load(filename) 
scipy_sample_rate, scipy_audio = wav.read(filename) 

print('Original sample rate:', scipy_sample_rate) 
print('Librosa sample rate:', librosa_sample_rate)

print('Original audio file min~max range:', np.min(scipy_audio), 'to', np.max(scipy_audio))
print('Librosa audio file min~max range:', np.min(librosa_audio), 'to', np.max(librosa_audio))


import matplotlib.pyplot as plt
# Original audio with 2 channels 
# plt.figure(figsize=(12, 4))
# plt.plot(librosa_audio)
# plt.show()


mfccs = librosa.feature.mfcc(y=librosa_audio, sr=librosa_sample_rate, n_mfcc=40)
print(mfccs.shape)

import librosa.display
librosa.display.specshow(mfccs, sr=librosa_sample_rate, x_axis='time')
# plt.show()


def extract_features(file_name):
   
    try:
        audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast') 
        mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
        mfccsscaled = np.mean(mfccs.T,axis=0)
        
    except Exception as e:
        print("Error encountered while parsing file: ", file)
        return None 
     
    return mfccsscaled


# Load various imports 
import pandas as pd
import librosa
from os import listdir
from os.path import isfile, join
# Set the path to the full UrbanSound dataset 
# fulldatasetpath = '/Volumes/Untitled/ML_Data/Urban Sound/UrbanSound8K/audio/'

# metadata = pd.read_csv('../UrbanSound Dataset sample/metadata/UrbanSound8K.csv')

features = []

# # Iterate through each sound file and extract the features 
# for index, row in metadata.iterrows():
    
#     file_name = os.path.join(os.path.abspath(fulldatasetpath),'fold'+str(row["fold"])+'/',str(row["slice_file_name"]))
    
#     class_label = row["class_name"]
#     data = extract_features(file_name)
    
#     features.append([data, class_label])

# Convert into a Panda dataframe

def getFeatures(className):
	mypath = "./" + className + "/"
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

	for fileName in onlyfiles:
		print (fileName)
		filePath = mypath + fileName
		data = extract_features(filePath)
		features.append([data, Dict[className]])

getFeatures("cow")
getFeatures("deer")
getFeatures("lion")
getFeatures("wolf")

featuresdf = pd.DataFrame(features, columns=['feature','class_label'])

print('Finished feature extraction from ', len(featuresdf), ' files')


from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical

# Convert features and corresponding classification labels into numpy arrays
X = np.array(featuresdf.feature.tolist())
y = np.array(featuresdf.class_label.tolist())

print("x")
print (X)
print ("y")
print (y)
# Encode the classification labels
# le = LabelEncoder()
# yy = to_categorical(le.fit_transform(y))

# print ("yy")
# print (yy)
# split the dataset 
from sklearn.model_selection import train_test_split 

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 42)

# training a linear SVM classifier 
from sklearn.svm import SVC 
svm_model_linear = SVC(kernel = 'linear', C = 1).fit(x_train, y_train) 
svm_predictions = svm_model_linear.predict(x_test) 
  
# model accuracy for X_test   
accuracy = svm_model_linear.score(x_test, y_test) 
print ("acc: ", accuracy)
# creating a confusion matrix 
# cm = confusion_matrix(y_test, svm_predictions) 