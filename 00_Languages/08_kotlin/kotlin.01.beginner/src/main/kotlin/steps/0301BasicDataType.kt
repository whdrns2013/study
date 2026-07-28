package org.example.steps

fun basicDataType() {

    // Integers
    val byte   : Byte = 1
    val shor   : Short = 2
    val int    : Int = 3
    val long   : Long = 4_000_000_000L

    // Unsigned Integers
    val ubyte  : UByte  = 0u
    val ushort : UShort = 10u
    val uint   : UInt   = 0u
    val ulong  : ULong  = 0u

    // Floating Porint numbers
    val float  : Float  = 19.9f
    val double : Double  = 19.99

    // Booleans
    val isTrue  : Boolean = true
    val isFalse : Boolean = false

    // Characters
    val char     : Char = 'a'
    val char_num : Char = 65.toChar()
    val char_16num : Char = '\u0000'

    // Strings
    val text : String = "Hello World!"

    // https://kotlinlang.org/docs/kotlin-tour-basic-types.html
}