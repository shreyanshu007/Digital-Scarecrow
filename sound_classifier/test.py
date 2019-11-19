import librosa 
from scipy.io import wavfile as wav
import numpy as np
import os
import pandas as pd
import librosa
from os import listdir
from os.path import isfile, join


filePath = '22475.wav'


d = '.'
animalClassList = [o for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))]
RevDict = dict()

for i in range(len(animalClassList)):
	RevDict[i]=animalClassList[i]
	# {'cow': 0, 'deer':1, 'lion':2, 'wolf':3} 


def extract_features(file_name):
   
    try:
        audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast') 
        mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
        mfccsscaled = np.mean(mfccs.T,axis=0)
        
    except Exception as e:
        print("Error encountered while parsing file: ", file_name)
        return None 
     
    return mfccsscaled



data = extract_features(filePath)
features = []
features.append([data])
featuresdf = pd.DataFrame(features, columns=['feature'])


from sklearn.preprocessing import LabelEncoder

# Convert features and corresponding classification labels into numpy arrays
X = np.array(featuresdf.feature.tolist())

from sklearn.externals import joblib 

# Load the model from the file 
svm_from_joblib = joblib.load('trained_data.pkl')  
  
# Use the loaded model to make predictions 
predicted_class = svm_from_joblib.predict(X)

# model predict  
print(predicted_class)
print ( RevDict[predicted_class[0]])