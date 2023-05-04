**AdviseInc - Technical Exercise Plan - 120 minutes**

10 mins - Read Exercise
10 mins - Write Plan
5 mins - Prerequisites:
		a) Fork GitHub repo to personal account
		b) Check Snowflake credentials			
45 mins - Develop Python Script to load CSV file into Snowflake 
30 mins - Develop SQL queries, and export results to CSV files. (Export using Python). 
10 mins - Write README file including answers, instructions, issues and solutions.
10 mins - Proof-check exercise. 

Update: Ran out of time, spent longer than anticipated developing Python code and trouble shooting issues throughout the process (detailed below).

_____________________________________________
_____________________________________________

**Instructions -**

1. CSV file **must** be locally downloaded, and you must specify the file path of the CSV in the Python script in order to run the Python script. However, this script could function by creating a stage and uploading file elsewhere i.e. GCS buckets
2. You must input neccesary Snowflake Connection credentials when running this script (I have removed my sensitive data i.e. user/pass from script). So you will need to update the script where there is "{placeholder} in the code. 


_____________________________________________
_____________________________________________

**Issues - **

1. Forgot to specify role in the Snowflake connection, unable to run script for a little while (I suspected perhaps permissions based error at first) ~ 5-10 min delay. **Resolve**: Realised, and continued as normal. 
2. The CSV file in the GIT repository had dates in Transaction Number column. **Resolve**:  ON_ERROR = CONTINUE (not neccesarily reccomended).
3. Minor Python related errors when running script. Resolve: Swift troubleshooting. 
