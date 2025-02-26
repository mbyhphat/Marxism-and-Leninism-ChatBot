from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings

def load_pdf_file(data):
    loader = DirectoryLoader(data,
                             glob="*.pdf",
                             cls=PyPDFLoader)
    documents = loader.load()
    return documents

def text_split(documents):
    splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
    text_chunks = splitter.split_documents(documents)
    return text_chunks

def load_embeddings():
    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
    return embeddings