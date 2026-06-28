from rag.retriever import retrieve_context
from llm.groq_llm import llm
from langchain_core.messages import HumanMessage
def account_agent(state):
    query = state["query"]
    context = retrieve_context(query)
    state["retrieved_context"] = context
    prompt = f"""
You are an Account Support Executive.
Use only the provided documentation.
Documentation:
{context}
Customer Query:
{query}
"""
    response = llm.invoke([HumanMessage(content=prompt)])
    state["department_response"] = response.content
    return state