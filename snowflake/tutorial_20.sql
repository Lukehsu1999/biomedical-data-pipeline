// Reference: https://docs.snowflake.com/en/user-guide/tutorials/snowflake-in-20minutes#create-snowflake-objects
// Create Database
CREATE OR REPLACE DATABASE sf_tuts;

SELECT CURRENT_DATABASE(), CURRENT_SCHEMA();

// Create Table
CREATE OR REPLACE TABLE emp_basic (
   first_name STRING ,
   last_name STRING ,
   email STRING ,
   streetaddress STRING ,
   city STRING ,
   start_date DATE
   );

// Create warehouse
CREATE OR REPLACE WAREHOUSE sf_tuts_wh WITH
   WAREHOUSE_SIZE='X-SMALL'
   AUTO_SUSPEND = 180
   AUTO_RESUME = TRUE
   INITIALLY_SUSPENDED=TRUE;

SELECT CURRENT_WAREHOUSE();