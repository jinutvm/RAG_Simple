# Using Llama Index to perform RAG. 
# Changing the default OpenAI module and OpenAI embeddings

from dotenv import load_dotenv
load_dotenv()
import os

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

from llama_index.core import Settings

# changing the default openai to Anthropic
from llama_index.llms.anthropic import Anthropic
Settings.llm = Anthropic(model="claude-3-opus-20240229")

#changing the default openaiembedding to Voyageembedding
from llama_index.embeddings.voyageai import VoyageEmbedding
Settings.embed_model = VoyageEmbedding(voyage_api_key=os.getenv('VOYAGE_API_KEY'), model_name="voyage-2")

# will load all the files in the directory into documents
documents = SimpleDirectoryReader("./data").load_data()
#Load documents into Vector DB using vectorstore
index = VectorStoreIndex.from_documents(documents)
#Use the index for retrieval purposes
query_engine = index.as_query_engine()

# Provide the query and get the response from LLM
response = query_engine.query("Tell me about Agent Systems?")
print(response)