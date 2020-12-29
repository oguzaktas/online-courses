package nicestring

fun String.isNice(): Boolean {
    var conditionList = emptyList<Boolean>()
    conditionList += !Regex("b[aeu]").containsMatchIn(this)
    conditionList += this.filter { it in "aeiou" }.count() >= 3
    conditionList += this.zipWithNext() { a, b -> a == b }.filter { it }.count() >= 1
    return conditionList.filter { it }.count() >= 2
}

/*
fun String.isNice(): Boolean {
    val predicates = listOf(
        ::doesNotContainPredefinedSubstrings,
        ::containsAtLeastThreeVowels,
        ::containsDoubleLetter
    )
    return predicates.count { run(it) } >= 2
}

private fun String.doesNotContainPredefinedSubstrings(): Boolean {
    val containsPredefinedStrings = this.contains("bu", true)
            || this.contains("ba", true)
            || this.contains("be", true)
    return !containsPredefinedStrings
}

private fun String.containsAtLeastThreeVowels(): Boolean {
    return this.count { it == 'a' || it == 'e' || it == 'i' || it == 'o' || it == 'u' } >= 3
}

private fun String.containsDoubleLetter(): Boolean {
    for (i in 0 until this.length - 1) {
        if (this[i] == this[i + 1]) return true
    }
    return false
}
*/

/*
fun String.isNice(): Boolean {
    val condition1 = !contains("b[uae]".toRegex())
    val condition2 = count { it in "aeiou" } >= 3
    val condition3 = zipWithNext().any { (a, b) -> a == b }
    return listOf(condition1, condition2, condition3).count { it } >= 2
}
*/

/*
fun String.isNice(): Boolean {
    val noBadSubstring = !contains("ba") && !contains("be") && !contains("bu")
    // val noBadSubstring = setOf("ba", "be", "bu").all { !this.contains(it) }
    // val noBadSubstring = setOf("ba", "be", "bu").none { this.contains(it) }

    val hasThreeVowels = count { it in setOf('a', 'e', 'i', 'o', 'u') } >= 3
    // val hasThreeVowels = count { it in "aeiou" } >= 3

    val hasDouble = false
    if (length > 1) {
        var prevCh: Char? = null
        for (ch in this) {
            if (ch == prevCh)
                hasDouble = true
            prevCh = ch
        }
    }
    // (0 until lastIndex).any { this[it] == this[it + 1] }
    // zipWithNext().any { it.first == it.second }
    // windowed(2).any { it[0] == it[1] }


    return listOf(noBadSubstring, hasThreeVowels, hasDouble).filter { it == true }.size >= 2
    // return listOf(noBadSubstring, hasThreeVowels, hasDouble).count { it } >= 2
    /*
    var conditions = 0
    if (noBadSubstring) conditions++
    if (hasThreeVowels) conditions++
    if (hasDouble) conditions++
    return conditions >= 2
    */
*/