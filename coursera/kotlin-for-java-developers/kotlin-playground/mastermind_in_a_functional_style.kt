data class Evaluation(val rightPosition: Int, val wrongPosition: Int)

fun evaluateGuess(secret: String, guess: String): Evaluation {

    val rightPositions = secret.zip(guess).count { c -> c.first == c.second }

    val commonLetters = "ABCDEF".sumBy { ch ->

        Math.min(secret.count { it == ch }, guess.count { it == ch })
    }
    return Evaluation(rightPositions, commonLetters - rightPositions)
}

fun main(args: Array<String>) {
    val result = Evaluation(rightPosition = 1, wrongPosition = 1)
    evaluateGuess("BCDF", "ACEB") eq result
    evaluateGuess("AAAF", "ABCA") eq result
    evaluateGuess("ABCA", "AAAF") eq result
}

/*
fun evaluateGuess(secret: String, guess: String): Evaluation {
    val zipped = secret.zip(guess)
    val unmatched = zipped.filter { it.first != it.second }

    val (unmatchedSecrets, unmatchedGuesses) = unmatched.unzip()
    val remainingGuess = unmatchedSecrets.fold(unmatchedGuesses) { guesses, char ->
        guesses - char
    }
    val rightPositions = zipped.size - unmatched.size
    val wrongPositions = unmatchedGuesses.size - remainingGuess.size
    return Evaluation(rightPositions, wrongPositions)
}
*/