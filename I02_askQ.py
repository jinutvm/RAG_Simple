# From ChromaDB get the relevant chunks using retriever.
# provide the chunks to llm for responding
# used llama3 through groq.
# used LCEL for chaining.

from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.vectorstores import Chroma
from langchain_voyageai import VoyageAIEmbeddings
from langchain_groq import ChatGroq
from operator import itemgetter
import os
from dotenv import load_dotenv
load_dotenv()


# Embeddings
embeddings = VoyageAIEmbeddings(
    voyage_api_key=os.getenv('VOYAGE_API_KEY'), model="voyage-2"
)
# connect to chroma db
vectorstore = Chroma(embedding_function=embeddings,
                     persist_directory="./chroma_db1k")

# define the retriever
retriever = vectorstore.as_retriever()

# prompt for the activity
template = """You are a helpful assistant. 

Answer the question based only on the following context:
{context}

Strictly DO NOT answer from outside context and if context is empty, respond back that No relevant information is available in the documents uploaded.  

Here is the current question

Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

# define the model
# using gemini
# model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
# using llama3 through Groq.
model = ChatGroq(temperature=0, model_name="Llama3-8b-8192")

# define the output parser
output_parser = StrOutputParser()


# define chain
rag_chain = (
    {"context": itemgetter("question") | retriever,
     "question": itemgetter("question")}
    | prompt
    | model
    | output_parser
)


print("Enter input below. Type EXIT to stop chat!")
while True:
    user_ask = input(">>")
    if user_ask.lower() == "exit":
        break
    result = rag_chain.invoke({"question": user_ask})
    print(">>>", result)
