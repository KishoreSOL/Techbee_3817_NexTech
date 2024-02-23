# Import Essential dependencies
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

if __name__ == "__main__":
    # Path to save the FAISS database
    DB_FAISS_PATH = 'newvectorstore/db_faiss'
    
    # Paths to your PDF files
    pdf_paths = [ r"C:\Users\Sathish\machine learning\kriya\KCE-policies-and-Regulations-2021.pdf", r"C:\Users\Sathish\machine learning\kriya\students_info.pdf"]

    
    # Initialize the document list
    all_docs = []
    
    # Load and accumulate documents from both PDFs
    for pdf_path in pdf_paths:
        # Create a new PyPDFLoader instance for each PDF
        loader = PyPDFLoader(file_path=pdf_path)
        docs = loader.load()  # Load the current PDF
        all_docs.extend(docs)  # Add the loaded documents to the list
    
    # Initialize the text splitter
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    
    # Split all loaded documents
    splits = text_splitter.split_documents(all_docs)
    
    # Create the vectorstore from the split documents
    vectorstore = FAISS.from_documents(documents=splits, embedding=OpenAIEmbeddings(api_key="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"))
    
    # Save the vectorstore locally
    vectorstore.save_local(DB_FAISS_PATH)
