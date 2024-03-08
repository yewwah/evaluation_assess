#!/bin/bash

# Creating the docker network for internal mapping across multiple folders 
docker network create es-network


folder_path_1="es_data_1"
folder_path_2="es_data_2"
# Check if the folder exists
if [ -d "$folder_path_1" ]; then
    echo "Folder already exists."
else
    # Create the folder
    mkdir -p "$folder_path_1"
    echo "Folder created successfully."
fi

# Check if the folder exists
if [ -d "$folder_path_2" ]; then
    echo "Folder already exists."
else
    # Create the folder
    mkdir -p "$folder_path_2"
    echo "Folder created successfully."
fi

# Setting max vm counts for elastic search 
sysctl -w vm.max_map_count=262144
