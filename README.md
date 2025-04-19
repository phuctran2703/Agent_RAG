# Retrieval-Augmented-Generation (RAG)

## Introduction

Agent_RAG is a demo project that builds a simple Retrieval-Augmented Generation (RAG) agent, combining the power of **LangGraph**, **LangChain**, and an external search tool (**DuckDuckGoSearch**) to enhance the agent’s ability to answer user queries.

The code is implemented in a Jupyter Notebook for educational purposes and quick experimentation.  
[Colab Link](https://colab.research.google.com/drive/1GLlEQ04ULiJP03Pbo7jCFcIvR9kDuz-4?usp=sharing)

## Notebook Structure

**The notebook consists of 4 main parts:**

### Creating vector embeddings from data
- Uses the embedding model `sentence-transformers/all-mpnet-base-v2` to encode PDF content into vector embeddings.
- These vectors are stored in a **Chroma vector store** for semantic search purposes.

### Building RAG with LangGraph
- Utilizes **LangGraph** to design a simple processing graph for the RAG task.
- Maps the data flow between steps such as: retrieving documents → generating prompt → producing answers.
- Helps visualize the processing pipeline clearly and makes components easier to manage.

### Creating a search-augmented Agent (DuckDuckGo) using LangChain
- Builds a **RAG Agent** using `langchain.agents` that can perform real-time external searches.
- Integrates **DuckDuckGoSearch** to fetch data from the web.
- The agent automatically decides when to use the search tool and how to synthesize the final response.

### Evaluating response quality
- Uses the dataset from [Kaggle - Question-Answer Dataset](https://www.kaggle.com/datasets/rtatman/questionanswer-dataset).
- Performs manual evaluation of the agent model's answers based on predefined criteria.

## App 
The RAG App is a minimal web-based interface designed to interact with the RAG agent in real-time. It provides an accessible front-end for users to input questions and receive responses powered by both the local knowledge base (vector store) and live web search.

### Key Features
- **Interactive Chat Interface:** Users can type natural language queries and receive contextual responses from the RAG agent.

- **Dynamic Tool Use:** The agent decides whether to use the internal knowledge (PDF embeddings) or trigger an external web search (DuckDuckGo) depending on the query complexity.

- **Streaming Output:** Implemented with support for streaming responses to improve user experience and responsiveness
  
### How to Run
- Give your api into docker-compose.
- Create image by ```docker build -t rag-agent .```
- Run container by ```docker compose up -d```
- Access link ```localhost:8000```

### Interface
![Screenshot 2025-04-18 185907](https://github.com/user-attachments/assets/ea4f21d8-008d-41fa-b16d-ffffd783a111)

**Interface includes 2 part:**
1. Upload your file pdf
Users can upload any PDF document they wish to interact with. This file will be processed and its content extracted to enable meaningful conversations with the chatbot. The upload feature supports drag-and-drop as well as manual file selection.
2. Chat with chatbot
After uploading the PDF, users can ask questions or make requests related to the content of the document.
