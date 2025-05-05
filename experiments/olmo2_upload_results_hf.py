# Python code to upload
from huggingface_hub import HfApi
import os

# Initialize the API
api = HfApi()

# Login (you'll need to generate a token from your HF account settings)
api.login()

# Create a new dataset repository
dataset_name = "Neelectric/OLMo-2-1124-7B-Instruct_ROME_causal-trace-results"
api.create_repo(repo_id=dataset_name, repo_type="dataset")

# Upload all files in the directory
api.upload_folder(
    folder_path="/home/rome/results",  # Path to your results folder
    repo_id=dataset_name,
    repo_type="dataset"
)