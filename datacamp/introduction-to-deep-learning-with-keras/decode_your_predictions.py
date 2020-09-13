'''
Instructions
- Use texts_to_sequences() to turn the test_text parameter into a sequence of numbers.
- Get the model's next word prediction by passing in test_seq. The position representing the word with 
the highest probability is obtained by calling argmax(axis=1)[0] on the numpy array of predictions.
- Return the word associated to the prediction using the tokenizer's index_word dictionary.
'''

def predict_text(test_text):
  if len(test_text.split())!=3:
    print('Text input should be 3 words!')
    return False
  
  # Turn the test_text into a sequence of numbers
  test_seq = tokenizer.texts_to_sequences([test_text])
  test_seq = np.array(test_seq)
  
  # Get the model's next word prediction by passing in test_seq
  pred = model.predict(test_seq).argmax(axis = 1)[0]
  
  # Return the word associated to the predicted index
  return tokenizer.index_word[pred]