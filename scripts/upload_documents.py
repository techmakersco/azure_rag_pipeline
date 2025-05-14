from openai import AzureOpenAIEmbeddings
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from langchain.text_splitter import RecursiveCharacterTextSplitter
import uuid

# Configure Azure OpenAI
embedding = AzureOpenAIEmbeddings(
    azure_deployment="text-embedding-ada-002",
    azure_endpoint="https://<your-openai>.openai.azure.com",
    api_key="<your-openai-key>"
)

# Load and split documents
with open("faq.txt") as f:
    raw_text = f.read()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.split_text(raw_text)

# Get embeddings and upload to Azure AI Search
client = SearchClient(
    endpoint="https://<your-search>.search.windows.net",
    index_name="docs-index",
    credential=AzureKeyCredential("<your-search-key>")
)

batch = []
for i, chunk in enumerate(docs):
    vector = embedding.embed_query(chunk)
    batch.append({
        "id": str(uuid.uuid4()),
        "content": chunk,
        "contentVector": vector
    })

client.upload_documents(documents=batch)
