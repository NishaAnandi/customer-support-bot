from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from rag.loader import load_documents
def create_vectorstore():
    docs=load_documents()
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    splits=splitter.split_documents(docs)
    embedding=HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vectorstore=FAISS.from_documents(
        splits,
        embedding
    )
    vectorstore.save_local("faiss_index")
    return vectorstore