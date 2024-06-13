### Api Key
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

### パッケージ
```bash
pip install langchain_community
pip install langchain
pip install chromadb
pip install sentence_transformers
pip install langchain_openai
```

### 準備
```python
import os

os.environ['OPENAI_API_KEY'] = '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'
```

### LLM宣言
```python
from langchain.chains.llm import LLMChain
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model_name="gpt-3.5-turbo-0125", # `https://openai.com/api/pricing/`から取得
    temperature=0.7, # 0～2の数字、ランダム生成の可能性
    verbose=True
)
if callback is not None:
    llm.callbacks.append(callback)
return llm
```

### Prompt作成

```python
from langchain.prompts import PromptTemplate

prompt_template = """
你是AI助手，回答用户的问题，生成文字数最大50字

{question} 
"""  
prompt_qa = PromptTemplate(
        template=prompt_template,
        input_variables=["question"]
)

chain = LLMChain(llm=llm, prompt=prompt_qa, verbose=True)
```


### LLM送信
```python

res = chain..invoke({"question": "あなたは誰？"})
print(res['text'])
```