## Notes

This proved more challenging than I thought as I had never used snowflake before. Was not able to really get started. Apologies.

Kind Regards,
Navkaran Randhawa

# Technical exercise

## Exercise Description:

You are provided with a dataset containing NHS spending information. Your task is to use Python to load this data into Snowflake, perform some SQL queries on it, and export the results to a CSV file.

### Dataset:

This is an open source dataset, which can be found [here](https://www.kaggle.com/datasets/deepaktejasvisingh/expenditure-in-the-salisbury-nhs-v2). It contains spending details from 2010 to 2020 by Salisbury NHS Foundation Trust.
The dataset is in CSV format and contains the following fields:

- Department Family: cleansed to a single value for our specific dataset(Department of Health).
- Entity: cleansed to a single value for our specific dataset (Salisbury NHS Foundation Trust).
- Date: date of expenditure.
- Expense Type: category the expense falls under.
- Expense Area: area the expense falls under.
- Supplier: provider of the service or product.
- Transaction Number: transaction identifier (note that more than one line of spending can be included in the same transaction).
- Expenditure: money spent.

### Requirements:

1. Use Python to connect to the Snowflake database.
2. Create a Snowflake database and schema for this exercise.
3. Load the data from the CSV file into Snowflake using Python.
4. Write SQL queries to answer the following questions:
   - How many transactions are in the dataset?
   - What is the average yearly spend for Salisbury NHS Foundation Trust?
   - Who are the top 3 Suppliers by spend in 2018?
   - Which Expense Area has the highest spend overall?
   - How many suppliers are in the dataset?
5. Export the results of each query to a CSV file using Python.
6. Include answers to the following questions in your README:
   - If we had supplier_address as a column, how would you create a pipeline to extract the postcodes as another column (supplier_postcode) in the dataset?

### Instructions:

- Fork this GitHub repository to your personal account.
- Write the Python code to load the data into Snowflake, perform the SQL queries, and export the results to CSV files. You will need to create the objects you need inside your Snowflake database - see instructions for connecting to Snowflake below.
- Commit and push your changes to your branch.
- Create a pull request to merge your changes into the main branch of this repository.
- Include a README file with instructions on how to run your code and any relevant information about your solution (e.g. include how you have created the schema and tables you are using, if you experienced any issues with the exercise and how you resolved them, etc)

### Connecting to Snowflake

- You will receive a username and password via email
- Login to Snowflake [here](https://rvktngg-iu56961.snowflakecomputing.com/console/login) - you will be prompted to change your password
- You will be able to see a database with your name on - you have full access to this database.

### Evaluation:

Your solution will be evaluated based on the following criteria:

- Correctness of the SQL queries.
- Use of Python best practices.
- Efficiency of the code.
- Quality and clarity of the README file.

### Useful docs:

- [Snowflake copy into examples](https://docs.snowflake.com/en/sql-reference/sql/copy-into-table#examples)
- [Snowflake copy options](https://docs.snowflake.com/en/sql-reference/sql/copy-into-table#copy-options-copyoptions)
