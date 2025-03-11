import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain.memory import ChatMessageHistory

history = ChatMessageHistory()



if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = "AIzaSyCtmZnaP9_StbMtnW0gUpmOy57_OY0QNh4"


#SYSTEM PROMPT
history.add_message(SystemMessage(content="Solve the following math problems"))

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

