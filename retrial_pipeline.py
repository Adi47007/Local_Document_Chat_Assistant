import os
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
persistent_directory = os.path.join(BASE_DIR, "db", "chrom_db")

embedding_model=OllamaEmbeddings(model="nomic-embed-text")

model=ChatOllama(model="gemma3:4b")

db=Chroma(
    persist_directory=persistent_directory,
    embedding_function=embedding_model,
    collection_metadata={"hnsw:space":"cosine"}
)

chathistory=[]

def ask_question(user_question):
    print(f"\n--You asked: {user_question} --")
    if chathistory:
        messages=[
            SystemMessage(content="Given the chat history rewrite the new question to be standalone and searchable. Just return the question.") ] + chathistory + [
            HumanMessage(content=f"New question= {user_question}")
        ]
        result=model.invoke(messages)
        search_question=result.content.strip()
        print(f"Searching for: {search_question}")

    else:
        search_question=user_question

    retriever=db.as_retriever(search_kwargs={"k":3}) #retrive top 3 
    relevant_docs=retriever.invoke(search_question)

    print(f"Found {len(relevant_docs)} relevant docs")
    for i, doc in enumerate(relevant_docs, 1):
        lines=doc.page_content.split('\n')[:2]
        preview='\n'.join(lines)
        print(f" Doc {i}: {preview}...")
    
    combined_input = f"""
    You are a question-answering assistant.
    Use ONLY the information in the retrieved documents.
    
    Question:
    {user_question}
    
    Retrieved Documents:
    {chr(10).join(doc.page_content for doc in relevant_docs)}
    
    Answer:
    """
    messages=[
    SystemMessage(content="You are a helpful assistant that answers the answers the question based on the provided documents and conversation") ] + chathistory + [
    HumanMessage(content=combined_input)
    ]

    result=model.invoke(messages)
    answer= result.content
    chathistory.append(HumanMessage(content=user_question))
    chathistory.append(AIMessage(content=answer))
    
    print(result)
    print("----------------")
    print(result.content)

    return answer

def start_chat():
    print("Ask me question! Type quit to exit")

    while True:
        question=input("\n Your question: ")
        if question.lower()=='quit':
            print("Goodbye")
            break
        ask_question(question)

if __name__=="__main__":
    start_chat()

