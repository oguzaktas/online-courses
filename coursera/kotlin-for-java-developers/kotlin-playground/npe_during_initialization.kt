open class A(val value: String) {
    init {
		value.length
    }
}

class B(override val value: String) : A(value)

fun main(args: Array<String>) {
    val b = B("a")
    println(b.value)
}