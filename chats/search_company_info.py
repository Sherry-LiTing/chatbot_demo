import os
from uuid import UUID
import chainlit as cl
from chains.agents import create_search_companyinfo_agent
from langchain_core.callbacks import AsyncCallbackHandler
from langchain.agents import AgentExecutor
from langchain_core.messages import HumanMessage, AIMessage
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Sequence, TypeVar, Union

from pprint import pprint

class MyCustomHandler(AsyncCallbackHandler):
    msg: cl.Message

    def set_message(self, msg):
        self.msg = msg

    async def on_llm_new_token(self, token: str, **kwargs) -> None:
        await self.msg.stream_token(token)

    async def on_llm_start(
        self,
        serialized: Dict[str, Any],
        prompts: List[str],
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> None:
        pprint(prompts)


@cl.on_chat_start
async def on_chat_start():
    callback = MyCustomHandler()
    agent = create_search_companyinfo_agent(callback)
    cl.user_session.set("callback", callback)
    cl.user_session.set("agent", agent)
    cl.user_session.set("messages", [])

@cl.on_message
async def on_message(message: cl.Message):
    callback: MyCustomHandler = cl.user_session.get("callback")
    agent: AgentExecutor = cl.user_session.get("agent")
    messages: List = cl.user_session.get("messages")
    msg = cl.Message(content="")
    await msg.send()
    callback.set_message(msg)
    result = await agent.ainvoke({"input": message.content})
    pprint(result)
    messages.append(HumanMessage(content=message.content))
    messages.append(AIMessage(content=result['output']))
    await msg.update()


if __name__ == "__main__":
    from chainlit.cli import run_chainlit

    run_chainlit(__file__)
