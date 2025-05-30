package taxipark

/*
 * Task #1. Find all the drivers who performed no trips.
 */
fun TaxiPark.findFakeDrivers(): Set<Driver> =
        allDrivers - trips.map { it.driver }
        // allDrivers.minus(trips.map { it.driver })
        // allDrivers.filter { d -> trips.none { it.driver == d } }.toSet()

/*
 * Task #2. Find all the clients who completed at least the given number of trips.
 */
fun TaxiPark.findFaithfulPassengers(minTrips: Int): Set<Passenger> =
        allPassengers.filter { p -> trips.count { t -> p in t.passengers } >= minTrips }.toSet()
        // trips.flatMap(Trip::passengers).groupBy { passenger -> passenger }.filterValues { (_, group) -> group.size >= minTrips }.keys
        // allPassengers.partition { p -> trips.sumBy { t -> if (p in t.passengers) 1 else 0 } >= minTrips }.first.toSet()

/*
 * Task #3. Find all the passengers, who were taken by a given driver more than once.
 */
fun TaxiPark.findFrequentPassengers(driver: Driver): Set<Passenger> =
        allPassengers.filter { p -> trips.count { t ->  t.driver == driver && p in t.passengers } > 1 }.toSet()

/*
 * Task #4. Find the passengers who had a discount for majority of their trips.
 */
fun TaxiPark.findSmartPassengers(): Set<Passenger> =
        allPassengers.filter { p -> trips.count { t -> t.discount != null && p in t.passengers } > trips.count { t -> t.discount == null && p in t.passengers } }.toSet()
        /*
        val pair = trips.partition { it.discount is Double }
        return allPassengers.filter { p -> pair.first.count { p in it.passengers } > pair.second.count { p in it.passengers } }.toSet()
        */

/*
 * Task #5. Find the most frequent trip duration among minute periods 0..9, 10..19, 20..29, and so on.
 * Return any period if many are the most frequent, return `null` if there're no trips.
 */
fun TaxiPark.findTheMostFrequentTripDurationPeriod(): IntRange? {
    if (trips.isEmpty()) return null
    return trips.groupBy {
        val start = it.duration / 10 * 10
        val end = start + 9
        start..end
    }.maxBy { (_, group) -> group.size }?.key
}

/*
 * Task #6.
 * Check whether 20% of the drivers contribute 80% of the income.
 */
fun TaxiPark.checkParetoPrinciple(): Boolean {
    if (trips.isEmpty()) return false

    val totalIncome = trips.sumByDouble { it.cost }
    val totalDrivers = allDrivers.size
    val top20Income = trips.asSequence().groupBy { it.driver }
        .map { (_, tripsByDriver) -> tripsByDriver.sumByDouble { it.cost } }
        .sortedByDescending { it }
        .take((totalDrivers * 0.2).toInt())
        .sumByDouble { it }

    return (top20Income / totalIncome) >= 0.8
}