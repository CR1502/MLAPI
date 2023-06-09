# import the necessary libraries

import numpy as np
import pandas as pd
import tensorflow as tf
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from keras.models import Sequential
from keras.layers import Dense

# Reading the data
heart_data = pd.read_csv('heart_disease_data.csv')

# Displaying a portion of the data
print(heart_data.head())

# Displaying information about the data
print(heart_data.info())

# Checking if there are any null elements in the dataset
print(heart_data.isnull().sum())

# Describing the data
print(heart_data.describe())

# Printing the count of the target values
print(heart_data['target'].value_counts())
# 1 --> Defective Heart
# 0 --> Healthy Heart

# Splitting the features and the targets
X = heart_data.drop(columns='target', axis=1)
y = heart_data['target']

print(X)

print(y)

# Splitting the data into Training data and Testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=2)

# Making an ANN model
model = Sequential()
model.add(Dense(128, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
optimizer = tf.keras.optimizers.Adam()
model.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])

history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2, shuffle=False)

# Evaluating the model on the test data
test_loss, test_acc = model.evaluate(X_test, y_test)
print("Test loss:", test_loss)
print("Test accuracy:", test_acc)

# Building a Predictive System
input_data = (62, 0, 0, 140, 268, 0, 0, 160, 0, 3.6, 0, 2, 2)

# change the input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the numpy array as we are predicting for only on instance
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if prediction[0] == 0:
    print('The Person does not have a Heart Disease')
else:
    print('The Person has Heart Disease')

# Saving the trained model
import pickle
import joblib
filename = 'heart_model.hdf5'
joblib.dump(prediction, filename)