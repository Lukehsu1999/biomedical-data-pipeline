/*--
Reference: https://docs.snowflake.com/en/user-guide/tutorials/load-from-cloud-tutorial#introduction
For setting up AWS integration: https://docs.snowflake.com/en/user-guide/data-load-s3-config-storage-integration
--*/
USE ROLE ACCOUNTADMIN;

USE WAREHOUSE compute_wh;

CREATE OR REPLACE DATABASE cloud_data_db
  COMMENT = 'Database for loading cloud data';

CREATE OR REPLACE SCHEMA cloud_data_db.s3_data
  COMMENT = 'Schema for tables loaded from S3';

/*--
Using the emp_basic table because we already have its csv data files
--*/
CREATE OR REPLACE TABLE cloud_data_db.s3_data.emp_basic (
   first_name STRING ,
   last_name STRING ,
   email STRING ,
   streetaddress STRING ,
   city STRING ,
   start_date DATE
   );

SELECT * FROM cloud_data_db.s3_data.emp_basic;

/*--
Create a Storage Integration
--*/

CREATE OR REPLACE STORAGE INTEGRATION s3_data_integration
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = 'S3'
  STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::238592221641:role/mysnowflakerole'
  ENABLED = TRUE
  STORAGE_ALLOWED_LOCATIONS = ('s3://luketestsnowflakebucket/');

---> Get these two information for AWS: STORAGE_AWS_IAM_USER_ARN, STORAGE_AWS_EXTERNAL_ID
DESCRIBE INTEGRATION s3_data_integration;

/*--
Create a Stage
--*/
CREATE OR REPLACE STAGE cloud_data_db.s3_data.s3data_stage
  STORAGE_INTEGRATION = s3_data_integration
  URL = 's3://luketestsnowflakebucket/'
  FILE_FORMAT = (TYPE = CSV);

SHOW STAGES;

/*--
Load data from stage
--*/
COPY INTO cloud_data_db.s3_data.emp_basic
  FROM @cloud_data_db.s3_data.s3data_stage
    FILES = ('employees05.csv');

SELECT * FROM cloud_data_db.s3_data.emp_basic;


