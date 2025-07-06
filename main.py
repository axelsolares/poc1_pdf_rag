import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.docstore.document import Document
from chains.custom_chains import get_financial_chain

from utils.load_docs import load_pdf, load_csv

from dotenv import load_dotenv

load_dotenv()

pdf_text = load_pdf("docs/financial_report.pdf")
csv_text = load_csv("docs/financial_data.csv")
all_text = pdf_text + "\n" 
documents = [Document(page_content=all_text)]
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
vector_store = FAISS.from_documents(docs, embeddings)
retriever = vector_store.as_retriever(search_kwargs={"k": 4})
chain = get_financial_chain(retriever)
query = "Please summarize the main financial results and highlight any key insights or concerns"
response = chain.invoke(query)
print("📊 Result:")
print(response)
