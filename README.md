# RAG_Basic

### Retrieval Augmented Generation (RAG)

Language models (LLMs) are highly capable of providing information on a wide range of topics because they are trained on publicly available data. This extensive training enables their widespread use across various applications. However, one significant limitation of LLMs is their lack of access to proprietary information from companies or individuals, as they cannot access or learn from such restricted data.

To address this gap, Retrieval Augmented Generation (RAG) is employed. RAG enhances the response accuracy of LLMs by allowing them to pull information from specific documents, ensuring that the answers are based on precise and relevant sources.

### Retrieval Augmented Generation (RAG) Steps:

1. **Storing Documents in a Vector Store:**

   - Documents (such as PDFs, web pages, etc.) are divided into chunks, or smaller pieces of text.
   - These chunks are then embedded and stored in a vector store.

2. **Retrieving Relevant Text:**

   - The question is embedded using the same technique that was used to store the document chunks.
   - The question embedding is then searched within the vector store to find the relevant chunk embeddings that are closest to it.

3. **Generating Answers from Retrieved Context:**
   - The relevant chunks obtained from the vector store are provided to the LLM along with the question.
   - The LLM then answers the question based on the context provided by these chunks.

### From Simple Implementation to Production-Ready: Navigating the Complexities of RAG

While implementing Retrieval Augmented Generation (RAG) can be straightforward with just a few lines of code, transitioning it to a production-ready system involves tackling numerous complexities. Let’s explore these challenges in detail.

We can begin by setting up a basic RAG system to demonstrate its capabilities. This initial setup will allow us to identify various challenges and assess the impact of different strategies on making the system robust and efficient for production use.

### Basic RAG

**Programs**
I01_web_loader - Load data from the webpage, embed and store in vector store(Chroma db)

I02_askQ - Retrieve relevant documents and feed to LLM(Llama3) to respond to the queries

I03_chat - Use chat history along with the user ask. This will provide a conversation style of interaction.

**Detailed Explanation**

#### Load the data into Vector store (Module Name: I01_web_loader.py)

1. Using Webloader, retrieve the data from a wikipedia website. Response will be as Documents 
2. Split the documents using RecursiveCharactorTextSplitter with chunk size as 1000 and overlap as 200
3. Embed the chunks using `VoyageAIEmbeddings`.
4. Store the chunks into Vectorstore (Chroma DB).


#### Ask Question to the document (Module Name: I02_askQ.py)

1. Define the embeddings. User questions will be converted into embeddings before searching in the vector store. Make sure to use the same embedding methodology used to store the content in the Vector Store, in this case we use VoyageAIEmbeddings.
2. Connect to ChromaDB to search for relevant chunks
3. Define the retriever. Here, we use VectorStore as the backbone for Retrievers.
4. Define the model to be used (LLAMA3 used through Groq).
5. Define the prompt to be given to the model in order to perform the task.
6. Define the output parser to parse the results from the model
7. Create the chain using LCEL. Below steps will be performed in sequence. 
   - Using UserAsk, call the retriever to retrieve relevant chunks based on the user question (search will happen using embeddings, but response will be actual text) and provide the results to dict key “context”
   - User Ask is passed to dict key “question”
   - Invoke prompt which will reformat the prompt by replacing context and question given as input
   - Call the model using the updated prompt which contains the context and question.
   - Pass the response from the model to the output parser to retrieve the relevant information from the LLM response.(Along with the answer, LLM will provide many other parameters).
8. Invoke the Chain with the user ask.


#### Include Chat history also in the conversation (Module Name: I03_chat.py)

The same process as mentioned above is followed with a few changes:
1. Prompt will have an additional chat_history parameter as well
2. Using built-in module, ChatMessageHistory to store user ask and AI response. 
3. While invoking the chain, along with the user ask, `chat_history` will also be provided.


