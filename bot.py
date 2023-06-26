from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(openai_api_key=openai_api_key)

chat = ChatOpenAI(temperature=0)
res = chat.predict_messages([HumanMessage(content="Where is the city of Harare located?")])
print(res.content)
# >> AIMessage(content="J'aime programmer.", additional_kwargs={})

