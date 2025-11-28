# SQLite

- [Official SQLite Docs](https://sqlite.org/docs.html)
- [Docs for SQLite3 module](https://docs.python.org/3/library/sqlite3.html)
- [SQLite Language Expression Docs](https://www.sqlite.org/lang_expr.html)
- **SQLite** is the most widely deployed database software, as it runs on **every operating system** and is **small enough to embed within other applications**
- **SQL** is a mini language you can work with from within Python, much like regex for regular expressions.

## Spreadsheets vs. Databases

- Spreadsheets are for data entry and analysis, while databases are for data storage and management

- You can think of a **database table as a spreadsheet**, and a **database can contain one or more tables**. 
- Tables have **columns** of **different properties for each record**, also called a row or entry
- Databases like SQLite are called **relational databases**, where relation means that the **database can contain multiple tables with relationships between them**

- SQL database, tables often have an **ID column for each record’s primary key** - a **unique** identifier for each record called `rowid`
- `rowid` does not change if you delete or add a record to the table unlike in a spreadsheet
- Databases aren't visually pleasing, they just contain raw data. Spreadsheets give you the flexibility of putting any data into any cell, **databases have a  stricter structure to make data retrieval easier for software.**

## SQLite vs. Other SQL Databases

- It's a **full relational database that uses SQL** capable of reading and writing massive amounts of data (but not as powerful as a NoSQL database)
- **Runs within your Python program**, **NO installation or configuration required**.
- **Operates on a single file**, which you can move, copy or delete
	- There are **no network connections** involved.
- It's **lightweight** and **fast**, 
	- For faster performance, SQLite databases can exist entirely in memory and be saved to a file before the program exits.
	- Very **low resource usage**, can be run on a very old computer
- **better alternative to JSON or spreadsheet files** if your program needs the ability to store and quickly retrieve large amounts of data
- **Doesn’t** strictly **enforce a column’s data type**
- **No permission settings or user roles** in SQLite. There are **no** `GRANT` or `REVOKE` **statements** like in other SQL databases.
- **Public domain software** - can be used commercially without restrictions

## Creating SQL Databases and Tables

- **SQL is a mini language** you can work with from within Python, much like regex for regular expressions
- **SQL queries** are written as Python **string values**

### Example database

- We will name it `example.db`
	- extension for SQLite databases is `.db` or `.sqlite`
- **SQL Database** can contain **multiple tables**, and 
	- each **table** should store **one type of data**
	- **1st table** could contain records of **cats**, while **2nd table** could contain **records of vaccinations** given to **cats in the first table**
		- It would look like this: `[('Zophie', '2021-01-24', 'black', 5.6), ('Colin', '2016-12-24', 'siamese', 6.2), ...]` and so on.
	- You can think of a **table** as a **list of tuples, where each tuple is a table row**.

#### Example: 

1) Let’s **create a database**
	- Get a `Connection object` by calling `sqlite3.connect()` function
	- **first argument** to the function can be either a **string of a filename or a `pathlib.Path object`**
	- If the file doesn’t exist, it will be created
	- If file is **not sqlite3 database**, it will call an exception `sqlite3.DatabaseError: file is not a database exception`
		- You can catch it using `os.path.exists()` function
	- Second argument `isolation_level=None` tells SQLite to use autocommit mode (**no need to call `conn.commit()` after each `execute()`**).

2) **create a table** for the cat data
	- call the `execute()` method on the `Connection object`
	- use `CREATE TABLE` SQL query to create the table
	- use `CREATE` and `TABLE` to create the table
		- **SQL queries** are written using **uppercase letters** but **SQLite doesn’t enforce this** `create table if not exists cats (name text not null, birthdate text, fur text, weight_kg real) strict` runs just fine.
		- **Table and column names are also case-insensitive** the **convention is to make them lowercase and to separate multiple words with underscores**, as in weight_kg.
	- use `IF NOT EXISTS` to **prevent errors** if the table already exists `sqlite3.OperationalError: table cats already exists`
	- `NOT NULL` part of name `TEXT NOT NULL` specifies that the **Python None value cannot be stored in the name column**. This is a good way to make a **table column mandatory**

3) **insert** some cat **records** into it

4) **read** the **data** from the database

5) **close** the database **connection**
	- When your program is done with the database, call `conn.close()` to **close the connection**
	- Program will automatically close the connection when it terminates.


```python
import sqlite3
conn = sqlite3.connect('example.db', isolation_level=None)
conn.execute('CREATE TABLE IF NOT EXISTS cats (name TEXT NOT NULL, birthdate TEXT, fur TEXT, weight_kg REAL) STRICT') # Create the table
#<sqlite3.Cursor object at 0x0000013FB13ED9C0>
```

## SQL Data Types

| Data Type              | Description                                                                                          | Python Analogy |
| :--------------------- | :--------------------------------------------------------------------------------------------------- | :------------- |
| **NULL**               | Represents a missing or unknown value.                                                               | `None`         |
| **INT** or **INTEGER** | A signed integer, stored as 1, 2, 3, 4, 6, or 8 bytes.                                               | `int` type     |
| **REAL**               | A floating-point value.                                                                              | `float` type   |
| **TEXT**               | A text string, stored using the database encoding (UTF-8, UTF-16BE, or UTF-16LE).                    | `str` type     |
| **BLOB**               | Short for **Binary Large Object**. Used for storing raw binary data, such as images or entire files. | `bytes` type   |

- **SQLite is not strict about the data types of its columns.** This means SQLite will, by default, gladly store the string 'Hello' in an INTEGER column without raising an exception.
- SQLite **automatically casts the data type** of the column based on the first value inserted into the column. This is called **data type affinity**
- (version 3.37.0+) You can override this behavior using `STRICT` keyword. it enables **strict mode** for table, **demanding** that **all data has specified type**
	- You can check version using `sqlite3.sqlite_version`

- **BOOL is not supported** in SQLite, it uses **0** or **1** to represent **true** or **false**

- **datetime is not supported** in SQLite either, it uses **text** to represent **date and time**
- For maximum compatibility and readability, the following formats are **recommended** when storing dates and times as **TEXT**.in SQLite

| Format | Example | Description |
| :--- | :--- | :--- |
| `YYYY-MM-DD` | `2035-10-31` | Date only. |
| `YYYY-MM-DD HH:MM:SS` | `2035-10-31 16:30:00` | Date and time (to the second). |
| `YYYY-MM-DD HH:MM:SS.SSS` | `2035-10-31 16:30:00.407` | Date and time with milliseconds. |
| `HH:MM:SS` | `16:30:00` | Time only (to the second). |
| `HH:MM:SS.SSS` | `16:30:00.407` | Time only with milliseconds. |

## rowid

**SQLite tables automatically create a `rowid` column containing a unique primary key integer**. 
Even if your cats table has two cats that coincidentally have the **same name, birthday, fur color, and weight,** the `rowid `allows you to **distinguish** between them.

## Listing Tables and Columns

- `sqlite_schema` is a table that lists metadata about the database, including all of its tables
- table itself isn’t listed as a table. You will never need to modify the sqlite_schema table yourself, and doing so will **likely corrupt the database, making it unreadable.**

```python
conn.execute('SELECT name FROM sqlite_schema WHERE type="table"').fetchall() # SQL query for all tables in the database
#[('cats',)] 
conn.execute('PRAGMA TABLE_INFO(cats)').fetchall() # SQL query for all columns in the table
#[(0, 'name', 'TEXT', 1, None, 0), (1, 'birthdate', 'TEXT', 0, None, 0), (2, 'fur', 'TEXT', 0, None, 0), (3, 'weight_kg', 'REAL', 0, None, 0)]
```

The output of the SQLite command `PRAGMA table_info(table_name)` returns metadata about a table's columns. This information is typically presented with the following structure:

| Column Header                  | Value         | Description                                                                                                                 | Key Fact                                                  |
| :----------------------------- | :------------ | :-------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------- |
| **cid** (Column position)      | `1`           | Indicates the column's zero-based position in the table. The first column is at position **0**.                             | Column numbers are zero-based, like Python list indexes.  |
| **name**                       | `'birthdate'` | The name of the column.                                                                                                     | SQLite names are case-insensitive.                        |
| **type**                       | `'TEXT'`      | The defined SQLite storage class for the column.                                                                            | Use appropriate SQLite data types (`TEXT`, `INT`, etc.).  |
| **notnull**                    | `0`           | A value of **`0`** means **`False`** (can contain `NULL`). A value of **`1`** means **`True`** (cannot contain `NULL`).     | Corresponds to the `NOT NULL` constraint.                 |
| **dflt_value** (Default value) | `None`        | The default value inserted if no other value is specified for the column during an `INSERT`.                                | Can be a literal value or `NULL`.                         |
| **pk** (Primary Key)           | `0`           | A value of **`0`** means **`False`** (not a primary key). A value of **`1`** means **`True`** (is part of the primary key). | Identifies columns that enforce uniqueness and integrity. |


## CRUD Database Operations

- `CRUD` is an **acronym** for the **four** basic operations that databases carry out: **creating data, reading data, updating data, and deleting data**
	- 1) `INSERT`
	- 2) `SELECT`
	- 3) `UPDATE`
	- 4) `DELETE`
- **CRUD operations are the building blocks** of any database application, and the **CRUD operations** are **the only way to access a database**

- Here are examples of each statement, which we’ll later pass as strings to conn.execute():

```sql
INSERT INTO cats VALUES ("Zophie", "2021-01-24", "black", 5.6)
SELECT rowid, * FROM cats ORDER BY fur
UPDATE cats SET fur = "gray tabby" WHERE rowid = 1
DELETE FROM cats WHERE rowid = 1
```

### INSERT

- The parentheses are **mandatory** for `INSERT` queries
- The sqlite3 module uses either single or double quotes for its TEXT values.
- `INSERT` statement begins a **transaction** , also triggered by `UPDATE`, or `DELETE`. 
	- To ensure data integrity, every transaction must adhere to the **ACID** properties:

| Property       | Definition            | Description                                                                                                                                                                                          |
| :------------- | :-------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Atomic**     | All or Nothing        | The transaction is treated as a single, complete operation. It is carried out **either completely or not at all**. If any part fails, the entire transaction is rolled back.                         |
| **Consistent** | State Integrity       | The transaction must not violate any defined rules or constraints (e.g., **`NOT NULL`**, foreign keys). It guarantees that the database moves from one valid state to another valid state.           |
| **Isolated**   | Independent Execution | The concurrent execution of multiple transactions results in a system state that is equivalent to one where the transactions were executed sequentially. **One transaction does not affect others.** |
| **Durable**    | Permanent Record      | Once a transaction has been **committed**, its results are permanently written to persistent storage (like the hard drive) and will survive subsequent system failures (e.g., power loss).           |

- A SQLite query will **either completely insert data into the database or not insert it at all**

```python
import sqlite3
conn = sqlite3.connect('example.db', isolation_level=None)

conn.execute('CREATE TABLE IF NOT EXISTS cats (name TEXT NOT NULL, birthdate TEXT, fur TEXT, weight_kg REAL) STRICT') # Create the table
conn.execute('INSERT INTO cats VALUES ("Zophie", "2021-01-24", "black", 5.6)') # Insert data into the table
# <sqlite3.Cursor object at 0x0000013FB13EDA40>
```

#### SQL Injection Attacks

- **Not really a problem with SQLite** since it doesn't require internet connection
- But it's still a **good practice** to avoid SQL injection attacks by using `?` question mark syntax whenever you **reference variables when inserting or updating data in your database**

**BAD EXAMPLE**
If you want to **insert a new cat record** based on data stored in variables, **do not insert these variables directly into the query string using Python**, like this:

```python
cat_name = "Zophie"
cat_birthdate = "2021-01-24"
cat_fur = "black"
cat_weight = 5.6
conn.execute(f"INSERT INTO cats VALUES ('{cat_name}', '{cat_birthdate}', '{cat_fur}', {cat_weight})")
```
- The hacker could potentially specify strings that changed the meaning of the query.

**GOOD EXAMPLE**
Instead, use the `?` question mark syntax:

```python
cat_name = "Zophie"
cat_birthdate = "2021-01-24"
cat_fur = "black"
cat_weight = 5.6
conn.execute('INSERT INTO cats VALUES (?, ?, ?, ?)', [cat_name, cat_bday,fur_color, cat_weight])
```

### SELECT

- Once there’s data inside the database, you can read it with a `SELECT` query
- You need to use `.fetchall()` to actually get the data, otherwise it will only return the **cursor object**
- **Each record is returned as a tuple in the list of tuples**. The data in each tuple appears **in the order** of the table’s **columns**.

```python
import sqlite3
conn = sqlite3.connect('example.db', isolation_level=None)
conn.execute('SELECT * FROM cats') # this will only return the cursor object, need to use .fetchall()
#<sqlite3.Cursor object at 0x0000013FB13EDA40>
conn.execute('SELECT * FROM cats').fetchall() # SQL query for all rows in the table
# [('Zophie', '2021-01-24', 'black', 5.6)]
```

- A basic `SELECT` query in SQL is used to retrieve data from a database. 
- This simple example query can be broken down into four essential components:

| Component | Example Value | Description | Key Fact |
| :--- | :--- | :--- | :--- |
| **The `SELECT` Keyword** | `SELECT` | The command that tells the SQLite engine you want to **retrieve** data. | **All SQL queries start with a main command.** |
| **Target Columns** | `*` (Asterisk) | Specifies **which columns** should be returned in the result set. | **`*` is a shorthand for "all columns except `rowid`."** |
| **The `FROM` Keyword** | `FROM` | A required separator that indicates the table source is coming next. | Follows the columns and precedes the table name. |
| **The Source Table** | `cats` | The **table** from which the data should be retrieved. | Data is extracted from this specific table. |

- **Example Query Structure:** `SELECT column_name(s) FROM table_name;`

```python
conn.execute('SELECT rowid, name FROM cats').fetchall() # get rowid and name columns of records in the cats table
# [(1, 'Zophie')]
```

#### Looping over Query Results

- You can loop over the results of a query with a `for` loop.
- No need to use `.fetchall()` because the cursor object is iterable
- The code can access the **columns** using the **tuple's integer index:** index 0 for the name, index 1 for the birthdate, and so on.

```python
import sqlite3
conn = sqlite3.connect('sweigartcats.db', isolation_level=None) # We will be working on excersise material database

for row in conn.execute('SELECT * FROM cats'): # Loop over all rows in the table
	print(f'Row data: {row}')	
	print(f'{row[0]} is one of my favourite cats') # Access the columns by index
#Row data: ('Zophie', '2021-01-24', 'black', 5.6)
#Zophie is one of my favourite cats
#Row data: ('Miguel', '2016-12-24', 'siamese', 6.2)
#Miguel is one of my favourite cats
#(...)
```

### Filtering Retrieved Data

- [SQLite Language Expression Docs](https://www.sqlite.org/lang_expr.html)

#### WHERE

- SQLite uses a set of operators for use in the `WHERE` clause

The `WHERE` clause in SQLite uses a set of operators to filter records based on specific conditions. These operators are similar in function to those found in Python, though the syntax for equality differs.

| SQLite Operator | Function | Python Analog | Example Usage |
| :--- | :--- | :--- | :--- |
| **`=`** | Tests for **equality**. | `==` | `age = 25` |
| **`!=`** | Tests for **inequality** (is not equal to). | `!=` | `status != 'Pending'` |
| **`<`** | Less than. | `<` | `price < 10.00` |
| **`>`** | Greater than. | `>` | `score > 90` |
| **`<=`** | Less than or equal to. | `<=` | `units <= 5` |
| **`>=`** | Greater than or equal to. | `>=` | `level >= 10` |
| **`AND`** | **Logical AND**. Requires both conditions on either side to be true. | `and` | `(age > 18 AND country = 'USA')` |
| **`OR`** | **Logical OR**. Requires at least one of the conditions to be true. | `or` | `(city = 'NY' OR city = 'LA')` |
| **`NOT`** | **Logical NOT**. Negates the following condition. | `not` | `NOT (paid = 1)` |

- **Note:** In a `WHERE` clause, the values on either side of the operator can be a **column name** or a **literal value** (e.g., `'Text'`, `10`, `NULL`).
- **Example Query Structure:** `SELECT column_name(s) FROM table_name WHERE column_name = value;`

```python
import sqlite3
conn = sqlite3.connect('sweigartcats.db', isolation_level=None) # We will be working on excersise material database
conn.execute('SELECT * FROM cats WHERE fur = "black"').fetchall() # Filter out all cats with black fur ONLY
#[('Zophie', '2021-01-24', 'black', 5.6), ('Toby', '2021-05-17', 'black', 6.8), ('Thor', '2013-05-14', 'black', 5.2), ('Sassy', '2017-08-20', 'black', 7.5), ('Hope', '2016-05-22', 'black', 7.6)]

import pprint # for pretty printing
matching_cats = conn.execute('SELECT * FROM cats WHERE fur = "black"').fetchall()
pprint.pprint(matching_cats)
#[('Zophie', '2021-01-24', 'black', 5.6),
# ('Toby', '2021-05-17', 'black', 6.8),
# ('Thor', '2013-05-14', 'black', 5.2),
# ('Sassy', '2017-08-20', 'black', 7.5),
# ('Hope', '2016-05-22', 'black', 7.6)]

matching_cats_date = conn.execute('SELECT * FROM cats WHERE fur = "black" OR birthdate >= "2024-01-01"').fetchall() # Filter out all cats with black fur OR older than 2024-01-01
pprint.pprint(matching_cats_date)
# [('Zophie', '2021-01-24', 'black', 5.6),
# ('Toby', '2021-05-17', 'black', 6.8),
# ('Taffy', '2024-12-09', 'white', 7.0),
# ('Hollie', '2024-08-07', 'calico', 6.0),
# ('Lewis', '2024-03-19', 'orange tabby', 5.1),
# ('Thor', '2013-05-14', 'black', 5.2),
# ('Shell', '2024-06-16', 'tortoiseshell', 6.5),
# ('Jasmine', '2024-09-05', 'orange tabby', 6.3),
# ('Sassy', '2017-08-20', 'black', 7.5),
# ('Hope', '2016-05-22', 'black', 7.6)]
```

#### LIKE

- `LIKE` operator lets you **match just the start or end of a value**, using sign `%` as a **wildcard**.
- **Examples:**
	- `name LIKE "%y"` matches all the names that **end with 'y'**
	- `name LIKE "Ja%"` matches all the names that **start with 'Ja'**
	- `name LIKE "%ob%"` matches all names that have **'ob' anywhere in them**
- Matches are case **insensitive**
	- `name LIKE "%ob%"` also matches `'%OB%'`, `'%Ob%'`, and `'%oB%'`
	- To make it **case-sensitive use GLOB operator **[[Glob Patterns]] and `*` as a wildcard


```python
import sqlite3
conn = sqlite3.connect('sweigartcats.db', isolation_level=None)

ycats = conn.execute('SELECT rowid, name FROM cats WHERE name LIKE "%y"').fetchall() # Filter out all cats with names that end with 'y'
print(f"Cats with names that end with 'y': {ycats}")
# Cats with names that end with 'y': [(7, 'Trey'), (11, 'Toby'), (17, 'Molly'), (18, 'Dusty'), (23, 'Mandy'), (24, 'Taffy'), (31, 'Rocky'), (33, 'Bobby'), (36, 'Misty'), (40, 'Mitsy'), (44, 'Colby'), (46, 'Riley'), (52, 'Ruby'), (71, 'Daisy'), (73, 'Crosby'), (78, 'Harry'), (83, 'Sassy'), (91, 'Lily'), (99, 'Spunky')]

jacats = conn.execute('SELECT rowid, name FROM cats WHERE name LIKE "Ja%"').fetchall() # Filter out all cats with names that start with 'Ja'
print(f"Cats with names that start with 'Ja': {jacats}")
# Cats with names that start with 'Ja': [(3, 'Jacob'), (55, 'Java'), (81, 'Jasmine'), (86, 'Jamison')]

obcats = conn.execute('SELECT rowid, name FROM cats WHERE name LIKE "%ob%"').fetchall() # Filter out all cats with names that have 'ob' anywhere in them
print(f"Cats with names that have 'ob' anywhere in them: {obcats}")
# Cats with names that have 'ob' anywhere in them: [(3, 'Jacob'), (11, 'Toby'), (33, 'Bobby')]

case_sensitive_mcats = conn.execute('SELECT rowid, name FROM cats WHERE name GLOB "*m*"').fetchall() # Filter out all cats with names that have 'm' anywhere in them but make sure it's case-sensitive for only 'm' lowercase
print(f"Cats with names that have lowercase 'm' anywhere in them: {case_sensitive_mcats}")
# Cats with names that have lowercase 'm' anywhere in them: [(4, 'Gumdrop'), (15, 'Thomas'), (50, 'Sam'), (69, 'Cinnamon'), (81, 'Jasmine'), (85, 'Samantha'), (86, 'Jamison')]
```

#### ORDER BY

- The `ORDER BY` clause lets you **sort the results** of a query.
- It needs to come after the `WHERE` clause.
- You can use multiple `ORDER BY` clauses to sort by multiple columns.
- **Example:**
	- if you want to sort the rows by fur color use:
		`cur = conn.execute('SELECT * FROM cats ORDER BY fur')`

	- if you want to first sort the rows by fur color and then sort the rows within each fur color by birthdate use:
		`cur = conn.execute('SELECT * FROM cats ORDER BY fur, birthdate')`
- **By default**, these sorts are in **ascending order**: the smallest values come first, followed by larger values. 
- **To sort in descending order, add the `DESC` keyword after the column name**. You can also use the `ASC` keyword to specify ascending order if you want your query to be explicit and readable


```python
import sqlite3, pprint
conn = sqlite3.connect('sweigartcats.db', isolation_level=None)

print(f"Sorted by fur color:")
pprint.pprint(conn.execute('SELECT * FROM cats ORDER BY fur').fetchall()) # Sorts the results by fur color

print(f"Sorted by fur color and then by birthdate:")
pprint.pprint(conn.execute('SELECT * FROM cats ORDER BY fur, birthdate').fetchall()) # Sorts the results by fur color and then by birthdate

print(f"Sorted by fur color ascending order and then by birthdate in descending order:")
cur = conn.execute('SELECT * FROM cats ORDER BY fur ASC, birthdate DESC') # Sorts the results by fur color ascending and then by birthdate descending
pprint.pprint(cur.fetchall())
```

### SELECT

- You can **limit the number of the returned `SELECT` results** with the `LIMIT` keyword.
	- **Theoretically** you could slice a list of results with `[:3]` to see only the first 3 rows but it's **inefficient** because it has to iterate over the entire list to get the first 3 rows and discards the rest.
- `LIMIT` clause **must come after** the `WHERE` and `ORDER BY`clauses
- **Example:**
	- if you want to limit the number of the returned `SELECT` results to 3 use:
		`cur = conn.execute('SELECT * FROM cats LIMIT 3')`


```python
import sqlite3
conn = sqlite3.connect('sweigartcats.db', isolation_level=None)
cat3 = conn.execute('SELECT * FROM cats LIMIT 3').fetchall() # Returns the first 3 cats
print(f"First 3 cats: {cat3}")
# First 3 cats: [('Zophie', '2021-01-24', 'black', 5.6), ('Miguel', '2016-12-24', 'siamese', 6.2), ('Jacob', '2022-02-20', 'orange and white', 5.5)]
cat4 = conn.execute('SELECT * FROM cats WHERE fur="orange" ORDER BY birthdate LIMIT 4').fetchall() # Returns the first 4 cats with fur color 'orange'
print(f"First 4 cats with fur color 'orange' and sorted by birthdate: {cat4}")
# First 4 cats with fur color 'orange' and sorted by birthdate: [('Mittens', '2013-07-03', 'orange', 7.4), ('Piers', '2014-07-08', 'orange', 5.2), ('Misty', 2016-07-08', 'orange', 5.2), ('Blaze', '2023-01-16', 'orange', 7.4)]
```

### Indexes

- For **small databases** with only a **few thousand records**, you can safely **ignore indexes**, as the benefits they provide are negligible
- `SQL index` is a **data structure** that organizes a column’s data so that it can be efficiently searched.
- Queries with `WHERE` clauses that use these columns will perform better
- An **index takes up a little bit more storage**, so **queries** that insert or update data will be **slightly slower**, because SQLite must also update the data’s index
- **Indexing is automatically done** when you insert data into a table, but you can also create indexes manually with the `CREATE INDEX` command
- **Example:**
	- To create indexes on, the `names` and `birthdate` columns in the `cats table`, run the following `CREATE INDEX` queries
		- `conn.execute('CREATE INDEX idx_name ON cats (name)')`
		- `conn.execute('CREATE INDEX idx_birthdate ON cats (birthdate)')`
- **Indexes require names**, and by convention, **we name them after the column** to which they apply
- To **see all the indexes that exist for a table**, check the built-in `sqlite_schema` table with a `SELECT` query
	- `conn.execute('SELECT * FROM sqlite_schema WHERE type="index"')`
- You can **delete indexes** with the `DROP INDEX` query
	`conn.execute('DROP INDEX idx_name')`

### UPDATE

- you can change a row with an `UPDATE` statement
- **Remember to include the `WHERE` clause to specify which rows to update**, otherwise all rows will be updated with the new values!!!

| Part | Keyword/Clause | Description | Key Action |
| :--- | :--- | :--- | :--- |
| **1. Command** | `UPDATE` | The primary keyword that signals the database engine to begin a modification operation. | **Initiates the row modification process.** |
| **2. Target** | `table_name` | The **name of the table** that contains the rows you intend to change. | Identifies where the changes will occur. |
| **3. Modification** | `SET` clause | Specifies **which column(s)** to change and the **new value** to assign to them (e.g., `SET column1 = 'new_value'`). | Defines the specific data change. |
| **4. Filtering** | `WHERE` clause | **(Optional but recommended)** Specifies **which specific rows** in the table will be updated. If omitted, **ALL** rows in the table are updated. | Controls the scope of the update. |

- **Example Query Structure:** `UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;`

```python
conn.execute('SELECT * FROM cats WHERE rowid = 1').fetchall() # Returns the first cat
#[('Zophie', '2021-01-24', 'black', 5.6)]
conn.execute('UPDATE cats SET fur = "gray tabby" WHERE rowid = 1') # Changes the fur color of the first cat to gray tabby
conn.execute('SELECT * FROM cats WHERE rowid = 1').fetchall() # Returns the first cat again with the new fur color
#[('Zophie', '2021-01-24', 'gray tabby', 5.6)]
```

- You can `UPDATE` **multiple columns at a time by separating them with commas**. 
	- For example, `'UPDATE cats SET fur = "black", weight_kg = 6 WHERE rowid = 1'` updates the value in the **fur and weight** columns to "black" and 6, respectively.

```python
conn.execute('UPDATE cats SET fur = "black", weight_kg = 6 WHERE rowid = 1') # Changes the fur color of the first cat to black and the weight to 6
# [('Zophie', '2021-01-24', 'black', 6)]
```
- In** most update queries**, the `WHERE` clause uses the **primary key from the `rowid` column** to specify an individual record to update instead of for example `WHERE name = "Zophie"` which may update **all the rows with the same name** "zophie"
- IF you do want to populate all the rows with new data, use `WHERE 1` as the condition in the `WHERE` clause, which **always evaluates to true** and avoids bugs

### DELETE

- you can delete a row with a `DELETE` statement
- **Remember to include the `WHERE` clause to specify which rows to delete**, otherwise all rows will be deleted!!!
-  If you intend to **delete every row**, use `WHERE 1` so that you can identify any `DELETE `statement without a `WHERE `clause as a bug.

| Component | Keywords | Purpose |
| :--- | :--- | :--- |
| **Command** | `DELETE FROM` | Specifies the action to remove rows and indicates which table to act upon. |
| **Target** | *Table Name* | The name of the table containing the rows to delete. |
| **Filter** | `WHERE` clause | **Crucial for safety.** Specifies the exact rows that should be deleted. If omitted, all rows in the table are deleted. |

- **Example Query Structure:** `DELETE FROM table_name WHERE condition;`

- **To delete a row by its primary key, use `DELETE FROM table_name WHERE rowid = <primary key>`**

```python
import sqlite3
conn = sqlite3.connect('sweigartcats.db', isolation_level=None)
conn.execute('SELECT rowid, * FROM cats WHERE rowid = 1').fetchall() # Returns the first cat
# [(1, 'Zophie', '2021-01-24', 'gray tabby', 5.6)]
conn.execute('DELETE FROM cats WHERE rowid = 1') # Deletes the first cat
conn.execute('SELECT * FROM cats WHERE rowid = 1').fetchall() # Returns the first cat again
# []
```

## ROLLBACK

- you can use `conn.rollback()` to undo changes made to the database before you `conn.commit()` them

**Example:**

```python
import sqlite3
conn = sqlite3.connect('sweigartcats.db', isolation_level=None)

conn.execute('BEGIN') # Starts a transaction
conn.execute('INSERT INTO cats VALUES ("Socks", "2022-04-04", "white", 4.2)') # Adds a new cat record
conn.execute('INSERT INTO cats VALUES ("Fluffy", "2022-10-30", "gray", 4.5)') # Adds another cat record
conn.rollback()  # This undoes the INSERT statements.
conn.execute('SELECT * FROM cats WHERE name = "Socks"').fetchall()
# []
conn.execute('SELECT * FROM cats WHERE name = "Fluffy"').fetchall()
# []
# The new cats, Socks and Fluffy, were not inserted into the database because the transaction was rolled back.
```

## COMMIT

- if you want to **apply all of the queries you’ve run**, call `conn.commit()` to commit the changes to the database:

```python
import sqlite3
conn = sqlite3.connect('sweigartcats.db', isolation_level=None)

conn.execute('INSERT INTO cats VALUES ("Socks", "2022-04-04", "white", 4.2)') # Adds a new cat record
conn.execute('INSERT INTO cats VALUES ("Fluffy", "2022-10-30", "gray", 4.5)') # Adds another cat record
conn.commit() # Commits the changes to the database

conn.execute('SELECT * FROM cats WHERE name = "Socks"').fetchall()
# [('Socks', '2022-04-04', 'white', 4.2)]
conn.execute('SELECT * FROM cats WHERE name = "Fluffy"').fetchall()
# [('Fluffy', '2022-10-30', 'gray', 4.5)]
# The new cats, Socks and Fluffy, were inserted into the database successfully.
```

## Backup Databases

- If a program isn’t currently accessing the SQLite database, you can back it up by simply copying the database file to another location
	- for example use `shutil.copy('sweigartcats.db', 'backup.db')`
- If program is actively accessing the database, you must use `Connection object’s backup()` method instead
	- The `backup()` method safely backs up the contents of the database to the `backup.db` file in between the other queries being run on it.

```python
import sqlite3
conn = sqlite3.connect('sweigartcats.db', isolation_level=None)
backup_conn = sqlite3.connect('backup.db', isolation_level=None) # Create the backup database
conn.backup(backup_conn) # Copy the database to the backup database
```

## ALTER TABLE

Common `ALTER TABLE` Actions

| Action Type           | SQL Command Structure                                        | Purpose                                                             |                                             |
| :-------------------- | :----------------------------------------------------------- | :------------------------------------------------------------------ | ------------------------------------------- |
| **Adding a Column**   | `ALTER TABLE table_name ADD COLUMN column_name data_type;`   | Adds a new column with a specified name and data type to the table. |                                             |
| **Removing a Column** | `ALTER TABLE table_name DROP COLUMN column_name;`            | Deletes a column and all its data from the table structure.         |                                             |
| **Renaming a Column** | `ALTER TABLE table_name RENAME COLUMN old_name TO new_name;` | Changes the name of an existing column.                             |                                             |
| **Renaming a Table**  | `ALTER TABLE old_name RENAME TO new_name;`                   | Changes the name of the entire table.                               | The full, common syntax is `RENAME TO ...`. |
| **Deleting a Table**  | `DROP TABLE table_name;`                                     | Permanently removes an entire table and all its data.               |                                             |

```python
import sqlite3
conn = sqlite3.connect('sweigartcats.db', isolation_level=None)

# Renaming a Table
conn.execute('SELECT name FROM sqlite_schema WHERE type="table"').fetchall() # SQL query for all tables in the database
# [('cats',)]
conn.execute('ALTER TABLE cats RENAME TO felines') # Rename the cats table to felines
conn.execute('SELECT name FROM sqlite_schema WHERE type="table"').fetchall()
# [('felines',)]

# Renaming a Column 
conn.execute('PRAGMA TABLE_INFO(felines)').fetchall()[2]  # List the third column.
# (2, 'fur', 'TEXT', 0, None, 0)
conn.execute('ALTER TABLE felines RENAME COLUMN fur TO description') # Rename the fur column to description
conn.execute('PRAGMA TABLE_INFO(felines)').fetchall()[2]  # List the third column again.
# (2, 'description', 'TEXT', 0, None, 0)

# Adding a Column
conn.execute('ALTER TABLE felines ADD COLUMN is_loved INTEGER DEFAULT 1') # Add the is_loved column
print(conn.execute('SELECT * FROM felines LIMIT 3').fetchall())
# [('Zophie', '2021-01-24', 'gray tabby', 5.6, 1), ('Miguel', '2016-12-24', 'siamese', 6.2, 1), ('Jacob', '2022-02-20', 'orange and white', 5.5, 1)]

# Removing a Column
conn.execute('PRAGMA TABLE_INFO(felines)').fetchall()  # List all columns.
# [(0, 'name', 'TEXT', 1, None, 0), (1, 'birthdate', 'TEXT', 0, None, 0), (2, 'description', 'TEXT', 0, None, 0), (3, 'weight_kg', 'REAL', 0, None, 0), (4, 'is_loved', 'INTEGER', 0, '1', 0)
conn.execute('ALTER TABLE felines DROP COLUMN is_loved')  # Delete the column.
conn.execute('PRAGMA TABLE_INFO(felines)').fetchall()  # List all columns.
# [(0, 'name', 'TEXT', 1, None, 0), (1, 'birthdate', 'TEXT', 0, None, 0), (2, 'description', 'TEXT', 0, None, 0), (3, 'weight_kg', 'REAL', 0, None, 0)]

# Deleting a Table
conn.execute('SELECT name FROM sqlite_schema WHERE type="table"').fetchall() # SQL query for all tables in the database
# [('felines',)]
conn.execute('DROP TABLE felines') # Delete the felines table
conn.execute('SELECT name FROM sqlite_schema WHERE type="table"').fetchall() # SQL query for all tables in the database
# []
```

- Try to limit how often you change your tables and columns, as you’ll also have to update the queries in your program to match.

## Foreign Keys & INNER JOIN

- A `foreign key` is a column in a table that **references** the `primary key` of **another table.**
- The `primary key` is a **unique value** that is used to **identify each row in a table**.
- `INNER JOIN`s use the **primary key of one table to match the foreign key of another table**

**Example**

```python
import sqlite3
conn = sqlite3.connect('sweigartcats.db', isolation_level=None)

# Lets add a new vaccination table and reference it with a foreign key
conn.execute('PRAGMA foreign_keys = ON') # Enable foreign key support
conn.execute('CREATE TABLE IF NOT EXISTS vaccinations (vaccine TEXT, date_administered TEXT, administered_by TEXT, cat_id INTEGER, FOREIGN KEY(cat_id) REFERENCES cats(rowid)) STRICT') # Create the new table and add a foreign key 

# Add some vaccinations to the vaccinations table
conn.execute('INSERT INTO vaccinations VALUES ("rabies", "2023-06-06", "Dr. Echo", 1)')
conn.execute('INSERT INTO vaccinations VALUES ("FeLV", "2023-06-06", "Dr. Echo", 1)')
conn.execute('SELECT * FROM vaccinations').fetchall() # SQL query for all vaccinations in the database in the vaccinations table
# [('rabies', '2023-06-06', 'Dr. Echo', 1), ('FeLV', '2023-06-06', 'Dr. Echo', 1)]

# Now lets find cat named Mango
conn.execute('SELECT rowid, * FROM cats WHERE name = "Mango"').fetchall() # SQL query for all cats in the database in the cats table with the name Mango
# [(23, 'Mango', '2017-02-12', 'tuxedo', 6.8)]
conn.execute('INSERT INTO vaccinations VALUES ("rabies", "2023-07-11", "Dr. Echo", 23)') # . The "cat_id" value references the primary key of the "cats" table. 
#The "STRICT" keyword ensures that the foreign key constraint is enforced and an error is raised if the referenced row does not exist.

# We can also perform a type of `SELECT` query called an inner join, which returns the linked rows from both tables
conn.execute('SELECT * FROM cats INNER JOIN vaccinations ON cats.rowid = vaccinations.cat_id').fetchall()
# [('Zophie', '2021-01-24', 'gray tabby', 5.6, 'rabies', '2023-06-06', 'Dr. Echo', 1), 
# ('Zophie', '2021-01-24', 'gray tabby', 5.6, 'FeLV', '2023-06-06', 'Dr. Echo', 1),
# ('Mango', '2017-02-12', 'tuxedo', 6.8, 'rabies', '2023-07-11', 'Dr. Echo', 23)]
```

Data safety features in SQLite for foreign keys in above db example:
- Need to be enabled manually: `conn.execute('PRAGMA foreign_keys = ON')`
- you **can’t insert or update** a vaccination **record** using a `cat_id` for a **nonexistent** cat. 
- SQLite also **forces** you to **delete all vaccination records for a cat before deleting the cat** to avoid “orphaned” vaccination records.

### In-Memory Databases and Backups

- **In-memory databases** are databases that are stored in RAM (random access memory) and don’t need to be saved to disk.
- They improve performance because there is no need to read and write to disk, RAM is faster than disk.
- **Backups** are copies of databases that are stored on disk to avoid loss of data if the database is corrupted or deleted in case of a power failure.

- **MAJOR DOWNSIDE** of in-memory databases: If your program **crashes from an unhandled exception, you’ll lose the database**
	- use `Try` statements to **avoid exceptions from crashing your program and losing all data**
	- if exception is handled, you can use `backup()` method to **save the database to disk**

**Example**:

```python
import sqlite3

memory_db_conn = sqlite3.connect(':memory:', isolation_level=None) # Create an in-memory database
memory_db_conn.execute('CREATE TABLE test (name TEXT, number REAL)') # Create a table in the in-memory database called test
memory_db_conn.execute('INSERT INTO test VALUES ("foo", 3.14)') # Insert data into the table

file_db_conn = sqlite3.connect('test.db', isolation_level=None) # Create a file-based database called test.db
memory_db_conn.backup(file_db_conn)  # Save the copy of the in-memory database to test.db.


#  load a SQLite database file into memory with the backup() method
file_db_conn = sqlite3.connect('sweigartcats.db', isolation_level=None)
memory_db_conn = sqlite3.connect(':memory:', isolation_level=None)
file_db_conn.backup(memory_db_conn) # Copy the database to the in-memory database
memory_db_conn.execute('SELECT * FROM cats LIMIT 3').fetchall() # Query the in-memory database
# [('Zophie', '2021-01-24', 'gray tabby', 5.6), ('Miguel', '2016-12-24', 'siamese', 6.2), ('Jacob', '2022-02-20', 'orange and white', 5.5)]
```

## Copying Databases

- Copy of the DB can be made by calling `iterdump()` method on the original `DB comnnection object`
	- This creates an `iterator` that you can use to copy the database - It's a **text file** that contains the **SQL commands** to **recreate the database**
	- You can use iterators in `for loop` or pass them to the `list()` function.

```python
import sqlite3
conn = sqlite3.connect('sweigartcats.db', isolation_level=None)

# create a text file called sweigartcats_queries.txt that contains the SQL commands to recreate the database
with open('sweigartcats_queries.txt', 'w', encoding='utf-8') as fileObj: # Open a text file for writing 
	for line in conn.iterdump(): # Copy the database queries line by line
		fileObj.write(f'{line}\n') # Write each line to the text file
```

Example of how it looks inside the text file:

```sql
BEGIN TRANSACTION;
CREATE TABLE "cats" (name TEXT NOT NULL, birthdate TEXT, fur TEXT, weight_kg REAL) STRICT;
INSERT INTO "cats" VALUES('Zophie','2021-01-24','gray tabby',5.6);
INSERT INTO "cats" VALUES('Miguel','2016-12-24','siamese',6.2);
INSERT INTO "cats" VALUES('Jacob','2022-02-20','orange and white',5.5);
--snip--
INSERT INTO "cats" VALUES('Spunky','2015-09-04','gray',5.9);
INSERT INTO "cats" VALUES('Shadow','2021-01-18','calico',6.0);
COMMIT;
```

- This file will be larger than the original database file, but it will still be a valid SQLite database file.
- It is human-readable and can be used to **recreate the database** or even edit it before recreating it or passing into Python code or SQLite App.

## SQLite Apps

- You can **edit SQLite databases** directly from **CLI** instead of using Python - [Docs here](https://sqlite.org/cli.html)
- You can also download a **SQLite App**, which is a GUI collection of tools for your OS - [Download here](https://sqlite.org/download.html)
	- for Windows place `sqlite3.exe` file in system `PATH`
	- Linux use `sudo apt install sqlite3`
	- macOS this is pre-installed as `sqlite3` command

In CLI run `sqlite3 database_name.db` to connect to that db
- If file doesn't exist, it will be created
- You have to add semicolons `;` at the end of each command to execute it

```sql
C:\Users\BOBeirne>sqlite3 example.db
SQLite version 3.xx.xx
Enter ".help" for usage hints.
sqlite> CREATE TABLE IF NOT EXISTS cats (name TEXT NOT NULL, birthdate TEXT, fur TEXT, weight_kg REAL) STRICT;
sqlite> INSERT INTO cats VALUES ('Zophie', '2021-01-24', 'gray tabby', 4.7);
sqlite> SELECT * from cats;
Zophie|2021-01-24|gray tabby|4.7
--- You can also use .tables (which shows the tables in the database) and .headers (which lets you turn column headers on or off): ---
sqlite> .tables
cats
sqlite> .headers on
sqlite> SELECT * from cats;
name|birthdate|fur|weight_kg
Zophie|2021-01-24|gray tabby|4.7
```

#### You can also use Open Souce apps:

- [DB Browser for SQLite](https://sqlitebrowser.org/)
- [SQLite Studio](https://sqlitebrowser.org/dl/)
- [DBeaver Community](https://dbeaver.com/)

This table compares those three popular database management tools linked above


| Feature | DB Browser for SQLite | SQLite Studio | DBeaver Community |
| :--- | :--- | :--- | :--- |
| **Core Focus** | Dedicated SQLite Tool | Dedicated SQLite Tool | **Universal Database Client** |
| **Supported DBs** | **SQLite only** | **SQLite only** (via extensions) | **All Major DBs** (MySQL, PostgreSQL, SQL Server, Oracle, etc.) |
| **Interface** | Clean, basic, and **intuitive** | Modern, feature-rich, tabbed | Professional, feature-packed, Java-based |
| **Key Features** | Basic SQL editor, data editing, import/export (CSV, SQL) | Advanced SQL editor, data manipulation, stored procedures support, **visual query builder** | **Advanced visual editors**, powerful schema management, **ER diagrams**, data transfer, **multiple simultaneous connections** |
| **Installation** | Standard install | **Portable version available** | Standard install |
| **Licensing** | Open Source (Public Domain) | Open Source (GPLv3) | Open Source (Apache License) |
| **Best For** | Quick edits, viewing data, **simple data manipulation**. Ideal for non-developers. | Developers and Sysadmins needing a powerful, **feature-rich SQLite-only environment.** | **Professionals managing diverse environments** and needing one tool for everything from SQLite to Enterprise DBs. |


