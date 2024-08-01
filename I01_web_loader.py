# load data from the webpage.
# RecursiveCharactor Text splitter is used to split into chunks. Chunk size and chunk Overlap mentioned.
# Voyage embeddings used to embed chunks
# ChromaDB vector DB is used in this exercise.


from langchain_community.vectorstores import Chroma
from langchain_voyageai import VoyageAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader

import os
from dotenv import load_dotenv
load_dotenv()


# Retrive from the web and get the content as Documents.
loader = WebBaseLoader(
    web_paths=("https://en.wikipedia.org/wiki/Kerala",)
)
docs = loader.load()


# Split
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)

# embeddings
embeddings = VoyageAIEmbeddings(
    voyage_api_key=os.getenv('VOYAGE_API_KEY'), model="voyage-2"
)

# store in vector db.
vectorstore = Chroma.from_documents(
    documents=splits, embedding=embeddings, persist_directory="./chroma_db1k")
