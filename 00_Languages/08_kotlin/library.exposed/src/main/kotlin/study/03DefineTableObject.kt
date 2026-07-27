package org.example.study

import jdk.jfr.internal.event.EventConfiguration.timestamp
import org.jetbrains.exposed.v1.core.Schema
import org.jetbrains.exposed.v1.r2dbc.R2dbcDatabase
import org.jetbrains.exposed.v1.jdbc.Database

import org.jetbrains.exposed.v1.core.dao.id.IntIdTable
import org.jetbrains.exposed.v1.core.Table
import org.jetbrains.exposed.v1.core.Column
import org.jetbrains.exposed.v1.datetime.CurrentTimestamp
import org.jetbrains.exposed.v1.datetime.timestamp
import java.util.UUID

import kotlin.uuid.Uuid

// 1. Table
// Table 클래스는 데이터베이스 테이블을 정의하기 위한 핵심 추상화
// 컬럼 타입, 제약 조건, 그 밖의 테이블 관련 속성을 정의할 수 있는 메서드가 제공됨
// org.jetbrains.exposed.v1.core 하위에 존재

// 2. IdTable
// 기본 키가 `id`인 테이블을 편하게 정의하기 위한 `Table`의 하위 클래스
// 일반 `Table`에서는 직접 `id` 컬럼을 만들어야 하는 반면, IdTable은 이미 id 컬럼이 있고, 기본키로 id가 지정되어있다.
// (1)IdTable: 표준 id 기본 키 정의를 자동화
// (2)IntIdTable: 정수형 ID
// (3)LongIdTable: Long ID
// (4)UUIDTable: UUID ID

// 3. Table 정의
// (1) 생성방법
// object 키워드는 Kotlin에서 클래스를 정의하면서 동시에 인스턴스 하나를 생성하는 문법이다.
// object StarWarsFilmsTable : Table()
// 위 문장은 대략 아래같은 구조
class StarWarsFilmsTable : Table()
val starWarsFilmsTable = StarWarsFilmsTable()
// 다만 object는 인스턴스를 딱 하나만 만들 수 있고, 그래서 싱글턴 객체라고 부름

// (2) 컬럼


// (3) 테이블명 설정
// - 테이블명을 명시적으로 지정하지 않으면 클래스 이름이 테이블명이 되며, 클래스명 뒤에 table 이라는 단어가 있다면 그 단어는 빼고 테이블명이 정해진다.
// - 테이블명을 지정하려면 `Table` 생성자에 name 파라미터를 할당한다.
// (4) 테이블옵션
// - 기본키, 엔진, charset 등의 옵션은 선언하는 테이블 오브젝트 안에 primarykey 등의 속성을 override하여 설정한다.

object SampleTable : Table(name="sample") {
    val id = integer(name= "id").autoIncrement()
    val uuid = integer(name = "uuid").uniqueIndex()
    val name = varchar(name= "name", length= 100)
    val category = varchar(name= "category", length= 100)

    override val primaryKey = PrimaryKey(id)
    override val options = listOf(
        EngineOption(TableEngine.INNODB),
        CharsetOption("utf8mb4"),
    )
}

// 또한 PostgreSQL 처럼 스키마별로 테이블이 논리적으로 구분되는 경우, 테이블명에 스키마.테이블 명을 적어주면 된다.
object SampleTable2 : Table(name="homedb.sample2")  {
    // ...
}

// (5) Storage Parameters
// Storage와 관련된 설정을 수행할 수 있는 기능
// 이는 PostgreSQL, SQL Server 등에서 유용하게 사용됨
object LargeDataTable : Table("large_data") {
    val id = integer("id")
    val data = text("data")
    override val primaryKey = PrimaryKey(id)
    override val storageParameters = listOf(
        FillFactorParameter(70),
        AutovacuumEnabledParameter(false)
    )
}


// 4.제약조건

// (1) Nullable - Null 가능
// 클래스에 선언하는 데이터 속성에 nullable(?) 를 포함하고
// 정의되는 데이터 값에 대해 `.nullable()` 메서드를 붙이면 된다.
object SampleTable3 : Table("sample") {
    val nullableColumn : Column<String?> = varchar("nullable_column", length=200).nullable()
}

// (2) Default - 기본값
// a `.default(defaultValue: T)` : 고정된 값을 기본값으로 할당할 때
// b `.defaultExpression(defaultValue: Expression<T>)` : DB 사이드에서 SQL 표현식으로 컬럼의 기본값을 제공
// c `.clientDefault(defaultValue: () -> T)` : Insert 전에 Client인 코틀린 사이드에서 함수를 실행해 기본값을 생성
object Users : Table("users") {
    val id        = integer("id").autoIncrement()
    val status    = varchar("status", length=200).default("ACTIVE")
    val createdAt = timestamp("created_at").defaultExpression(CurrentTimestamp)
    val clientId  = uuid("client_id").clientDefault { Uuid.random() }
}

// (3) Index - 인덱싱
// `.index()` 메서드를 이용해서 인덱스 설정을 할 수 있다.
// a. customIndexName : String? = null :: 인덱스명을 지정할 수 있음
// b. unique : Boolean :: 유니크 여부 지정 가능
// c. columns : List<Column> :: 함께 인덱스로 묶을 컬럼 목록
// d. indexType : String? = null :: 커스텀 인덱스 타입으로 "BTREE" 또는 "HASH"로 지정할 수 있음
// 그 외에도 있고 공식 doc 참고
object Items: Table(name="items"){
    val id        = integer("id").autoIncrement()
    val itemName  = varchar("item_name", length=200).index()
    val prodYear  = integer("prod_year")
    val prodMonth = integer("prod_month")

    init {
        index(customIndexName = "prodtime",
              isUnique = false,
              columns= *arrayOf(prodYear, prodMonth),
              indexType = "HASH")
    }
}

// (4) Unique - 유일성 제약
// 해당 컬럼에서 하나의 값은 한 번만 나올 수 있도록 제약
// .uniqueIndex() : 유니크하면서 인덱스로 활용할 컬럼을 선언. 인덱스 설정이 됨.
// .unique() 메서드는 없음.
object Categories: Table("categories") {
    val id = integer("id").autoIncrement()
    val name = varchar("category_name", length=200).uniqueIndex()
}

// (5) Primary Key
// Not Null과 Unique 제약이 자동으로 붙는다.
// 여러 컬럼을 Primary Key로 묶을 수 있다.
object SaleHistoryTable : Table("sale_history") {
    val itemId = integer("item_id")
    val userId = integer("user_id")
    // ...
    override val primaryKey = PrimaryKey(firstColumn = itemId, userId)
}

// (6) Foreign Key
// 외래키 제약조건
// 나중에 찾아보자


// (7) Check


// 5. Creating Tables