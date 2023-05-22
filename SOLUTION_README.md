# NHS Expenditure - Giles Matthews

## How to Run

Install dependencies

```
pip install -r requirements.txt
```

create a `.env` file and populate with the following credentials:

```
SNOWFLAKE_USERNAME=
SNOWFLAKE_PASSWORD=
SNOWFLAKE_ROLE=
SNOWFLAKE_DATABASE=
```

## Issues Faced

**Datatypes**: I was blocked for some time due to a datatype issue. I believe this was due to inconsistent datatypes in the Expenditure field which were a mixture of float types and string types. To resolve I cast the field to strings.

**Python Connector**: I used the `write_pandas` from `snowflake.connector.pandas_tools` to copy the data into the Snowflake table however I initially lost time trying to implement the `df.to_sql` method powered by `sqlalchemy`.