# Using Llama Index to perform RAG. 
# Uses default OpenAI module and OpenAI embeddings

from dotenv import load_dotenv
load_dotenv()

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

# will load all the files in the directory into documents
documents = SimpleDirectoryReader("./data").load_data()
#Load documents into Vector DB using vectorstore
index = VectorStoreIndex.from_documents(documents)
#Use the index for retrieval purposes
query_engine = index.as_query_engine()

# Provide the query and get the response from LLM
response = query_engine.query("Explain more about LSH?")
print(response)