import librosa 
from scipy.io import wavfile as wav
import numpy as np
import os


d = '.'
animalClassList = [o for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))]
Dict = dict()

for i in range(len(animalClassList)):
	Dict[animalClassList[i]]=i
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


# Load various imports 
import pandas as pd
import librosa
from os import listdir
from os.path import isfile, join

features = []


def getFeatures():
	for className in animalClassList:
		mypath = "./" + className + "/"
		onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

		for fileName in onlyfiles:
			print (fileName)
			filePath = mypath + fileName
			data = extract_features(filePath)
			features.append([data, Dict[className]])



getFeatures()

featuresdf = pd.DataFrame(features, columns=['feature','class_label'])

print('Finished feature extraction from ', len(featuresdf), ' files')


from sklearn.preprocessing import LabelEncoder

# Convert features and corresponding classification labels into numpy arrays
X = np.array(featuresdf.feature.tolist())
y = np.array(featuresdf.class_label.tolist())

print("x")
print (X)
print ("y")
print (y)


from sklearn.model_selection import train_test_split 

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state = 42)

# training a linear SVM classifier 
from sklearn.svm import SVC 
svm_model_linear = SVC(kernel = 'linear', C = 1, probability = True).fit(x_train, y_train) 
svm_predictions = svm_model_linear.predict(x_test) 
  
# model accuracy for X_test   
accuracy = svm_model_linear.score(x_test, y_test) 
print ("acc: ", accuracy)


from sklearn.externals import joblib 
  
# Save the model as a pickle in a file 
joblib.dump(svm_model_linear, 'trained_data.pkl') 
