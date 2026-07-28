package org.example.steps

fun declareVariable() {
    // val : Read-only variables
    // var : Mutable variables

    val ten = 10
    var eleven = 11

    println(ten + eleven)

    eleven = 10
    println(ten + eleven)
}