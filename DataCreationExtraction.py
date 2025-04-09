import csv
from faker import Faker
import random
import string
from google.cloud import storage

# Initialize Faker
fake = Faker()

# Specify number of records to generate
num_records = 100

# Define character set for password
password_characters = string.ascii_letters + string.digits + 'm'

# List of U.S. states and cities
states = ["California", "Texas", "Florida", "New York", "Illinois", "Pennsylvania", "Ohio", "Georgia", "North Carolina", "Michigan"]
cities = ["Los Angeles", "New York", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "Austin"]
job_titles = ["Civil", "IT", "Mechanical", "Electrical", "Aeronautical"]

# Generate credit card data with additional columns
credit_card_data = []

for _ in range(num_records):
    # Generate a random year between 2020 and 2025
    random_year = random.randint(2020, 2025)

    record = {
        "first_name": fake.first_name(),  # string
        "last_name": fake.last_name(),  # string
        "job_title": fake.job(),  # string
        "department": fake.job(),  # string
        "email": fake.email(),  # string
        "address": fake.city(),  # string
        "phone_number": fake.phone_number(),  # string
        "credit_card_debt": round(random.uniform(500, 20000), 2),  # float
        "ssn": fake.ssn(),  # string
        "credit_score": random.randint(300, 850),  # int
        "password": ''.join(random.choice(password_characters) for _ in range(8)),  # string
        "year": random_year,  # random year between 2020 and 2025
        "state": random.choice(states),  # random state
        "city": random.choice(cities),  # random city
        "salary": random.randint(40000, 120000),  # salary as int
        "job": random.choice(job_titles)  # random job title
    }

    credit_card_data.append(record)

# Define CSV file name
csv_file_path = "credit_card_data.csv"

# Write data to CSV
with open(csv_file_path, mode="w", newline="") as file:
    fieldnames = credit_card_data[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(credit_card_data)

# Upload CSV file to Google Cloud Storage
def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to GCS."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)
    print(f"File {source_file_name} uploaded to {destination_blob_name} in bucket {bucket_name}.")

# Replace with your GCS bucket name
bucket_name = "ccdataexploration"
destination_blob_name = "credit_card_data.csv"

# Upload file
upload_to_gcs(bucket_name, csv_file_path, destination_blob_name)
