fun main(args: Array<String>) {
    val s = "string"
    println(s as? Int)    // null
    println(s as Int?)    // exception (ClassCastException)
}