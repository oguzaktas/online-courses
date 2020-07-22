'''
Instructions
- Use the model's .predict() method to predict from -10 to 10 minutes.
- Use the model's .predict() method to predict from -40 to 40 minutes.
'''

# Predict the twenty minutes orbit
twenty_min_orbit = model.predict(np.arange(-10, 11))

# Plot the twenty minute orbit 
plot_orbit(twenty_min_orbit)

# Predict the eighty minute orbit
eighty_min_orbit = model.predict(np.arange(-40, 41))

# Plot the eighty minute orbit 
plot_orbit(eighty_min_orbit)