# Using Llama Index to extract and store in vector store DB

import pipes
from dotenv import load_dotenv
load_dotenv()
import os


# for changing the default settings
from llama_index.core import Settings

# changing the default openai to Anthropic
from llama_index.llms.anthropic import Anthropic
Settings.llm = Anthropic(model="claude-3-opus-20240229")

#changing the default openaiembedding to Voyageembedding
from llama_index.embeddings.voyageai import VoyageEmbedding
Settings.embed_model = VoyageEmbedding(voyage_api_key=os.getenv('VOYAGE_API_KEY'), model_name="voyage-2")

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

from llama_index.core import StorageContext 

# will load all the files in the directory into documents
documents = SimpleDirectoryReader("./data").load_data()
#Load documents into Vector DB using vectorstore
index = VectorStoreIndex.from_documents(documents)

#store the index persist
PERSIST_DIR = './storage'
index.storage_context.persist(persist_dir=PERSIST_DIR)
