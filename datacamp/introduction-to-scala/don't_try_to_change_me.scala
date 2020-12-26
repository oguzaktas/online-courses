/* Instructions
- Define playerA, playerB, and playerC as immutable variables with the strings "Alex", "Chen", and "Marta", respectively.
- Read the code that reassigns playerC to "Umberto". Click "Run Code" and observe the error.
- Delete the code that reassigns playerC to "Umberto".
- Change the original playerC variable definition from "Marta" to "Umberto".
*/

// Define immutable variables for player names
val playerA: String = "Alex"
val playerB: String = "Chen"
val playerC: String = "Umberto"

// Change playerC from Marta to Umberto
// playerC = "Umberto"

/* Output
cmd0.sc:6: reassignment to val
val res0_3 = playerC = "Marta"
                     ^Compilation Failed
*/