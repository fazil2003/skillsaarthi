from haystack.document_stores import InMemoryDocumentStore
from haystack.nodes import FARMReader, EmbeddingRetriever
from haystack.pipelines import ExtractiveQAPipeline

docs = [{"content": "You can apply for PMKVY scheme via your nearest training center."}]
doc_store = InMemoryDocumentStore()
doc_store.write_documents(docs)

retriever = EmbeddingRetriever(document_store=doc_store, embedding_model="sentence-transformers/all-MiniLM-L6-v2")
reader = FARMReader(model_name_or_path="distilbert-base-uncased", use_gpu=False)

pipe = ExtractiveQAPipeline(reader, retriever)
res = pipe.run(query="How to apply for PMKVY?", params={"Retriever": {"top_k": 1}, "Reader": {"top_k": 1}})
print(res["answers"][0].answer)
