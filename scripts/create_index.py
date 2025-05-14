import requests
import os

AZURE_SEARCH_ENDPOINT = "https://<your-search>.search.windows.net"
AZURE_SEARCH_KEY = "<your-key>"

headers = {
    "Content-Type": "application/json",
    "api-key": AZURE_SEARCH_KEY
}

index_payload = {
    "name": "docs-index",
    "fields": [
        {"name": "id", "type": "Edm.String", "key": True},
        {"name": "content", "type": "Edm.String"},
        {
            "name": "contentVector",
            "type": "Collection(Edm.Single)",
            "searchable": True,
            "vectorSearchDimensions": 1536,
            "vectorSearchConfiguration": "default"
        }
    ],
    "vectorSearch": {
        "algorithmConfigurations": [
            {
                "name": "default",
                "kind": "hnsw",
                "parameters": {
                    "m": 4,
                    "efConstruction": 400,
                    "efSearch": 500
                }
            }
        ]
    }
}

resp = requests.put(
    f"{AZURE_SEARCH_ENDPOINT}/indexes/docs-index?api-version=2023-07-01-Preview",
    headers=headers,
    json=index_payload
)

print(resp.status_code, resp.json())
