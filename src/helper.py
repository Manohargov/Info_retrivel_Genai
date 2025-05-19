import os
from pyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import GooglePalmEmbeddings
from langchain.llms import googlepalm
from langchain.vectorstrores import FAISS
from langchain.chains import concersationalRetrivelChain
form langchain.memory import conversationVufferMemory
form dotenv import load_dotenv


load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY


def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text+=page.extract_text()
    return text

def Get_text_chunks(text):
    text_splitter= recursiveCharecterTextSplitter( chunk_size=1000,chunks_overlap=20)
    chunks =text_splitter.split_text(text)
    return chunks

def get_vector_store(chunks):
    embeddings = GooglePalmEmbeddings()
    vector_store = FAISS.from_texts(chunks,embedding=embeddings)
    return vector_store

def get_conversational_chain(vector_store):
    llm = GooglePalm()
    memory = conversationalbufferMemory(memory_key="chat_history",return_messages=True)
    conversation_chain = conversationalRetrivelChain.from_llm(llm= llm,retriver=vector_store,memory=memory)
    return conversation_chain


