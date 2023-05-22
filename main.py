# This is a sample Python script. You can delete everything in here if you feel like it.
# We provide a starting point for you to connect to Snowflake
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
from sqlalchemy import create_engine
import pandas as pd
import zipfile
import time

import os
from dotenv import load_dotenv

from queries import *

load_dotenv()

con = snowflake.connector.connect(
    user=os.getenv('SNOWFLAKE_USERNAME'),
    password=os.getenv('SNOWFLAKE_PASSWORD'),
    account='QI42254.eu-west-2.aws',
    role=os.getenv('SNOWFLAKE_ROLE'),
    database=os.getenv('SNOWFLAKE_DATABASE'),
    warehouse='compute_wh',
    session_parameters={
        'QUERY_TAG': 'data-recruitment',
    }
)

def main():

    zf = zipfile.ZipFile('expenditure_v2.zip') 
    df = pd.read_csv(zf.open('expenditure_v2.csv'))

    col_mappings = {col: col.replace(' ', '') for col in df.columns}
    df = df.rename(columns=col_mappings)

    df['Expenditure'] = (df['Expenditure'].astype(str))

    query_create_schema = 'create or replace schema NHS;'
    con.cursor().execute(query_create_schema)

    query_create_table = '''
    create or replace table 
        expenditure(
        "DepartmentFamily" string,
        "Entity" string,
        "Date" string,
        "ExpenseType" string,
        "ExpenseArea" string,
        "Supplier" string,
        "TransactionNumber" string,
        "Expenditure" string
        );'''

    con.cursor().execute(query_create_table)

    write_pandas(con, df, 'EXPENDITURE', 'GILESMATTHEWS', 'NHS')

    transaction_count(con)


if __name__ == '__main__':
    main()
