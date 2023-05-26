# This is a sample Python script. You can delete everything in here if you feel like it.
# We provide a starting point for you to connect to Snowflake
import snowflake.connector
import pandas as pd
from snowflake.connector.pandas_tools import write_pandas


#create snowflake connection
con = snowflake.connector.connect(
    user='ALSEN',  # given on your instruction email
    password='n8PpSkHkH6jsHj',  # set by you after you log in to Snowflake for the first time
    account='LS54927.eu-west-2.aws',
    role='alsen',  # this would've been created by us, it will be the same as your user but all lower case
    database='ALSEN',  # you will see a database with your name when you log in
    warehouse='compute_wh',
    session_parameters={
        'QUERY_TAG': 'data-recruitment',
    }
)


def main():
    query_create_schema = 'create or replace schema test3;'
    con.cursor().execute('USE DATABASE ALSEN')
    con.cursor().execute(query_create_schema)

    query_create_table='''
    CREATE OR REPLACE TABLE
    expenditure (Department_Family string,Entity string, Date date, Expense_Type string, Expense_Area string, Supplier string, Transaction_Number string,Expenditure float)
    
    '''

    con.cursor().execute(query_create_table)
    # Tried using Copy into method to send files to snowflake
    #upload_sql_data = "COPY INTO expenditure FROM './expenditure_v2/expenditure_v2.csv';"
    #con.cursor().execute(upload_sql_data)

data = pd.read_csv(r'./expenditure_v2/expenditure_v2.csv', low_memory=False)
df = pd.DataFrame(data, columns=['DEPARTMENT_FAMILY','ENTITY', 'DATE', 'EXPENSE_TYPE', 'EXPENSE_AREA', 'SUPPLIER', 'TRANSACTION_NUMBER','EXPENDITURE'])


success, num_chunks, num_rows, output = write_pandas(
            conn=con,
            df=df,
            table_name='EXPENDITURE',
            database='ALSEN',
            schema='TEST3'
        )


if __name__ == '__main__':
    main()
