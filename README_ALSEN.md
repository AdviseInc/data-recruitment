#AdviseInc Technical Task

## About
I established a database connection using the credentials provided by AdviseInc.
I selected to use the database that was previously created for my name.
Using the query provided in the code I created the schema named test3, also created the table 'expenditure'. 


Created a dataframe to load the data into snowflake database but I got some errors:
'pandas.errors.DatabaseError: Execution failed on sql 'SELECT name FROM sqlite_master WHERE type='table' AND name=?;': not all arguments converted during string formatting'

As I couldn't find a solution to the errors I encountered, I decided to load the data using the GUI and then run the SQL queries by this way however as the file is too large I couldn't manage that either.

I did not have time to write the SQL queries but I would write something like this for the first problem:

 WITH cte AS(SELECT DISTINCT TRANSACTION_NUMBER FROM EXPENDITURE;)
 select COUNT(*) as total_transactions FROM cte;

 I feel like I could have solved the SQL queries if I had the data uploaded correctly.

## Question
If we had supplier_address as a column, how would you create a pipeline to extract the postcodes as another column (supplier_postcode) in the dataset?

- I would use a regex to get postcode data and store it in another column.