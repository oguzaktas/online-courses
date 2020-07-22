'''
Instructions
- Summarize the model.
- Plot the model.
'''

# Import the plotting function
from keras.utils import plot_model
import matplotlib.pyplot as plt

# Summarize the model
model.summary()

# Plot the model
plot_model(model, to_file='model.png')

# Display the image
data = plt.imread('model.png')
plt.imshow(data)
plt.show()

'''
Output:
<script.py> output:
    _________________________________________________________________
    Layer (type)                 Output Shape              Param #   
    =================================================================
    Input-Layer (InputLayer)     (None, 1)                 0         
    _________________________________________________________________
    Output-Layer (Dense)         (None, 1)                 2         
    =================================================================
    Total params: 2
    Trainable params: 2
    Non-trainable params: 0
    _________________________________________________________________
'''