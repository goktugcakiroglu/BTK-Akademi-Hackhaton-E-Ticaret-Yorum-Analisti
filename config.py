import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("HATA: .env dosyasında GOOGLE_API_KEY bulunamadı! Lütfen dosya içeriğini kontrol et.")

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)