/* Instructions
- Define a counter variable, i, equal to zero.
- Define the number of iterations for the while loop, numRepetitions, equal to three.
- Fill out the first if clause so "winner" is printed in the first iteration of the loop, 
then "winner" again in the second iteration, and "chicken dinner" in the final iteration.
- Increment the counter variable by one.
*/

// Define counter variable
var i = 0

// Define the number of loop iterations
var numRepetitions = 3

// Loop to print a message for winner of the round
while (i < numRepetitions) {
  if (i < 2)
    println("winner")
  else
    println("chicken dinner")
  // Increment the counter variable
  i = i + 1
}