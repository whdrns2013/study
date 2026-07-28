plugins {
    kotlin("jvm") version "2.4.0"
}

group = "org.example"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
}

dependencies {
    testImplementation(kotlin("test"))
    implementation("org.jetbrains.exposed:exposed-core:1.3.1")
    implementation("org.jetbrains.exposed:exposed-jdbc:1.3.1")
    implementation("org.jetbrains.exposed:exposed-r2dbc:1.3.1")
    implementation("org.jetbrains.exposed:exposed-dao:1.3.1")
    implementation("org.jetbrains.exposed:exposed-kotlin-datetime:1.3.1")
}

kotlin {
    jvmToolchain(21)
}

tasks.test {
    useJUnitPlatform()
}