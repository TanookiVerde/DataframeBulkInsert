# Dataframe Bulk Insert (MySQL)
Python class for bulk inserting into MySQL database, from `pandas.DataFrame` object (and returning inserted ids)

# Important
- In order to retrieve the inserted ids I use `LAST_INSERT_ID` and `ROW_COUNT` from the cursor.
- This works if your database guarantees sequential numbers for `AUTO_INCREMENT`.
- More details about that in this Stack Overflow [answer](https://stackoverflow.com/a/16592867).

# How to use

```python
import mysql.connector
import pandas as pd

# Create DB Connection
cnx = mysql.connector.connect(
    user='user', 
    password='password',
    host='localhost',
    port='8000',
    database='database'
)

# Create a DataFrame
df = pd.DataFrame()
df['descricao'] = ['D', 'E', 'F']

# Create a instance of DataFrameBulkInsert
bulkInsert = DataFrameBulkInsert(
    table_name="dim_acao", 
    dataframe=df,
    db_cursor=cnx.cursor()
)

# Execute the insertion and returns the inserted ids (same order as dataframe)
inserted_ids = bulkInsert.bulk_insert()
cnx.commit()

# You can store the ids
df['ids'] = inserted_ids
```
