# ETL Data Pipeline on Google Cloud using Cloud Data Fusion, Airflow, and Looker Studio

# Overview
This project demonstrates the creation of a complete ETL (Extract, Transform, Load) pipeline using Google Cloud Platform (GCP) tools — particularly Cloud Data Fusion, Google Cloud Storage (GCS), BigQuery, and Apache Airflow. The pipeline is designed to handle synthetic credit card/employee data and visualize it in Looker Studio.
 
Step-by-Step Workflow

Step 1: Data Extraction with Python
A Python script (DataCreationExtraction.py) is developed to simulate the data extraction phase:
•	Faker Library Initialization
The script starts by importing necessary modules, including Faker, csv, and GCP's storage library. The Faker library is initialized to generate fake but realistic data.
•	Data Definition
It defines a character set for password generation (letters, digits, and a custom character), and lists of U.S. states, cities, and job titles for randomized input.
•	Synthetic Data Generation
A loop runs 100 times to generate synthetic records. For each record, the following fields are created:
•	Personal information (first/last name, SSN, email, phone number, address)
•	Employment details (job title, department, salary)
•	Credit details (credit score and debt)
•	A randomly generated password
•	Randomized metadata like year, state, city
•	CSV File Creation
These records are written to a CSV file named credit_card_data.csv. Field names are auto-generated based on the dictionary keys in the first record.
•	Upload to Google Cloud Storage (GCS)
The file is uploaded to a GCS bucket named ccdataexploration. This is done using the google.cloud.storage library, where:
•	The GCS client is initialized
•	The target bucket and blob (file object) are defined
•	The local file is uploaded to the cloud bucket
 
Step 2: Workflow Automation with Airflow
An Apache Airflow DAG (dag.py) is created to automate and orchestrate the pipeline:
•	DAG Configuration
The DAG is named CCdata and is scheduled to run daily. It starts on December 18, 2023. It has built-in retry logic (1 retry with a 5-minute delay) but does not send emails on failure or retry.
•	Task - BashOperator
A single task is defined that runs a Bash command. This command executes the Python script (DataCreationExtraction.py) that generates the synthetic data and uploads it to GCS. The script is assumed to reside in /home/airflow/gcs/dags/scripts/.
•	Purpose
Automating this step ensures that the pipeline always works with fresh data daily without manual intervention.
 
Step 3: Data Transformation with Cloud Data Fusion
Cloud Data Fusion is used to design a visual, code-free ETL pipeline:
•	Instance Setup
A Cloud Data Fusion instance is created to manage data integration and transformation.
•	Pipeline Creation
The pipeline:
o	Ingests the data from the specified GCS bucket
o	Transforms the data (e.g., renaming fields, converting data types)
o	Masks sensitive information such as SSNs or email addresses for data privacy
o	Loads the cleaned and transformed data into a target BigQuery table for analysis
 
Step 4: Data Visualization with Looker Studio
•	Once the transformed data is available in BigQuery, Looker Studio is used for the visualization layer.
•	Looker Studio connects to the BigQuery dataset to build interactive dashboards.
•	Visualizations include metrics like:
•	Average credit score
•	Salary distributions
•	Job title breakdowns
•	Debt vs. income trends
 
Summary of Technologies Used

Component	Tool/Service	Purpose
Data Generation	Python + Faker	Create synthetic employee/credit card data
Data Storage	Google Cloud Storage (GCS)	Store raw CSV files
Orchestration	Apache Airflow	Automate data creation and upload
ETL/Transformation	Cloud Data Fusion	Build data pipelines, apply transformations
Data Warehouse	BigQuery	Store transformed data for querying
Data Visualization	Looker Studio	Build dashboards and data reports
 
Conclusion:
This project serves as a practical, end-to-end demonstration of building an ETL pipeline in the cloud using GCP’s suite of services. It highlights automation, data transformation, secure handling of sensitive data, and visualization — all critical components of a modern data engineering workflow.

