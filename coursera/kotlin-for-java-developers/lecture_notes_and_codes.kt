import java.awt.Point
import java.io.IOException
import java.lang.IllegalArgumentException
import java.lang.IllegalStateException
import java.lang.StringBuilder
import java.math.BigInteger
import java.util.concurrent.locks.Lock
import javax.sound.midi.MidiDeviceReceiver
import kotlin.reflect.typeOf
import kotlin.random.Random
import kotlin.sequences.Sequence

fun main(args: Array<String>) {
    println("Hello World!")
    println("shfsjakdgvege")
    displaySeparator()
    println()
    displaySeparator('#', 5)
    println()
    println(sum(a = 1, b = 2))
    val list = listOf("a", "b", "c", "d", "e")
    val map = mapOf(1 to "one",
                    2 to "two",
                    3 to "three")
    for (c in list) {
        print("$c ")
    }
    println()
    for ((key, value) in map) {
        println("$key = $value")
    }
    for (i in 1..9) {
        print(i)
    }
    println()
    for (i in 1.until(9)) { // excluding upper bound
        print(i)
    }
    println()
    for (i in 9 downTo 1 step 2) {
        print(i)
    }
    println()
    for (c in "abc") {
        println(c + 1)
    }
    println(isLetter('*'))
    println(isLetter('a'))
    println(isNotDigit('1'))
    println(recognizeChar('*'))
    println(recognizeChar('1'))
    println("Kotlin" in setOf("Java", "Scala"))
    var number = 10
    val percentage = if (number in 0..100)
        number
    else
        throw IllegalArgumentException("A percentage value must be between 0 and 100: $number")
    try {
        foo()
    } catch(e : IOException) {
        println("IOException")
    }
    val c: Char = "abc".lastChar()
    println(c)
    println("string".repeat(2))
    val set = hashSetOf(1, 2, 3, 4)
    val list2 = arrayListOf(1, 2, 3, 4)
    val map2 = hashMapOf(1 to "one", 2 to "two")
    println(set.javaClass)
    println(list2.javaClass)
    println(map2.javaClass)
    // Kotlin library (extensions on collections) -> filter, map, reduce, count, find, any, flatMap, groupBy
    println(listOf('a', 'b', 'c').joinToString(separator = "", prefix = "(", postfix = ")"))
    val list3 = listOf("a", "b", "c", "d")
    for ((index, element) in list3.withIndex()) {
        println("$index $element")
    }
    println("Answer" to 1)
    println('%'.isLetterOrDigit())
    val q = """to code, 
        |or not to code?""".trimMargin(marginPrefix = "#")
    println(q)
    val a = q.trimIndent()
    println(a)
    val regex = "\\d{2}\\.\\d{2}\\.\\d{4}".toRegex()
    println(regex.matches("15.02.2016"))
    println(regex.matches("15.02.16"))
    println("1e-10".toDouble())
    println("xx".toIntOrNull())
    fun getAnswer() = 42
    println(getAnswer() eq 42)
    println(getAnswer() eq 43)
    // 'a' to 1.0 is type of Pair<Char, Double>
    val pair: Pair<Char, Double> = 'a' to 1.0
    val parent: Parent = Child()
    println(parent.foo())
    println("abc".get(0))
    println(A().foo(2))
    val s1: String = "not null"
    val s2: String? = "can be null or non-null"
    val s3: String? = null
    println(s1.length)
    if (s3 != null) {
        println(s3.length)
    }
    val length = s2?.length // val length = if (s1 != null) s1.length else null
    // length's type is nullable int (Int?)
    val length2: Int? = s2?.length ?: 0 // if (s2 != null) s2.length else 0
    val a1: Int? = null
    val b1: Int? = 1
    val c1: Int = 2
    val s4 = (b1 ?: 0) + c1
    println(s4)
    // s!! throws NullPointerException if s is null
    println(isFoo2(null))
    // Nullable types are implemented using @Nullable, @NotNull annotations
    println(s1.isNullOrEmpty())
    println(s1.isEmptyOrNull())
    val s5 = "string"
    println(s5 as? Int)
    val employees: List<Employee>
    /*
    employees.filter { it.city == "Prague" }
        .map { it.age }
        .average()
    */
    // Lambda syntax: { x: Int, y: Int -> x + y }
    // list.any({ i: Int -> i > 0 }) or list.any { i: Int -> i > 0 } (empty parentheses can be omitted)
    /* Multi-line lambda
    list.any {
        println("processing $it")
        it > 0 (the last expression is the result)
    }
    */
    map.mapValues { entry -> "${entry.key} -> ${entry.value}!" } // map.mapValues { (key, value) -> "$key -> $value!" }
    map.mapValues { (_, value) -> "$value!" } // if one of the parameters is not used, it can be replaced with underscore
    val heroes = listOf(Hero("The Captain", 60, Gender.MALE),
        Hero("Frenchy", 42, Gender.MALE),
        Hero("The Kid", 9, null),
        Hero("Lady Lauren", 29, Gender.FEMALE),
        Hero("First Mate", 29, Gender.MALE),
        Hero("Sir Stephen", 37, Gender.MALE))
    println(heroes.last().name)
    println(heroes.firstOrNull{ it.age == 30 }?.name)
    println(heroes.map{ it.age }.distinct())
    println(heroes.filter{ it.age < 30 }.size)
    val (youngest, oldest) = heroes.partition{ it.age < 30 }
    println(oldest.map{ it.name })
    println(heroes.maxBy { it.age }?.name)
    println(heroes.minBy { it.age }?.name)
    println(heroes.all { it.age < 50 })
    println(heroes.any { it.gender == Gender.FEMALE })
    val mapByAge: Map<Int, List<Hero>> = heroes.groupBy { it.age }
    val (age, group) = mapByAge.maxBy { (_, group) -> group.size }!!
    println(age)
    val mapByName: Map<String, Hero> = heroes.associateBy { it.name }
    println(mapByName["Frenchy"]?.age)
    println(mapByName.getValue("Frenchy").age)
    // println(mapByName.getValue("unknown").age) -> NoSuchElementException
    val unknownHero = Hero("unknown", 0, null)
    println(mapByName.getOrElse("unknown") { unknownHero }.age)
    val mapByName2 = heroes.associate { it.name to it.age }
    println(mapByName2.getOrElse("unknown2") { 0 })
    val (first, second) = heroes.flatMap { first -> heroes.map { hero -> first to hero } }
        .maxBy { it.first.age - it.second.age }!!
    println(first.name)
    val allPossiblePairs = heroes.flatMap { first -> heroes.map { second -> first to second } } // Simplifyig the first code
    val (first2, second2) = allPossiblePairs.maxBy { it.first.age - it.second.age }!!
    println(first2.name)
    val oldest2 = heroes.maxBy { it.age }
    val youngest2 = heroes.minBy { it.age }
    println(youngest2?.name)
    val isEven = { i: Int -> i % 2 == 0 } // val isEven: (Int) -> Boolean = { i: Int -> i % 2 == 0 }
    val list4 = listOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    println(list4.any(isEven))
    println(list4.filter(isEven))
    run { println("hey") } // Calling lambda directly
    // val f1: () -> Int? = null // Does not compile, return type should be nullable
    val f2: () -> Int? = { null }
    val f3: (() -> Int)? = null
    // val f4: (() -> Int)? = { null } // Does not compile
    val f5:(() -> Int)? = run { { 42 } }
    /* Calling nullable function;
    1. if (f != null) { f() }
    2. f?.invoke()
    */
    // Member reference usage -> people.maxBy(Person::age)
    val predicate = { i: Int -> isEven(i) } // val predicate = ::isEven (function reference)
    val person = Person("Person", 29)
    println(person.isOlder(30))
    val agePredicate: (Int) -> Boolean = { ageLimit -> person.isOlder(ageLimit) }
    println(agePredicate(20))
    println(duplicateNonZero(listOf(3, 0, 5)))
    println(duplicateNonZeroLocalFunction(listOf(1, 2, 0, 3)))
    println(duplicateNonZero2(listOf(0, 1, 2)))
    /*
    list.forEach {
        if (it == 0) return@forEach
        print(it)
    }
    the same as;
    for (element in list) {
        if (element == 0) continue
        print(element)
    }
    */
    // return inside forEach does not correspond to break inside for loop
    val rectangle = Rectangle(2, 3);
    println(rectangle.isSquare)
    println("$foo1")
    val lengthCounter = LengthCounter()
    lengthCounter.addWord("Hello")
    println(lengthCounter.counter)
    println(Random.nextInt())
    println("string".indices)
    val s6 = "abcde"
    println(s6.medianChar)
    println(s6.medianChar)
    val sb = StringBuilder("Kotlin?")
    sb.lastChar = '!'
    println(sb)
    println(lazyValue)
    println(lazyValue) // After the first time, the stored value is returned
    // lateinit var myData: MyData -> lateinit cannot be val, cannot be final, cannot be nullable, cannot be primitive type
    /* public, final -> default. open = explicit non-final. There is no package private visibility in Kotlin.
    internal = visible in the same module.
    set of Kotlin files compiled together (IntelliJ IDEA module, Maven project or a Gradle source set)
    open modifier -> can be overridden
    abstract modifier -> must be overridden (can't have an implementation)
    internal class member or top-level declaration is visible in the same module
    protected class member is visible in the class and its subclasses
    private top-level declaration is visible in the same file
    public - internal (visible in the module) - protected (visible in subclasses) - private
    private class member -> visible in the class only, private declaration -> visible in the same file
    */
    Child2()
    println()
    println(Color2.BLUE.r)
    println(Color2.RED.rgb())
    val contact = Contact("name", "address")
    contact.copy(address = "new address")
    // for data classes, == calls equals method, and === checks reference equality
    // == checks reference equality in default classes
    // sealed class modifier -> restricts class hierarchy, all subclasses must be located in the same file
    // by keyword -> implementing an interface by delegating to...
    KSingleton.foo()
    println(A2.foo())
    // Companion object can implement an interface
    A3.create()
    C.bar()
    // inner modifier cannot be used with object
    // const -> for primitive types and String (compile-time constant), @JvmField -> eliminates accessors
    println(oneHalf(null))
    println(oneHalf(13))
    // public and final -> default
    println(Point(1, 2) * 3)
    println(5.div(2))
    println(5.unaryMinus())
    println(5.inc()) // ++a, a++
    println(5.dec()) // --a, a--
    println(5.plusAssign(5))
    val mutableList = mutableListOf(1, 2, 3)
    mutableList += 4
    println(mutableList)
    val oneTo100: IntRange = 1..100
    println(BigInteger.TEN.plus(BigInteger.ONE))
    // Kotlin relies on naming conventions rather than interfaces
    // Some useful library functions -> run, let, takeIf, takeUnless, repeat, withLock, use
    /* let -> allows to check the argument for being non-null, not only the receiver
    if (email != null) sendEmailTo(email) or email?.let { e -> sendEmailTo(e) }
    getEmail()?.let{ sendEmailTo(it) } // the type of it is Email? (nullable email)
    */
    /* takeIf function -> returns the receiver object if it satisfies the given predicate, otherwise returns null
    issue.takeIf { it.status == FIXED }
    person.patronymicName.takeIf(String::isNotEmpty)
    issues.filter { it.status == OPEN }.takeIf(List<Issue>::isNotEmpty)?.let { println("There are some open issues") }
    */
    /* takeUnless function -> returns the receiver object if it does not satisfy the given predicate, otherwise returns null
    person.patronymicName.takeUnless(String?::isNullOrEmpty)
    */
    repeat(2) {
        println("Hello")
    }
    // Lambdas are inlined (no performance overhead), but intermediate collections are created for chained calls
    // Kotlin sequences (similar to Java 8 streams). Collections -> eager operation, sequences -> lazy evaluation
    val list5 = listOf(1, 2, -3, 4, 5, 0)
    val maxOddSquare = list5.asSequence().map { it * it }.filter { it % 2 == 1 }.max() // with sequence there is no intermediate collection created
    println(maxOddSquare)
    val list6 = listOf(1, 2, 3, 4)
    println(list6.asSequence().filter(::f).map(::m).toList()) // f1 f2 m2 f3 f4 m4
    // List, Set -> Collection -> Iterable
    // yield is not a built-in language feature, it's a regular library function in Kotlin.
    val numbers = sequence {
        var x = 0
        while (true) {
            yield(x++)
        }
    }
    println(numbers.take(5).toList())
    println(mySequence().map { it * it }.filter { it > 10 }.take(1)) // take is not a terminal operation, it's a intermediate operation
    println(mySequence().map { it * it }.filter { it > 10 }.first())
    println(fibonacci().take(10).toList())
    /*
    people.filter { it.age < 21 }.size -> can be simplified with -> people.count { it.age < 21 }
    people.sortedBy { it.age }.reversed() -> can be simplified with -> people.sortedByDescending { it.age }
    people.map { person -> person.takeIf { it.isPublicProfile }?.name}.filterNotNull() -> can be simplified with -> people.mapNotNull { person.takeIf { it.isPublicProfile }?.name }
    people.asSequence().groupBy { it.age }.mapValues { (_, group) -> group.size } -> can be simplified with -> people.asSequence().groupingBy { it.age }.eachCount()
    */
    val sb2 = StringBuilder()
    with (sb2) { // with is a regular function defined in the standard library
        appendln("Alphabet: ")
        for (c in 'a'..'z') {
            append(c)
        }
        toString()
    }
    println(sb2)
    // Lambda with receiver = lambda with implicit this
    // Regular function - extension function - regular lambda - lambda with receiver (extension lambda)
    val isOdd: Int.() -> Boolean = { this % 2 == 1 }
    println(isOdd(1))
    println(2.isOdd())
    // Any is (similar to Java Object class) is supertype of reference and primitive types in Kotlin
    val g: (() -> Int)? = null
    g?.invoke()
    println(arrayOf(1, 2) == arrayOf(1, 2))
    println(arrayOf(0, 1).contentEquals(arrayOf(1, 2)))
    // Unit instead of void
    // Nothing is different to Unit/void -> Nothing means this function never returns
    // Unit -> the function completes successfully, Nothing -> the function never completes
    // throw IllegalStateException(), return, TODO("Needs to be done") -> These expressions have Nothing type
    val answer2: Any = if (true) {
        42
    } else {
        fail("Not ready")
    }
    println(answer2)
    // In Kotlin bytecode, Nothing type is replaced with Java void
    // Nothing? -> const null
    val users: List<Nothing?> = mutableListOf(null)
    // Nullable types are implemented with @Nullable, @NotNull annotations
    // Preventing NullPointerException -> annotate your Java types or specify types explicitly
    /* kotlin.collections.List -> read-only (read-only is not the same as immutable) List, kotlin.collections.MutableList
    Read-only interface just lacks mutating methods. The actual list can be changed by another reference
    */
    val mutableList2 = mutableListOf(1, 2, 3)
    val list7: List<Int> = mutableList2
    mutableList2.add(4)
    println(list7)
    // java.util.ArrayList -> kotlin.MutableList -> kotlin.List
}

fun infiniteLoop(): Nothing {
    while (true) {

    }
}

fun fail(message: String): Nothing {
    throw IllegalStateException(message)
}

inline fun <T> T.also(block: (T) -> Unit): T { block(this); return this }

inline fun <T, R> with(
    receiver: T,
    block: T.() -> R
): R = receiver.block()

inline fun buildString(
    builderAction: StringBuilder.() -> Unit): String {
    val stringBuilder = StringBuilder()
    stringBuilder.builderAction()
    return stringBuilder.toString()
}

fun fibonacci(): Sequence<Int> = sequence {
    var elements = Pair(0, 1)
    while (true) {
        yield(elements.first)
        elements = Pair(elements.second, elements.first + elements.second)
    }
}

fun mySequence() = sequence {
    println("yield one element")
    yield(1)
    println("yield a range")
    yieldAll(3..5)
    println("yield a list")
    yieldAll(listOf(7, 9))
}

interface Sequence<out T> {
    operator fun iterator(): Iterator<T>
}

fun m(i: Int): Int {
    print("m$i ")
    return i * i
}

fun f(i: Int): Boolean {
    print("f$i ")
    return i % 2 == 0
}

inline fun <T> Lock.withLock(action: () -> T): T {
    lock()
    try {
        return action()
    } finally {
        unlock()
    }
}

inline fun <R> run(block: () -> R): R = block()

inline fun <T> T.takeUnless(predicate: (T) -> Boolean): T? =
    if (!predicate(this)) this else null

operator fun BigInteger.plus(other: BigInteger) = this.add(other)

// data class Pair<A, B>(val first: A, val second: B)
data class IndexedValue<T>(val index: Int, val value: T)

private fun Int.plusAssign(i: Int): Any? {
    return this + i
}

operator fun Point.times(scale: Int): Point {
    return Point(x * scale, y * scale)
}

/*
interface List<out E> {
    fun get(index: Int): E
}
*/

inline fun <reified R> List<*>.filterIsInstance() {}

fun <T: Number?> oneHalf(value: T): Double? {
    if (value == null) return null
    return value.toDouble() / 2.0
}

fun <T: Any> foo(list: List<T>) { // <T: Any> non-nullable upper bound
    for (element in list) {

    }
}

fun <T> List<T>.firstOrNull(): T? { return null }

fun <T> List<T>.filter(predicate: (T) -> Boolean): ArrayList<T> {
    val d = ArrayList<T>()
    for (element in this) {
        if (predicate(element)) d.add(element)
    }
    return d
}

/*
interface List<E> {
    fun get(index: Int): E
}
*/

const val answer = 42

@JvmField
val prop = MyClass() // same as static property in Java


object Obj {
    @JvmStatic fun foo() {}
    fun bar() {}
}

class C {
    companion object {
        @JvmStatic fun foo() {}
        fun bar() {}
    }

    object B
}

interface Factory<T> {
    fun create(): T
}

class A3 {
    private constructor()

    companion object : Factory<A> {
        override fun create(): A {
            return A()
        }
    }
}

class A2 {
    companion object { // Companion objects can be used static methods like in Java
        fun foo() = 1
    }
}

object KSingleton {
    fun foo() {
        println("object")
    }
}

class A1 {
    class B1
    inner class C1 {
        //
    }
}

sealed class Expr
class Num(val value: Int) : Expr()
class Sum(val left: Expr, val right: Expr) : Expr()

fun eval(e: Expr): Int = when (e) {
    is Num -> e.value
    is Sum -> eval(e.left) + eval(e.right)
    // else -> throw IllegalArgumentException("Unknown expression") // not necessary with sealed modifier
}

data class Bar(val first: Int, val second: Int) {
    override fun equals(other: Any?): Boolean {
        if (this == other) return true
        if (other !is Bar) return false
        return (first == other.first && second == other.second)
    }

    override fun hashCode(): Int {
        return first * 31 + second
    }
}

data class Contact(val name: String, val address: String)

enum class Color2(
    val r: Int, val g: Int, val b: Int
) {
    BLUE(0, 0, 255), ORANGE(255, 165, 0), RED(255, 0, 0);

    fun rgb() = (r * 256 + g) * 256 + b
}

open class Parent2 {
    init { print("parent class") }
}

class Child2: Parent2() {
    init { print("child class") }
}

class MyClass {
    lateinit var lateinitVar: String

    init { // Constructor body

    }

    fun initializationLogic() {
        println(this::lateinitVar.isInitialized) // false
        lateinitVar = "value"
        println(this::lateinitVar.isInitialized) // true
    }
}

val lazyValue: String by lazy { // Lazy property
    println("Computed!")
    "Hello"
}

var StringBuilder.lastChar: Char // Mutable extension property
    get() = get(length - 1)
    set(value: Char) {
        this.setCharAt(length - 1, value)
    }

val String.medianChar
    get(): Char? {
        println("Calculating...")
        return getOrNull(length / 2)
    }

val String.lastIndex: Int // Extension property
    get() = this.length - 1

val String.indices: IntRange
    get() = 0..lastIndex

interface Session {
    val user: User
}

fun analyzeUserSession(session: Session) {
    if (session.user is FacebookUser) {
        println(session.user.nickname) // Compiler error: Smart cast to 'FacebookUser' is impossible
    }
}

interface User {
    val nickname: String
}

class FacebookUser(val accountId: Int): User {
    override val nickname: String
        get() = TODO("Not yet implemented")
}

class LengthCounter {
    var counter: Int = 0
        private set
    fun addWord(word: String) {
        counter += word.length
    }
}

class StateLogger {
    var state = false
        set(value) {
            println("State has changed: " + "$field -> $value")
            field = value
        }
}

enum class State { ON, OFF }

val foo1 = run {
    println("Calculating the answer")
    1
}

class Rectangle(val height: Int, val width: Int) {
    val isSquare: Boolean
        get() {
            return height == width
        }
}

fun containsZero(list: List<Int>): Boolean {
    list.forEach { if (it == 0) return true }
    return false
}

fun duplicateNonZero2(list: List<Int>): List<Int> { // return from anonymous function
    return list.flatMap(fun (e): List<Int> {
        if (e == 0) return listOf()
        return listOf(e, e)
    })
}

fun duplicateNonZeroLocalFunction(list: List<Int>): List<Int> {
    fun duplicateNonZeroElement(e: Int): List<Int> {
        if (e == 0) return listOf()
        return listOf(e, e)
    }
    return list.flatMap(::duplicateNonZeroElement)
}

fun duplicateNonZero(list: List<Int>): List<Int> {
    return list.flatMap { if (it == 0) return@flatMap listOf<Int>()
    listOf(it, it)
    }
}

class Person(val name: String, val age: Int) {
    fun isOlder(ageLimit: Int) = age > ageLimit
    fun getAgePredicate() = this::isOlder // member reference, type of (Int) -> Boolean
}

data class Hero(
    val name: String,
    val age: Int,
    val gender: Gender?
)
enum class Gender { MALE, FEMALE }


data class Employee(
    val city: String, val age: Int
)

fun String?.isEmptyOrNull() = this == null || this.isEmpty() // fun isEmptyOrNull(s: String?) = s == null || s.isEmpty()

fun foo(list1: List<Int?>, list2: List<Int?>) {
    list1.size
    list2?.size
    val i: Int? = list1.get(0)
    val j: Int? = list2?.get(0)
}

class Optional<T>(private val value: T) { // Wrapper that stores the reference to the initial object
    fun isPresent() = value != null
    fun get() = value ?: throw NoSuchElementException("No value present")
}

fun isFoo2(n: String?) = n == "foo"

class A {
    fun foo() = "member"
}

fun A.foo(i: Int) = "extension($i)"

fun String.get(index: Int) = '*'

open class Parent
class Child: Parent()

fun Parent.foo() = "parent"
fun Child.foo() = "child"

enum class Color {
    BLUE, ORANGE, RED
}

/*
data class Pair<A, B>(val first: A, val second: B) {
    override fun toString(): String = "($first, $second)"
}
*/

infix fun <T> T.eq(other: T): String {
    if (this == other) return "Ok"
    else return "Error $this != $other"
}


// infix fun Int.until(to: Int) {}

infix fun <A, B> A.to(that: B) = Pair(this, that)

fun <T> Iterable<T>.joinToString(
    separator: CharSequence = ", ",
    prefix: CharSequence = "",
    postfix: CharSequence = ""
) {
}

fun <T> List<T>.getOrNull(index: Int) = if (index in 0 until size) this[index] else null

@Throws(IOException::class)
fun foo() {
    throw IOException()
}

fun String.lastChar() = get(length - 1) // this[this.length - 1]

fun String.repeat(n: Int): String {
    val sb = StringBuilder(n * length)
    for (i in 1..n) {
        sb.append(this)
    }
    return sb.toString()
}

fun isLetter(c: Char) = c in 'a'..'z' || c in 'A'..'Z'
fun isNotDigit(c: Char) = c !in '0'..'9'
fun recognizeChar(c: Char) = when(c) {
    in '0'..'9' -> "It's a digit"
    in 'a'..'z', in 'A'..'Z' -> "It's a letter"
    else -> "Cannot recognized"
}

fun getDescription(color: Color): String =
    when (color) {
        Color.BLUE -> "blue"
        Color.ORANGE -> "orange"
        Color.RED -> "red"
    }


fun displaySeparator(character: Char = '*', size: Int = 10) {
    repeat(size) {
        print(character)
    }
}

@JvmOverloads
fun sum(a: Int = 0, b: Int = 0, c: Int = 0) = a + b + c