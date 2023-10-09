var a: String = "initial"  // 1
val b: Int = 1             // 2
val c = 3                  // 3
println(a)

fun main() {
    print("hello world")
}

fun printProduct() {
    val x = 1
    val y : Int = 2
    val error = "Error!"

    // check values
    if (x == 1 && y == 2) {
        println(x * y)
    }
    else {
        println(error)
    }
}