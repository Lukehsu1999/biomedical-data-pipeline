// 1. Create Snowflake Objects Reference: https://docs.snowflake.com/en/user-guide/tutorials/snowflake-in-20minutes#create-snowflake-objects
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

// 2. Stage Data Files Reference: https://docs.snowflake.com/en/user-guide/tutorials/snowflake-in-20minutes#stage-data-files
// Upload the csv file to the stage
PUT file:///Users/lukehsu/Desktop/biomedical-data-pipeline/snowflake/getting-started/employees0*.csv @sf_tuts.public.%emp_basic;

// List the files in the stage
LIST @sf_tuts.public.%emp_basic;

// 3. Copy data into target table reference: https://docs.snowflake.com/en/user-guide/tutorials/snowflake-in-20minutes#copy-data-into-target-tables
COPY INTO emp_basic
  FROM @%emp_basic
  FILE_FORMAT = (type = csv field_optionally_enclosed_by='"')
  PATTERN = '.*employees0[1-5].csv.gz'
  ON_ERROR = 'skip_file';