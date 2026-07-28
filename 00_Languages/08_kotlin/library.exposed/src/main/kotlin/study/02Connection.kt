package org.example.study
import org.jetbrains.exposed.v1.jdbc.Database
import org.jetbrains.exposed.v1.r2dbc.R2dbcDatabase

// Configure Connection
// https://www.jetbrains.com/help/exposed/working-with-database.html

// 1. Database.connect() : JDBC-based access
// 2. R2dbcDatabase.connect() : non-blocking, R2DBC access

// 단 이 명령은 연결 설정만 구성될 뿐, 데이터베이스에 즉시 연결되지는 않음

// (1) 예시 : H2 DB
val h2dbJdbc  = Database.connect(url = "jdbc:h2:mem:test", driver = "org.h2.Driver")
val h2dbR2dbc = R2dbcDatabase.connect(url = "r2dbc:h2:mem:///test")
// jdbc : JDBC 연결임을 명시
// h2 : 해당 데이터베이스가 H2임을 명시. 다른 데이터베이스 사용시 맞는 이름을 넣어야 함.
// mem : 이 데이터베이스가 메모리에만 저장됨. 또한 실제 DB 사용시 알맞은 주소를 넣어야 함.
// test : 데이터베이스 이름


// (2) MariaDB
// dependency
// implementation("org.mariadb.jdbc:mariadb-java-client:3.5.6")
// implementation("org.mariadb:r2dbc-mariadb:1.3.0")
// connect
val mariadbJdbc = Database.connect(
    "jdbc:mariadb://localhost:3306/test",
    driver = "org.mariadb.jdbc.Driver",
    user = "root",
    password = "your_pwd"
)
val mariadbR2dbc = R2dbcDatabase.connect(
    "r2dbc:mariadb://localhost:3306/test",
    driver = "mariadb",
    user = "root",
    password = "your_pwd"
)

// (3) Oracle
//dependency
//implementation("com.oracle.database.jdbc:ojdbc8:23.26.0.0.0")
//implementation("com.oracle.database.r2dbc:oracle-r2dbc:1.3.0")
val oracledbJdbc = Database.connect(
    "jdbc:oracle:thin:@//localhost:1521/test",
    driver = "oracle.jdbc.OracleDriver",
    user = "user",
    password = "password"
)
val oracledbR2dbc = R2dbcDatabase.connect(
    "r2dbc:oracle://localhost:3306/test",
    driver = "oracle",
    user = "user",
    password = "password"
)

// (4) PostgreSQL
// dependency
// implementation("org.postgresql:postgresql:42.7.8")
// implementation("org.postgresql:r2dbc-postgresql:1.1.1.RELEASE")
val postgresqldbJdbc = Database.connect(
    "jdbc:postgresql://localhost:12346/test",
    driver = "org.postgresql.Driver",
    user = "user",
    password = "password"
)
val postgresqldbR2dbc = R2dbcDatabase.connect(
    url = "r2dbc:postgresql://db:5432/test",
    driver = "postgresql",
    user = "user",
    password = "password"
)