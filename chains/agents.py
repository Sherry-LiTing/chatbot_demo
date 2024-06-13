from langchain.agents import AgentExecutor, create_openai_tools_agent

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder,HumanMessagePromptTemplate,SystemMessagePromptTemplate
from langchain.memory import ConversationBufferMemory
from common.init import create_llm

from classes.serach_companyinfo import SearchCompanyInfoTool

def create_search_companyinfo_agent(callback = None):
    llm = create_llm(callback)
    
    # templateを定義
    template = """
You are an assistant responsible for company information research and analysis.
Your tasks are as follows:
Search for relevant information about the company based on the user's requirements.
Generate a motivation statement template based on the company's information, not exceeding 100 words.
Please respond fully in accordance with the return value of the SearchCompanyInfoTool.
When the user's question is unrelated to company information, please use your knowledge to answer.
Please use Japanese to answer questions
"""
    
    # プロンプト作成
    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessagePromptTemplate.from_template(template),
            MessagesPlaceholder(variable_name="chat_history"),  # Where the memory will be stored.
            HumanMessagePromptTemplate.from_template("{input}"),  # Where the human input will injected
            MessagesPlaceholder("agent_scratchpad"),
        ]
    )
    
    # メモリ作成
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    
    # ツール定義
    tools = [
        SearchCompanyInfoTool(),
    ]
    
    # エージェント作成
    agent = create_openai_tools_agent(llm, tools, prompt)
    # エージェント実行
    agent_executor = AgentExecutor.from_agent_and_tools(
        agent=agent, tools=tools, verbose=True, memory=memory
    )
    return agent_executor






















    
    