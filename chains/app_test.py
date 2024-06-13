import os
import json


#LLM宣言
from langchain.chains.llm import LLMChain
from langchain_openai import ChatOpenAI
from langchain.callbacks.base import BaseCallbackHandler
from langchain.prompts import PromptTemplate

llm = ChatOpenAI(
    model_name="gpt-3.5-turbo-0125", # `https://openai.com/api/pricing/`から取得
    temperature=0.7, # 0～2の数字、ランダム生成の可能性
    verbose=True
)


#Prompt作成
prompt_template = """
你是AI助手，回答用户的问题，生成文字数最大50字

{question} 
"""  
prompt_qa = PromptTemplate(
        template=prompt_template,
        input_variables=["question"]
)

chain = LLMChain(llm=llm, prompt=prompt_qa, verbose=True)

# # LLM送信
# res = chain.invoke({"question": "あなたは誰？"})
# print(res['text'])

# 控制台交互
def continuous_conversation():
    print("AI助手准备就绪。输入'退出'以结束对话。")
    while True:
        user_input = input("你: ")
        if user_input.lower() in ["退出", "exit", "quit"]:
            print("对话结束。")
            break
        # LLM送信
        response = chain.invoke({"question": user_input})
        print(f"AI助手: {response['text']}")

# Start the conversation
if __name__ == "__main__":
    continuous_conversation()
