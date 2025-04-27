# Change the style to fivethirtyeight
plt.style.use('fivethirtyeight')

# Change the style to ggplot
plt.style.use('ggplot')

# Choose any of the styles
plt.style.use("bmh")

# Plot lines
plt.plot(data["Year"], data["Phoenix Police Dept"], label="Phoenix")
plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles")
plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia")

# Add a legend
plt.legend()

# Display the plot
plt.show()
