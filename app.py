from langchain.chat_models import ChatAnthropic
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

chat = ChatAnthropic()

messages = [
    HumanMessage(
        content="Translate this sentence from English to French. I love programming."
    )
]
res = chat(messages)

ans = res[0]
reply = ans.content