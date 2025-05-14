# Azure RAG Pipeline (Terraform + Azure AI Search + OpenAI)

This project demonstrates a Retrieval-Augmented Generation pipeline using Azure AI Search and Azure OpenAI. All resources are provisioned using Terraform.

## Steps

1. Run Terraform:
```bash
cd terraform
terraform init
terraform apply
```

2. Create the vector index:
```bash
python scripts/create_index.py
```

3. Upload documents:
```bash
python scripts/upload_documents.py
```

4. Run a semantic query:
```bash
python scripts/ask_rag.py
```

## Azure DevOps

Use `.azure-pipelines/azure-pipelines.yml` to automate the whole process.

## Techmakers

This article is brought by the resources of www.techmakers.co 
