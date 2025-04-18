# ========== Import Modules ==========
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.tools import Tool, tool
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

from langgraph.prebuilt import create_react_agent
from langchain_huggingface import HuggingFaceEmbeddings
from pydantic import BaseModel
from app.helper import *

# ========== Configuration ==========
LLM_NAME = "qwen-qwq-32b"
VECTOR_STORE_DIR = "./chroma_db"
COLLECTION_NAME = "rag_collection"

# ========== Initialize Components ==========

# Initialize LLM
llm = init_chat_model(LLM_NAME, model_provider="groq")

# Initialize embeddings
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")


# Initialize vector store
vector_store = Chroma(
    collection_name=COLLECTION_NAME,
    embedding_function=embedding,
    persist_directory=VECTOR_STORE_DIR
)

# ========== Document Processing ==========
def add_pdf_to_vectorstore(pdf_path: str) -> None:
    """Load PDF, split into chunks, and add to vector store."""
    documents = PyPDFLoader(pdf_path).load()
    chunks = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    ).split_documents(documents)
    vector_store.add_documents(chunks)

# ========== Tools ==========
class RetrieveDocumentsInput(BaseModel):
    query: str

@tool
def retrieve_documents(query: str) -> str:
    """Search vector store and return top results."""
    results = vector_store.similarity_search(query, k=5)
    content = "\n\n".join(
        f"Source: {doc.metadata}\nContent: {doc.page_content}" for doc in results
    )
    return content

# Wrap tool
retrieve_documents_tool = Tool(
    name="retrieve_documents",
    description="Retrieve information related to user's query. Parameters include query.",
    func=retrieve_documents,
    args_schema=RetrieveDocumentsInput
)

search_tool = DuckDuckGoSearchRun()

tools = [retrieve_documents_tool, search_tool]
rag_model = create_react_agent(llm, tools)

# ========== Query ==========
def query_llm(prompt: str) -> str:
    """Helper for sending a user message to the model with a system prompt."""
    system_prompt = (
        "You are a smart and multilingual assistant for answering user questions in their native language. "
        "Depending on the question, you may:\n\n"
        "1. Answer immediately if you already know the answer.\n"
        "2. If you do not know the answer, attempt to retrieve information from the provided documents.\n"
        "3. If the documents are missing the necessary information or are insufficient, search the web for the most accurate and up-to-date response.\n\n"
        "You must:\n"
        "- Answer using the language of the user’s question.\n"
        "- Provide a detailed answer, using a maximum of 2000 sentences.\n"
        "- Clearly specify which parts of the answer come from retrieved documents and which parts come from web search.\n"
        "- If none of the sources provide sufficient data, explain that and give the best possible answer based on general knowledge.\n\n"
        "Your responses must be highly detailed, precise, and aligned with the user’s context."
    )

    response = rag_model.invoke({
        "messages": [
            SystemMessage(content=system_prompt),
            HumanMessage(content=prompt)
        ]
    })

    return response['messages'][-1].content
