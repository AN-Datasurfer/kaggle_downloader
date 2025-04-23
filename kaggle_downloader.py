#it is used to download datasets from the internet

# Download the dataset from Kaggle using Kaggle API

# Ensure you have the Kaggle API installed
# pip install kaggle
# Make sure to set your Kaggle API credentials in the environment variables
# Alternatively, you can set them directly in the script (not recommended for security reasons)

# Import necessary libraries
import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Set Kaggle credentials directly
os.environ['KAGGLE_USERNAME'] = 'your_kaggle_username'
os.environ['KAGGLE_KEY'] = 'your_kaggle_api_key'

# Authenticate
api = KaggleApi()
api.authenticate()

# Download dataset
api.dataset_download_files('abdulmalik1518/mobiles-dataset-2025', path='datasets', unzip=True)
