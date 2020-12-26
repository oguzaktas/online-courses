/* Instructions
- Write an if condition: if the hand busts, make the Int 0 the result of the function.
- Write an else condition: if the hand does not bust, subtract hand from 21 and make that difference the result of the function.
- Call pointsToBust with a hand with the cards tenSpades and fiveClubs as the argument.
*/

// Find the number of points that will cause a bust
def pointsToBust(hand: Int): Int = {
  // If the hand is a bust, 0 points remain
  if (hand > 21)
    0
  // Otherwise, calculate the difference between 21 and the current hand
  else
    21 - hand
}

// Test pointsToBust with 10♠ and 5♣
val myHandPointsToBust = pointsToBust(tenSpades + fiveClubs)
println(myHandPointsToBust)