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
