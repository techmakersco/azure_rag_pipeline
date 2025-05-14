from openai import AzureOpenAI
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

query = "What is GDPR and how is it handled?"

# Step 1: Embed the query
embedding = AzureOpenAIEmbeddings(...)
query_vector = embedding.embed_query(query)

# Step 2: Get top documents
search = SearchClient(...)
results = search.search(search_text=None, vector=query_vector, k_nearest_neighbors=3, vector_fields="contentVector")

context = "\n\n".join([r["content"] for r in results])

# Step 3: Ask OpenAI
client = AzureOpenAI(...)
response = client.chat.completions.create(
    deployment_id="gpt-4-turbo",
    messages=[
        {"role": "system", "content": "Answer with accurate info from context"},
        {"role": "user", "content": f"Context:\n{context}\n\nQuestion:\n{query}"}
    ]
)

print(response.choices[0].message.content)
