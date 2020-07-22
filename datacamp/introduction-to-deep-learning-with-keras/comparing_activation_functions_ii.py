'''
Instructions
- Create a pandas dataframe from val_loss_per_function.
- Call plot() on the dataframe.
- Create a pandas dataframe from val_acc_per_function.
- Once again, call plot() on the dataframe.
'''

# Create a dataframe from val_loss_per_function
val_loss = pd.DataFrame(val_loss_per_function)

# Call plot on the dataframe
val_loss.plot()
plt.show()

# Create a dataframe from val_acc_per_function
val_acc = pd.DataFrame(val_acc_per_function)

# Call plot on the dataframe
val_acc.plot()
plt.show()

'''
For every history callback of each activation function in activation_results:
- The history.history['val_loss'] has been extracted.
- The history.history['val_acc'] has been extracted.
- Both are saved in two dictionaries: val_loss_per_function and val_acc_per_function.
'''