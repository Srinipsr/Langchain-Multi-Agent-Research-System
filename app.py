import os
import certifi
import requests
from dotenv import load_dotenv

from langchain_groq import ChatGroq


GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    api_key=GROQ_API_KEY
)
