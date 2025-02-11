from langchain_community.document_loaders import UnstructuredURLLoader

# Define URLs to scrape
urls = ["https://service.northeastern.edu/ogs?id=kb_article_view&sys_kb_id=a6cf7f52c38b5614876b72977d01318f"]

# Load web content
loader = UnstructuredURLLoader(urls=urls)
docs = loader.load()

# Print extracted content

print(docs)

for doc in docs:
    print(doc.page_content)
