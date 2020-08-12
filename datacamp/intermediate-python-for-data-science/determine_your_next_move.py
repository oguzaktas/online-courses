'''
Instructions
- Roll the dice. Use randint() to create the variable dice.
- Finish the if-elif-else construct by replacing ___:
    - If dice is 1 or 2, you go one step down.
    - If dice is 3, 4 or 5, you go one step up.
    - Else, you throw the dice again. The number of eyes is the number of steps you go up.
- Print out dice and step. Given the value of dice, was step updated correctly?
'''

# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1, 7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice < 6 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)
