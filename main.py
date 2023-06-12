import os

from dotenv import load_dotenv
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
import pinecone

load_dotenv()

documents = TextLoader("./files_to_read/docker.txt").load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=20,
    length_function=len
)

texts = text_splitter.split_documents(documents)

pinecone.init(
    api_key=os.environ.get("PINECONE_API_KEY"),
    environment=os.environ.get("PINECONE_API_ENVIRONMENT"),
)

embeddings = OpenAIEmbeddings(openai_api_key=os.environ.get("OPENAI_API_KEY"))

vector_store = Pinecone.from_documents(
    texts, embeddings, index_name="chat-with-text-file"
)

qa = RetrievalQA.from_chain_type(
    llm=OpenAI(), chain_type="stuff", retriever=vector_store.as_retriever(), return_source_documents=True
)

question = "What is a docker DB? Treat me as a beginner and Give me a short answer"
result = qa({"query": question})

print(result)

