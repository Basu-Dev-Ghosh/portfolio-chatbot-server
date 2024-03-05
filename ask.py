import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader,PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_openai import OpenAI
documents = []
def ask(question: str):
    load_dotenv()
    for file in os.listdir('data'):
        if file.endswith('.pdf'):
            pdf_path = './data/' + file
            loader = PyPDFLoader(pdf_path)
            documents.extend(loader.load())
        elif file.endswith('.json'):
            json_path = './data/' + file
            loader = TextLoader(json_path)
            documents.extend(loader.load())
        elif file.endswith('.txt'):
            text_path = './data/' + file
            loader = TextLoader(text_path)
            documents.extend(loader.load())
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=10)
    chunked_documents = text_splitter.split_documents(documents)
    vectordb = Chroma.from_documents(chunked_documents,embedding=OpenAIEmbeddings(),persist_directory='./data')
    vectordb.persist()
    template = """Answer the question in your own words from the context given to you.

    Context: {context}

    If questions are asked where there is no relevant context available, please answer that you don't know.
    Remember, you are Basudev Ghosh.
    Answer in the first person view and try to be funny and creative.
    Human: {question}
    Assistant:"""
    prompt = PromptTemplate(input_variables=["context",  "question"], template=template)
    qa_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(temperature=0.6),
    retriever=vectordb.as_retriever(search_kwargs={'k': 3}),
    return_source_documents=True,
    chain_type_kwargs={'prompt': prompt}
    )
    result = qa_chain.invoke({'query': question})
    return result['result']

    