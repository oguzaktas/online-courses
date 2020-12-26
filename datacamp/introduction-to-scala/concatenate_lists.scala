/* Instructions
- Create the venuesNTOA list using List().
- Create the venuesEuroTO list using the cons operator (::).
- Concatenate venuesNTOA and venuesEuroTO to create a new list named venuesTOWorld.
*/

// The original NTOA and EuroTO venue lists
val venuesNTOA = List("The Grand Ballroom", "Atlantis Casino", "Doug's House")
val venuesEuroTO = "Five Seasons Hotel" :: "The Electric Unicorn" :: Nil

// Concatenate the North American and European venues
val venuesTOWorld = venuesNTOA ::: venuesEuroTO