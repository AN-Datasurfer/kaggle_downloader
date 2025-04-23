''' It is used to download datasets from the internet

  Download the dataset from Kaggle using Kaggle API

 Ensure you have the Kaggle API installed
You can install it using pip if you haven't already : pip install kaggle

Make sure to set your Kaggle API credentials in the environment variables KAGGLE_USERNAME and KAGGLE_KEY.
You can do this on  Kaggle's website by going to your account settings and creating a new API token. This will download a file called kaggle.json, which contains your credentials.

Alternatively, you can set them directly in the script (not recommended for security reasons) '''

# Import necessary libraries
import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Set Kaggle credentials directly
os.environ['KAGGLE_USERNAME'] = 'your_kaggle_username'
os.environ['KAGGLE_KEY'] = 'your_kaggle_api_key'

# Authenticate
api = KaggleApi()
api.authenticate()

# Define the dataset path
dataset = 'oluwademiladeadeniyi/mtn-nigeria-customer-churn'
# Download dataset
api.dataset_download_files(dataset, path='datasets', unzip=True)
print(f"Dataset {dataset} downloaded and unzipped successfully.")

