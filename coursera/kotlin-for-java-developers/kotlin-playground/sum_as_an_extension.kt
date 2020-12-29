fun List<Int>.sum(list: List<Int>): Int {
    var result = 0
    for (i in this) {
        result += i
    }
    return result
}

fun main(args: Array<String>) {
    val sum = listOf(1, 2, 3).sum()
    println(sum)    // 6
}