# Dataframe Bulk Insert (MySQL)
Python class for bulk inserting into MySQL database, from `pandas.DataFrame` object (and returning inserted ids)

# Important
- In order to retrieve the inserted ids I use `LAST_INSERT_ID` and `ROW_COUNT` from the cursor.
- This works if your database guarantees sequential numbers for `AUTO_INCREMENT`.
- More details about that in this Stack Overflow [answer](https://stackoverflow.com/a/16592867).

# How to use

- Suppose a table called `tb_user` with columns:
    - `id (autoincrement)`
    - `name`
- The following code uses the data from a dataframe to bulk insert into the table:

```python
import mysql.connector
import pandas as pd

from df_bulk_insert import DataFrameBulkInsert

# 1. Create DB Connection
cnx = mysql.connector.connect(
    user='user', 
    password='password',
    host='localhost',
    port='8000',
    database='database'
)

# 2. Create a DataFrame. Column names *must* match the ones in database.
df = pd.DataFrame()
df['name'] = ['John', 'Pedro', 'Hugh Mungus']

# 3. Create a instance of DataFrameBulkInsert
bulkInsert = DataFrameBulkInsert(
    table_name="tb_user", 
    dataframe=df,
    db_cursor=cnx.cursor()
)

# 4. Execute the insertion and returns the inserted ids (same order as dataframe)
inserted_ids = bulkInsert.bulk_insert()
cnx.commit()

# 5. You can store the ids in the dataframe
df['ids'] = inserted_ids
```
- All input dataframe columns will be used to create the query. Their names must match the column names from the specified table.
