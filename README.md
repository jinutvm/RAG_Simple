# RAG_Simple

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

### Explanation of Key Terminologies

**Vector**  
A vector is akin to an x-dimensional array. For instance, a 3-dimensional array [a, b, c] can be visualized on a 3-dimensional axis.

**Embeddings**  
Embeddings transform text into x-dimensional arrays based on their meanings. One widely used method, OpenAIEmbeddings, employs a 1024-dimensional vector. This means each chunk of text is converted into a 1024-parameter vector, which can be represented on a 1024-dimensional axis.

**Why Convert Text to Embeddings**  
Computers can understand numbers but not text. Therefore, vectors are utilized to compare and grasp the semantic meaning between texts, enabling computers to process and analyze textual information.

**Vector Store**  
Vector databases store these embedded vectors and are capable of searching for relevant chunks using various retrieval strategies, such as similarity search and Maximum Marginal Relevance (MMR).

### From Simple Implementation to Production-Ready: Navigating the Complexities of RAG

While implementing Retrieval Augmented Generation (RAG) can be straightforward with just a few lines of code, transitioning it to a production-ready system involves tackling numerous complexities. Let’s explore these challenges in detail.

We can begin by setting up a basic RAG system to demonstrate its capabilities. This initial setup will allow us to identify various challenges and assess the impact of different strategies on making the system robust and efficient for production use.

### Simple Implementation

**Programs**
I01_web_loader - Load data from the webpage, embed and store in vector store(Chroma db)

I02_askQ - Retrieve relevant documents and feed to LLM(Llama3) to respond to the queries

I03_chat - Use chat history along with the user ask. This will provide a conversation style of interaction.
