'''
Instructions
- Add a Dense layer of 16 neurons with relu activation and input_shape being the total number of pixels of each image.
- Add a Dense layer with 10 outputs and softmax activation.
- Compile your model with adam, categorical_crossentropy, and accuracy metrics.
- Make sure your model works by predicting on X_train.
'''

# Instantiate a Sequential model
model = Sequential()

# Input and hidden layer with input_shape, 16 neurons, and relu 
model.add(Dense(16, input_shape = (64,), activation = 'relu'))

# Output layer with 10 neurons (one per digit) and softmax
model.add(Dense(10, activation='softmax'))

# Compile your model
model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

# Test if your model works and can process input data
print(model.predict(X_train))

'''
Output;

<script.py> output:
    [[1.57801419e-01 3.13342916e-08 1.17609663e-04 ... 2.88670161e-03
      1.75133277e-08 9.27261251e-04]
     [9.17966962e-01 4.87130869e-08 1.09600009e-08 ... 1.81080788e-04
      8.53955407e-06 9.01037129e-05]
     [9.99938369e-01 1.82372684e-09 9.08111347e-12 ... 2.19022222e-05
      2.59289088e-15 4.20937489e-08]
     ...
     [5.37219822e-01 5.52924506e-09 1.57055577e-10 ... 1.38584892e-05
      4.47214532e-09 1.09312405e-05]
     [2.70578653e-01 5.34917831e-07 8.48428527e-08 ... 1.55824000e-05
      4.48651798e-03 3.27920467e-02]
     [4.90147155e-03 2.87994535e-05 1.48348074e-04 ... 1.64761033e-04
      2.08042213e-04 1.32970810e-01]]
'''