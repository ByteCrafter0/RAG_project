from langchain_arxiv import ArxivRetriever

retriever = ArxivRet
riever(
    k=3,
    full_text=False
)

docs = retriever.invoke("large language models")

for doc in docs:
    print("Title:", doc.metadata.get("title"))
    print("Content:", doc.page_content)
    print("-" * 50)