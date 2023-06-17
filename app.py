from langchain.llms import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
llm = OpenAI(temperature=0.9)

res = llm.predict("What would be a good company name for a company that makes colorful socks?")
# >> Feetful of Fun
print(res)