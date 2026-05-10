from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()


llm=GoogleGenerativeAI(model='gemini-3.1-flash-lite')

result =llm.invoke("what is the capital of india")

print(result)