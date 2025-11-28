# 📚 Practice Questions: SQL and SQLite with Python

---

## 💻 Python & SQLite Connection

1.  What Python instructions will obtain a `Connection` object for a SQLite database in a file named **`example.db`**?

- `conn = sqlite3.connect('example.db')` where conn is a variable for the `Connection` object

2.  How do you connect to a SQLite database in **autocommit mode**?

- use `isolation_level=None` to connect to a SQLite database in autocommit mode

3.  What **“filename”** do you specify to create an **in-memory database**?

- `:memory:` in `conn = sqlite3.connect(':memory:')`

4.  How can you copy one SQLite database to another database?

There are 2 options:
- If database is closed you can simply copy the file with `shutil.copy('database_name.db', 'backup.db')` or even manually in file explorer
- If database is actively accessed, you must use `Connection object’s backup()` method instead by creating a copy database file and then duplicating the contents of the original database to the copy 

```python
conn = sqlite3.connect('sweigartcats.db', isolation_level=None) # connect to the original database
backup_conn = sqlite3.connect('backup.db', isolation_level=None) # Create the backup database
conn.backup(backup_conn) # Copy the database contents to the backup database
```

---

## 🛠️ Table Creation and Structure (DDL)

5.  What Python instruction will create a new table named **`students`** with **`TEXT`** columns named **`first_name`**, **`last_name`**, and **`favorite_color`**?

`conn.execute('CREATE TABLE IF NOT EXISTS students (first_name TEXT NOT NULL, last_name TEXT, favourite_color TEXT) STRICT')`

6.  What’s the difference between the **`INTEGER`** and **`REAL`** data types in SQLite?

- INTEGER is a whole number just like integer type in Python
- REAL is a floating point number, just like float type in Python

7.  What does **strict mode** add to a table?

- It enforces that **all data has specified type** which needs to be provided in the `CREATE TABLE` statement when inserting data
- It is available from version 3.37.0+ SQLite
- It is disabled by default and needs to be enabled by adding `STRICT` to the `CREATE TABLE` statement

8.  How can you **delete a table** named **`cats`**?

`conn.execute('DROP TABLE cats')`

---

## 📊 Data Manipulation (CRUD)

9.  What does **CRUD** stand for?

**CRUD operations are the building blocks** of any database application, and the **CRUD operations** are **the only way to access a database**
`CRUD` is an **acronym** for the **four** basic operations that databases carry out: **creating data, reading data, updating data, and deleting data**
- 1) `INSERT`
- 2) `SELECT`
- 3) `UPDATE`
- 4) `DELETE`

10. What query **adds new records** to a table?

`conn.execute('INSERT INTO table_name VALUES (value1, value2, value3, ...)')`

11. What query **deletes records** from a table?

`conn.execute('DELETE FROM table_name WHERE condition')`


12. What happens if you **don’t specify the `WHERE` clause** in an **`UPDATE`** query?

It applies the change to **all rows** in the table updating all of them to the same value

---

## 🔍 Queries and Advanced Concepts

13. What does the **`*`** in the query **`'SELECT * FROM cats'`** mean?

- it's a **wildcard** for all the columns in the table cats

14. What does **ACID** stand for?

- Atomic - All or Nothing - if any part fails, the entire transaction is rolled back
- Consistent - State Integrity - the transaction must not violate any defined rules or constraints
- Isolated - Independent Execution - one transaction does not affect others
- Durable - Permanent Record - once committed it is permanent

15. What is an **index**? What code would create an index for a column named **`birthdate`** in a table named **`cats`**?

- It helps to speed up queries in databases with many thousands of records or more
- We name the index after the column to which it applies
- **Indexing is automatically done** when you insert data into a table, but you can also create indexes manually with the `CREATE INDEX` command
- To add indexes on the `birthdate` column in the `cats table`, run the following `CREATE INDEX` query: `conn.execute('CREATE INDEX idx_birthdate ON cats (birthdate)')`

16. What is a **foreign key**?

- It's a column that **references** the **primary key of another table**