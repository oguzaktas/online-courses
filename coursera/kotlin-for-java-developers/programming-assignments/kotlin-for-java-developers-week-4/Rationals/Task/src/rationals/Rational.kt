package rationals

import java.lang.IllegalArgumentException
import java.math.BigInteger

class Rational(val n: BigInteger, val d: BigInteger) : Comparable<Rational> {
    init {
        if (d == BigInteger.ZERO) {
            throw IllegalArgumentException("Denominator cannot be 0")
        }
    }

    operator fun plus(other: Rational): Rational {
        val numerator = n * other.d + other.n * d
        val denominator = d * other.d
        return numerator divBy denominator
    }

    operator fun minus(other: Rational): Rational {
        val numerator = n * other.d - other.n * d
        val denominator = d * other.d
        return numerator divBy denominator
    }

    operator fun times(other: Rational): Rational {
        val numerator = n * other.n
        val denominator = d * other.d
        return numerator divBy denominator
    }

    operator fun div(other: Rational): Rational {
        val numerator = n * other.d
        val denominator = d * other.n
        return numerator divBy denominator
    }

    operator fun unaryMinus(): Rational = Rational(-n, d)

    private fun normalize(): Rational {
        val gcd = n.gcd(d)
        return if (d < BigInteger.ZERO) {
            Rational(-n / gcd, - d / gcd)
        } else {
            Rational(n / gcd, d / gcd)
        }
    }
    /*
    private fun normalize(n: BigInteger, d: BigInteger): Rational {
        val g = n.gcd(d)
        val sign = d.signum().toBigInteger()
        return Rational(n / g * sign, d / g * sign)
    }
    */

    override fun compareTo(other: Rational): Int {
        val a = this.n * other.d divBy this.d * other.d
        val b = other.n * this.d divBy other.d * this.d
        return (a.n).compareTo(b.n)
    }

    override fun equals(other: Any?): Boolean {
        if (this === other) return true
        if (other !is Rational) return false
        val a = this.normalize()
        val b = other.normalize()
        return (a.n == b.n && a.d == b.d)
    }

    override fun hashCode(): Int {
        var result = n.hashCode()
        result = 31 * result + d.hashCode()
        return result
    }

    override fun toString(): String {
        return if (d == BigInteger.ONE || n % d == BigInteger.ZERO) {
                (n / d).toString()
        } else {
            val r = normalize()
            return "${r.n}/${r.d}"
        }
    }
}

infix fun BigInteger.divBy(other: BigInteger): Rational = Rational(this, other)
infix fun Int.divBy(other: Int): Rational = Rational(this.toBigInteger(), other.toBigInteger())
infix fun Long.divBy(other: Long): Rational = Rational(this.toBigInteger(), other.toBigInteger())

fun String.toRational(): Rational {
    val numbers = split("/")
    return when (numbers.size) {
        1 -> Rational(numbers[0].toBigInteger(), 1.toBigInteger())
        2 -> Rational(numbers[0].toBigInteger(), numbers[1].toBigInteger())
        else -> throw IllegalArgumentException()
    }
}

fun main() {
    val half = 1 divBy 2
    val third = 1 divBy 3

    val sum: Rational = half + third
    println(5 divBy 6 == sum)

    val difference: Rational = half - third
    println(1 divBy 6 == difference)

    val product: Rational = half * third
    println(1 divBy 6 == product)

    val quotient: Rational = half / third
    println(3 divBy 2 == quotient)

    val negation: Rational = -half
    println(-1 divBy 2 == negation)

    println((2 divBy 1).toString() == "2")
    println((-2 divBy 4).toString() == "-1/2")
    println("117/1098".toRational().toString() == "13/122")

    val twoThirds = 2 divBy 3
    println(half < twoThirds)

    println(half in third..twoThirds)

    println(2000000000L divBy 4000000000L == 1 divBy 2)

    println("912016490186296920119201192141970416029".toBigInteger() divBy
            "1824032980372593840238402384283940832058".toBigInteger() == 1 divBy 2)
}