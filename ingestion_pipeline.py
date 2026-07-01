import os 
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()

def load_documents(docs_path="docs"):
    print(f"loading documents from {docs_path}")
    if not os.path.exists(docs_path):
        raise FileNotFoundError(f"The directory {docs_path} does not exist")
    
    loader=DirectoryLoader(path=docs_path ,glob="*.txt" ,loader_cls=TextLoader)

    documents=loader.load()

    if len(documents)==0:
        raise FileNotFoundError(f"No .txt file in {docs_path}")
    
    for i,doc in enumerate(documents[:2]):
        print(f"\nDocument {i+1}:")
        print(f" Source: {doc.metadata['source']}")
        print(f" Content Length: {len(doc.page_content)} characters")
        print(f" Content Preview: {doc.page_content[:100]}...")
        print(f" metadata: {doc.metadata}")
    
    return documents

def split_docs(documents, chunk_size=500, chunk_overlap=200):
    print("splitting documents into chunks...")
    textsplitter=CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks=textsplitter.split_documents(documents)

    if chunks:
        for i, chunk in enumerate(chunks[:5]):
            print(f"\n -- chunk {i+1} --")
            print(f"Source: {chunk.metadata['source']}")
            print(f"Length: {len(chunk.page_content)} characters")
            print(f"Content:")
            print(chunk.page_content)
            print("-" *50)
        
        if len(chunks) >5:
            print(f"\n... and {len(chunks) - 5} more chunks")
    
    return chunks

def create_vector_store(chunks, persist_directory= "db/chrom_db"):
    print("creating embeddings and storing in chromaDB")
    embedding_models=OllamaEmbeddings(model="nomic-embed-text")
    print("--- Create vector store ---")
    vectorstore=Chroma.from_documents(
        documents=chunks,
        embedding=embedding_models,
        persist_directory=persist_directory,
        collection_metadata={"hnsw:space": "cosine"}
    )
    #hnsw -> Hierarchical Navigable Small World (quickly search through millions of vector)

    print("Finished Creating vector")
    print(f"Vector store created and stored to {persist_directory}")
    return vectorstore

def main():
    print("Main function")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    docs_path = os.path.join(base_dir, "docs")
    documents=load_documents(docs_path="docs")
    chunks=split_docs(documents)
    vectorstore=create_vector_store(chunks)

if __name__=="__main__":
    main()