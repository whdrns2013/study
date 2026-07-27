package org.example.study

// 1. 의존성 추가 (그래들)
// https://www.jetbrains.com/help/exposed/adding-dependencies.html#add-dependencies
// 추가한 뒤 그래들 새로고침 또는 빌드를 하면 설치됨
// e.g.
// dependencies {
//     testImplementation(kotlin("test"))
//     implementation("org.jetbrains.exposed:exposed-core:1.3.1")
//     implementation("org.jetbrains.exposed:exposed-jdbc:1.3.1")
//     implementation("org.jetbrains.exposed:exposed-r2dbc:1.3.1")
//     implementation("org.jetbrains.exposed:exposed-dao:1.3.1")
//     implementation("org.jetbrains.exposed:exposed-kotlin-datetime:1.3.1")
// }

// 2. 지원하는 데이터베이스 전송 계층
// (1) JDBC (Java Database Connectivity) - blocking, sync, traditional, well-established
// (2) R2DBC (ReactiveRelational Database Connectivity) - 비동기, 논블로킹
// JDBC는 단순하고 다양한 DB 수용이 가능하며, R2DBC는 상호작용이 많거나 코루틴을 이용하는 경우 유용함

// 3. 설치 후 import
// import org.jetbrains.exposed.v1.jdbc.Database
// import org.jetbrains.exposed.v1.r2dbc.R2dbcDatabase