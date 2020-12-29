fun isValidIdentifier(s: String): Boolean {
    if (s.contains('$')) {
        return false
    }
    if (s.length == 0) {
        return false
    }
    if (s.get(0) in 'a'..'z' || s.get(0) in 'A'..'Z' || s.get(0) in setOf('_', '$')) {
        return true
    } else {
        return false
    }
    /*
    fun isValidCharacter(c: Char) = c == '_' || c in '0'..'9' || c in 'a'..'z' || c in 'A'..'Z' // c.isLetterOrDigit()
    if (s.isEmpty() || s[0] in '0'..'9') return false
    for (c in s) {
        if (!isValidCharacter(c)) return false
    }
    return true
    */
}

fun main(args: Array<String>) {
    println(isValidIdentifier("name"))   // true
    println(isValidIdentifier("_name"))  // true
    println(isValidIdentifier("_12"))    // true
    println(isValidIdentifier(""))       // false
    println(isValidIdentifier("012"))    // false
    println(isValidIdentifier("no$"))    // false
}