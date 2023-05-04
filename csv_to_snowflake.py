import snowflake.connector

# Connect to Snowflake
con = snowflake.connector.connect(
    account='{placeholder}',
    user='{placeholder}',
    password='{placeholder}',
    warehouse='COMPUTE_wh',
    database='{placeholder}',
    schema='JORDAN',
    role='{placeholder}'
)

# CREATE TABLE statement
create_sql = """
   CREATE OR REPLACE TABLE {placeholder}.JORDAN.expenditure (
        department_family VARCHAR(255),
        entity VARCHAR(255),
        date DATE,
        expense_type VARCHAR(255),
        expense_area VARCHAR(255),
        supplier VARCHAR(255),
        transaction_number INT,
        expenditure NUMERIC(18, 2)
    )
"""

# COPY INTO statement
copy_sql = """
    COPY INTO {placeholder}.JORDAN.expenditure
    FROM @expenditure_stage/expenditure_v2.csv
    FILE_FORMAT = (TYPE = CSV FIELD_DELIMITER = ',' SKIP_HEADER = 1)
    ON_ERROR = CONTINUE
"""

# Execute the CREATE STAGE statement
con.cursor().execute("CREATE OR REPLACE STAGE {placeholder}.JORDAN.expenditure_stage")

# Put the CSV file into the stage
con.cursor().execute("PUT file://C:/Users/jorda/OneDrive/Desktop/expenditure_v2.csv @expenditure_stage")

# Execute the CREATE TABLE statement
con.cursor().execute(create_sql)

# Execute the COPY INTO statement
con.cursor().execute(copy_sql)

# Close the connection
con.close()
