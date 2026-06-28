from rag.retriever import retrieve_context
from llm.groq_llm import llm
from langchain_core.messages import HumanMessage
def technical_agent(state):
    query = state["query"]
    context = retrieve_context(query)
    state["retrieved_context"] = context
    prompt = f"""
You are a Technical Support Engineer.
Answer ONLY from the provided technical documentation.
Documentation:
{context}
Customer Query:
{query}
"""
    response = llm.invoke([HumanMessage(content=prompt)])
    state["department_response"] = response.content
    return state