# This is a sample Python script. You can delete everything in here if you feel like it.
# We provide a starting point for you to connect to Snowflake
import snowflake.connector

con = snowflake.connector.connect(
    user='XXXX',  # given on your instruction email
    password='XXXX',  # set by you after you log in to Snowflake for the first time
    account='LS54927.eu-west-2.aws',
    role='XXXX',  # this would've been created by us, it will be the same as your user but all lower case
    database='XXXX',  # you will see a database with your name when you log in
    warehouse='compute_wh',
    session_parameters={
        'QUERY_TAG': 'data-recruitment',
    }
)


def main():
    print('Hello World!')
    query_create_schema = 'create or replace schema test3;'
    con.cursor().execute(query_create_schema)


if __name__ == '__main__':
    main()
