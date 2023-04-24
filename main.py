# This is a sample Python script. You can delete everything in here if you feel like it.
# We provide a starting point for you to connect to Snowflake
import snowflake.connector

con = snowflake.connector.connect(
    user='rotest',
    password='XXXX',
    account='QI42254.eu-west-2.aws',
    role='rotest',
    database='rotest',
    session_parameters={
        'QUERY_TAG': 'data-recruitment',
    }
)


def main():
    print('Hello World!')
    query_create_schema = 'create or replace schema test;'
    con.cursor().execute(query_create_schema)


if __name__ == '__main__':
    main()
