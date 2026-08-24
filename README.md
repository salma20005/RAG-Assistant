# RAG Project

##  How to get in


### Clone repo
```git clone [repo-name]```
### create .env file
``` cp .env.example .env```
- GEMINI_API_KEY = Your API Key Here

## Thoughts
ChatGPT --> `chatbot` , [AI]-[predictions] --> RNN , LSTM / Transformer[Attention]+ [Huge language data] + [Computational power]=LLM
[GPT] [Decoder]

[GPT] --> pre-trained NN `Not alive`

+ Bring LLMS to live:
   - Fine Tuning : Re-train Model [Time] + [Money] + [Data]
   - RAG -> Retrieval --> Bring data
   -  Augmented --> [Data] + prompt
   -   Generation --> Generate Answer

## Goal
user [PDF] --> chat [PDF]
[user]pdf --> embedding [vectors] --> add in vectorDatabase
[user]query --> embedding [query] --> similarity
[Context[Query]] -- [context[vectorBase]]
(best_match[user_context]) + prompt ---> LLMS --> answer
## Structure 
app.py
modules/
  __init__.py
  pdf_utils
  embedding.py
  vectordb.py
  llm.py
prompts/
  rag_prompt.txt
.env
requirements.txt