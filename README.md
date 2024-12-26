# EMG Signal Data Pipeline
## Objective: 
Build a scalable data pipeline to process, analyze, and visualize real-time EMG signals. This can demonstrate handling large, continuous data streams and extracting actionable insights.

## Steps to Reproduce:
### 1. Download Apache Nifi
Reference: https://nifi.apache.org/nifi-docs/getting-started.html <br>
Snowflake-related processors are not built in, you need to get their nar file and put them under your $(brew --prefix nifi)/libexec/lib folder <br>
They are available here: https://repo.maven.apache.org/maven2/org/apache/nifi/ <br>
Or you can simply run these commands under /lib folder: <br>
```
wget https://repo.maven.apache.org/maven2/org/apache/nifi/nifi-snowflake-processors-nar/2.0.0/nifi-snowflake-processors-nar-2.0.0.nar

wget https://repo.maven.apache.org/maven2/org/apache/nifi/nifi-snowflake-services-api-nar/2.0.0/nifi-snowflake-services-api-nar-2.0.0.nar

wget https://repo.maven.apache.org/maven2/org/apache/nifi/nifi-snowflake-services-nar/2.0.0/nifi-snowflake-services-nar-2.0.0.nar
```

<br>
Hadoop related files are these: <br>
```
https://repo.maven.apache.org/maven2/org/apache/nifi/nifi-hadoop-libraries-nar/2.0.0/nifi-hadoop-libraries-nar-2.0.0.nar

https://repo.maven.apache.org/maven2/org/apache/nifi/nifi-hadoop-nar/2.0.0/nifi-hadoop-nar-2.0.0.nar
```

### 2. Download the flow you want from /nifi-flows

### 3. Upload to Apache Nifi
On your canvas, create "Process Group"
Click the "Browse" icon next to the group name,
Search for the downloaded flow and upload it.

#### 3.1 Sample_Flow.json
Note that you might have to enable some controllers in the group before running the flow.

#### 3.2 Put_Object_S3.json
* Note that I have specifically removed the AWS Credentials Provider Controller to protect my access key <br>
1. Go to AWS IAM, create a new user with AmazonS3FullAccess policy <br>
2. In user's Security Credentials, create new Access Key and copy Access Key and Secret Access Key <br>
3. Go to AWS S3, create a new bucket with public access, copy bucket name and region <br>
4. Upload the Put_Object_S3.json flow to nifi <br>
5. In the PutS3Object component, specify Bucket and Region <br>
6. For AWS Credentials Provider Service, create new controller, put in Access Key and Secret Access Key <br>


## Steps to Build the Project:
### 1. Simulate or Collect EMG Signals:

Use existing EMG signal data from the Mio band or simulate EMG signals in Python if access is limited.
Format the data to include time-series values for 8 channels, labeled with timestamps.
### 2. Stream the Data:

Use Apache Kafka to stream the continuous EMG signals into a data pipeline. Kafka is ideal for real-time applications.
Alternatively, you can use Apache NiFi for ease of use in building a streaming pipeline.
### 3. Ingest and Store Data:

Store raw data in a data lake (e.g., Amazon S3 or Google Cloud Storage) for long-term storage and batch processing.
For structured data analysis, save processed data into a Snowflake database or a SQL-based database.
### 4. Process Data (ETL):

Use PySpark or Python (Pandas) for real-time data processing, including:
Filtering out noise or artifacts in the EMG signals.
Extracting key metrics like muscle activation patterns, frequency domain features, or signal amplitude trends.
Transform and prepare the data for machine learning or statistical analysis.
### 5. Analyze Data:

Develop algorithms to detect patterns, such as specific gestures or anomalies in muscle activity.
Use ML models or rule-based systems to classify muscle movements or detect anomalies in signal patterns.
### 6. Visualize Insights:

Build real-time dashboards with Tableau or Power BI to show EMG signal trends, channel activation, and classification results.
Alternatively, use Python libraries like Plotly or Matplotlib.
### 7. Implement CI/CD:

Set up a CI/CD pipeline using GitHub Actions or Jenkins for deploying updates to the pipeline and machine learning models.
### 8. Deploy on Cloud:

Deploy the pipeline on AWS EC2 or Google Cloud VM for scalability and integration with cloud-native tools.

## References
1. Apache Nifi: https://nifi.apache.org/nifi-docs/getting-started.html <br>
2. Running Scripts on Apache NiFi:<br>
   Python Interpreter/Command Path: get the poetry environment path: <br>
   ```
   poetry env info --path
   ```
   Then put the {path to poetry env}/bin/python in the Command Path in Processors

