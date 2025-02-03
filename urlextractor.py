from langchain_community.document_loaders import UnstructuredURLLoader

# Define URLs to scrape
urls = ["https://searchneu.com/NEU/202560/search/1100"]

# Load web content
loader = UnstructuredURLLoader(urls=urls)
docs = loader.load()

# Print extracted content

print(docs)

for doc in docs:
    print(doc.page_content)
