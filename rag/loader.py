from langchain_community.document_loaders import PyPDFLoader
import os
def load_documents():
    docs=[]
    folder="documents"
    for file in os.listdir(folder):
        if file.endswith(".pdf"):
            loader=PyPDFLoader(
                os.path.join(folder,file)
            )
            docs.extend(loader.load())
    return docs