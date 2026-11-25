from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
data = PyPDFLoader("Document loaders/GRU.pdf")
docs = data.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=10)
splits = splitter.split_documents(docs)
print(len(splits))
print(splits[0].page_content)
