/* Instructions
- Calculate the hand value for playerA, who has the following cards: queenDiamonds, threeClubs, aceHearts (worth 1), fiveSpades.
- Calculate the hand value for playerB, who has the following cards: kingHearts, jackHearts.
- Call the maxHand function, passing in handPlayerA and handPlayerB as arguments. 
Pass this function call into the println function to print out the maximum hand value.
*/

// Calculate hand values
val handPlayerA: Int = queenDiamonds + threeClubs + aceHearts + fiveSpades
val handPlayerB: Int = kingHearts + jackHearts

// Find and print the maximum hand value
println(maxHand(handPlayerA, handPlayerB))