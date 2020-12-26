/* Instructions
- Initialize a list named prizes with an element for each round's prize, where 
the first through fifth round's prizes are 10, 15, 20, 25, and 30, respectively.
- Prepend to prizes using the cons (::) operator so a new first round is added, worth $5. Name the new list newPrizes.
*/

// Initialize a list with an element for each round's prize
val prizes = List(10, 15, 20, 25, 30)
println(prizes)

// Prepend to prizes to add another round and prize
val newPrizes = 5 :: prizes
println(newPrizes)