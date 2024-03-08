import requests

# Elasticsearch URL
elasticsearch_url = "http://localhost:9200"

# Index name
index_name = "cv-transcriptions_1"

def search_index(query):
    search_url = f"{elasticsearch_url}/{index_name}/_search"
    query_body = {
        "query": {
            "match": {
                "generated_text": query  # Replace with your specific field and query
            }
        }
    }

    response = requests.get(search_url, json=query_body)

    # Check the response
    if response.status_code == 200:
        results = response.json()
        print("Search results:")
        print(results)
    else:
        print("Failed to perform the search.")
        print(response.text)

if __name__ == "__main__":
    # Replace "your_query" with the actual query string
    search_query = "YOU HAVEN'T SEEN ANYTHING YET"

    search_index(search_query)
