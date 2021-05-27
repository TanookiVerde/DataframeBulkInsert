import pandas as pd
import mysql.connector

class DataFrameBulkInsert:
    
    def __init__(self, table_name, dataframe, db_cursor):
        self.table_name = table_name
        self.dataframe = dataframe
        self.db_cursor = db_cursor
    
    def bulk_insert(self):
        query = self.build_query()
        self.db_cursor.execute(query)
        
        first_row = self.db_cursor.lastrowid
        row_count = self.db_cursor.rowcount
        return list(range(first_row, first_row+row_count))
        
    def build_template(self,column_count, quote_on_string = False):
        value_gap = "{!r}" if quote_on_string else "{}"
        return "(" + value_gap + ((", " + value_gap) * (column_count-1)) + ")"

    def build_query(self):
        column_count = self.dataframe.shape[1]
        
        query = "insert into " + self.table_name
        query += self.build_template(column_count).format(*self.dataframe.columns)
        query += " values "

        for i, row in self.dataframe.iterrows():
            if i > 0:
                query += ",\n"
            campos = tuple(row.values.tolist())
            query += self.build_template(column_count, True).format(*campos)

        return query
