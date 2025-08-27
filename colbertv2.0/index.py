from ragatouille import RAGPretrainedModel

import json

#document_ids = []
documents = []
document_metadatas = []

with open("../data-prep/brand.jsonl", "r") as f:
    for line in f:
        data = json.loads(line)
        document_metadatas.append([
            {"entity": "image_name", "source": data["image_name"]},
            {"entity": "image_path", "source": data["image_path"]},
        ])
        documents.append(data["answer"])

RAG = RAGPretrainedModel.from_pretrained("colbert-ir/colbertv2.0")
indexer = RAG.index(
    index_name="brand",
    collection=documents,
    document_metadatas=document_metadatas,
)

# document_ids=document_ids,
# max_document_length=1000,
# split_documents=False,
