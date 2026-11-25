from langchain_community.document_loaders import WebBaseLoader
url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
Data = WebBaseLoader([url])
docs = Data.load()
print(docs[0].page_content)
