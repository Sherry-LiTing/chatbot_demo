from langchain_openai import ChatOpenAI

import os
from dotenv import load_dotenv
load_dotenv()

def create_llm(callback):
    #LLM宣言
    llm = ChatOpenAI(
        model=os.environ["OPENAI_API_MODEL"],
        temperature=os.environ["OPENAI_API_TEMPERATURE"],
        callbacks=[],
        verbose=True
    )
    
    if callback is not None:
        llm.callbacks.append(callback)
        
    return llm
