import os

from langchain_openai import ChatOpenAI

import langchain

from dotenv import load_dotenv

load_dotenv()

langchain.verbose = False
langchain.debug = False
langchain.llm_cache = False

llm = ChatOpenAI()

llm.invoke("Hello, world!")