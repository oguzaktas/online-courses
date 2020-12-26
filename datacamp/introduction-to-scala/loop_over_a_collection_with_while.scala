/* Instructions
- Define a counter variable, i. Set it equal to zero to start.
- Using the counter variable i, write a while loop that proceeds through the loop hands.length times.
- Find and print the winning hand's value for the ith hand.
- Increment the counter variable.
*/

// Define counter variable
var i = 0

// Create list with five hands of Twenty-One
var hands = List(16, 21, 8, 25, 4)

// Loop through hands
while (i < hands.length) {
  // Find and print number of points to bust
  println(pointsToBust(hands(i)))
  // Increment the counter variable
  i = i + 1
}