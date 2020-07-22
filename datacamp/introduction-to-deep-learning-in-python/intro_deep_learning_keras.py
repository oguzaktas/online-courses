# intro to building deep learning models with keras

import numpy as np
from keras.layers import Dense
from keras.layers import Sequential

predictors = np.loadtxt('predictors_data.csv', delimeter=',')

n_cols = predictors.shape[1]

model = Sequential()

model.add(Dense(100, activation='relu', input_shape=(n_cols,)))
model.add(Dense(100, activation='relu'))
model.add(Dense(1))