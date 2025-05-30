fun main(args: Array<String>) {
    val s1: String? = null
    val s2: String? = ""
    s1?.isEmptyOrNull() eq true
    s2?.isEmptyOrNull() eq true

    val s3 = "   "
    s3.isEmptyOrNull() eq false
}

fun String?.isEmptyOrNull() = this == null || this.isEmpty() // fun isEmptyOrNull(s: String?) = s == null || s.isEmpty()

infix fun <T> T.eq(other: T) {
    if (this == other) println("OK")
    else println("Error: $this != $other")
}