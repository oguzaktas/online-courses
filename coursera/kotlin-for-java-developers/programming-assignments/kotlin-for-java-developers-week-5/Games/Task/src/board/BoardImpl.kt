package board

import board.Direction.*

fun createSquareBoard(width: Int): SquareBoard = SquareBoardImpl(width)
fun <T> createGameBoard(width: Int): GameBoard<T> = GameBoardImpl(width)

open class SquareBoardImpl(final override val width: Int) : SquareBoard {
    private val cells = (1..width).flatMap { i -> (1..width).map { j -> Cell(i, j) } }

    override fun getCellOrNull(i: Int, j: Int): Cell? =
        getAllCells().firstOrNull { it == Cell(i, j) }

    override fun getCell(i: Int, j: Int): Cell =
        getCellOrNull(i, j) ?: throw IllegalArgumentException("Cell not found for i:$i, j:$j")

    override fun getAllCells(): Collection<Cell> = cells

    override fun getRow(i: Int, jRange: IntProgression): List<Cell> =
        jRange.applyBounds(width).map { j -> getCell(i, j) }

    override fun getColumn(iRange: IntProgression, j: Int): List<Cell> =
        iRange.applyBounds(width).map { i -> getCell(i, j) }

    override fun Cell.getNeighbour(direction: Direction): Cell? = when (direction) {
        UP -> getCellOrNull(this.i - 1, j)
        LEFT -> getCellOrNull(this.i, j - 1)
        DOWN -> getCellOrNull(this.i + 1, j)
        RIGHT -> getCellOrNull(this.i, j + 1)
    }
}

private fun IntProgression.applyBounds(bound: Int): IntProgression = when {
    last > bound -> first..bound
    first > bound -> bound..last
    else -> this
}

class GameBoardImpl<T>(width: Int) : SquareBoardImpl(width), GameBoard<T> {

    private val board = getAllCells().map { it to null }.toMap<Cell, T?>().toMutableMap()

    override fun get(cell: Cell): T? = board[cell]

    override fun set(cell: Cell, value: T?) {
        board[cell] = value
    }

    override fun filter(predicate: (T?) -> Boolean): Collection<Cell> =
        board.filter { predicate(it.value) }.map { it.key }

    override fun find(predicate: (T?) -> Boolean): Cell? =
        board.entries.find { predicate(it.value) }?.key

    override fun any(predicate: (T?) -> Boolean): Boolean =
        board.entries.any { predicate(it.value) }

    override fun all(predicate: (T?) -> Boolean): Boolean =
        board.entries.all { predicate(it.value) }
}