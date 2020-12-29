import kotlin.random.Random

val counter = 0
val foo: Int
    get() = counter++ // Random.nextInt()

fun main(args: Array<String>) {
    // The values should be different:
    println(foo)
    println(foo)
    println(foo)
}