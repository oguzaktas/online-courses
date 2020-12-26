/* Instructions
- Write code that accomplishes the following: if a player's hand is equal to 21, print "Twenty-One!" to output.
- Click "Run Code" and observe the output.
- Change fourSpades to threeSpades, then click "Submit Answer".
*/

// Point value of a player's hand
val hand = sevenClubs + kingDiamonds + threeSpades

// Congratulate the player if they have reached 21
if (hand == 21) {
    println("Twenty-One!")
}