from rag.vectorstore import create_vectorstore
if __name__ == "__main__":
    print("Building FAISS vector store...")
    create_vectorstore()
    print("Vector store created successfully!")