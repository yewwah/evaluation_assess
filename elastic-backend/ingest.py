from elasticsearch import Elasticsearch, helpers
import csv

# Elasticsearch connection
es = Elasticsearch(['http://localhost:9200'])

# Index name
index_name = "cv-transcriptions"

# CSV file path
csv_file_path = "cv-valid-dev.csv"  # Replace with your actual CSV file path

def infer_field_types(csv_file):
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        # Infer field types from the first row of the CSV
        sample_row = next(csv_reader)

        field_types = {}
        for field, value in sample_row.items():
            if value.isdigit():
                field_types[field] = "integer"
            elif value.replace(".", "", 1).isdigit():
                field_types[field] = "float"
            else:
                field_types[field] = "text"

    return field_types

def create_index(field_types):
    # Create index mapping based on inferred field types
    mapping = {"properties": {field: {"type": field_type} for field, field_type in field_types.items()}}

    # Create the index
    es.indices.create(index=index_name, body={"mappings": mapping}, ignore=400)  # ignore 400 Index Already Exists

def index_data(field_types):
    # Open and read CSV file
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        # Bulk index data
        bulk_data = []
        for row in csv_reader:
            # Convert field types based on inferred types
            converted_row = {field: int(row[field]) if field_types[field] == "integer" else
                             float(row[field]) if field_types[field] == "float" else row[field] for field in row}

            action = {
                "_op_type": "index",
                "_index": index_name,
                "_source": converted_row
            }
            bulk_data.append(action)

        # Use the bulk helper to send the data
        response = helpers.bulk(es, bulk_data)

        # Check the response
        if response[0] == len(bulk_data):
            print("Data indexed successfully.")
        else:
            print("Failed to index data.")

if __name__ == "__main__":
    # Infer field types from the CSV file
    field_types = infer_field_types(csv_file_path)

    # Create the Elasticsearch index
    create_index(field_types)

    # Index CSV data into Elasticsearch
    index_data(field_types)
