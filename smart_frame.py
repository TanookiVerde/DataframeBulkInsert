import pandas as pd

class SmartFrame:
  
    def __init__(self):
        self.df = pd.DataFrame()
    
    def select(self, columns):
        self.df = self.df[columns]
        return self
    
    def rename(self, column_name, new_name):
        self.df = self.df.rename(columns={column_name:new_name})
        return self
    
    def copy(self):
        new = SmartFrame()
        new.df = self.df
        return new
    
    def inner_join(self, frame, on):
        left, right = on
        self.df = pd.merge(self.df, frame.df, left_on = left, right_on = right)
        return self

# Example:

# Defining the SmartFrames: just like DataFrames
person = SmartFrame()
person.df['name'] = ['leonardo','john doe']
person.df['age'] = [12, 56]
person.df['country'] = ['brazil','russia']

country = SmartFrame()
country.df['name'] = ['brazil', 'russia']
country.df['language'] = ['portuguese', 'russian']

# Readable and small chained operations
result = person.copy() \
    .select(['name','country']) \
    .rename('name','first_name') \
    .inner_join(country, on=('country','name'))

# Maintain all Dataframe properties
result.df.to_csv()
