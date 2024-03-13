# Task 4
This README is designed for task 4. 

## Assumptions
1. No security concerns were considered 
2. Python 3.11 in installed on the OS
3. User has `sudo` and `docker` rights 

## Steps

1. Run `sudo bash setup.sh` to create the relevant docker networks and folders and configurations
2. Run `pip install -r requirements.txt` to install relevant libraries (`elasticsearch`)
2. Run `docker compose up -d` to run the relevant components
3. Run `python ingest.py` to create the relevant indexes and ingest the data
4. (Optional) Run `python query.py` to confirm if the indexes have been successfully generated

