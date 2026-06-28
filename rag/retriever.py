from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
vectorstore = FAISS.load_local(
    "faiss_index",
    embedding,
    allow_dangerous_deserialization=True
)
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)
def retrieve_context(query: str) -> str:
    """
    Retrieve the top 3 relevant document chunks for a query.
    """
    docs = retriever.invoke(query)
    context = "\n\n".join(doc.page_content for doc in docs)
    return context