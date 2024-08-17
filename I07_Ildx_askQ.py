from dotenv import load_dotenv
load_dotenv()
import os

from llama_index.core import StorageContext,load_index_from_storage

# for changing the default settings
from llama_index.core import Settings

# changing the default openai to Anthropic
from llama_index.llms.anthropic import Anthropic
Settings.llm = Anthropic(model="claude-3-opus-20240229")

#changing the default openaiembedding to Voyageembedding
from llama_index.embeddings.voyageai import VoyageEmbedding
Settings.embed_model = VoyageEmbedding(voyage_api_key=os.getenv('VOYAGE_API_KEY'), model_name="voyage-2")


PERSIST_DIR='./storage'
storage_content = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
index = load_index_from_storage(storage_content)

query_engine = index.as_query_engine()
result = query_engine.query("What is Article2?")
print(result)
