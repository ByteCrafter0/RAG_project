from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from langchain_core.documents import Document
load_dotenv()

docs = [
    Document(page_content="This is a test document.", metadata={"source": "test1.txt"}),
    Document(page_content="This is another test document.", metadata={"source": "test2.txt"}),

]

embeddings_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embeddings_model,
    persist_directory="chroma_db",
)
result=vectorstore.similarity_search("test document", k=2)
for i in result:
    print(i.page_content)
retriver = vectorstore.as_retriever()
docs = retriver.invoke("test document")
for i in docs:
    print(i.page_content)