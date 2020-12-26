/* Instructions
- Read the provided code, then fill in the type annotation for the informPlayer variable.
- Write appropriate if, else if, and else conditions based on the provided code.
- Change fiveSpades to fourSpades, then click "Run Code" and observe the output.
- Change fourSpades to threeSpades, then click "Submit Answer".
*/

// Point value of a player's hand
val hand = sevenClubs + kingDiamonds + threeSpades

// Inform a player where their current hand stands
val informPlayer: String = {
  if (hand > 21)
    "Bust! :("
  else if (hand == 21)
    "Twenty-One! :)"
  else
    "Hit or stay?"
}

// Print the message
print(informPlayer)