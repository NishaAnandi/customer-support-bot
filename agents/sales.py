from rag.retriever import retrieve_context
from llm.groq_llm import llm
from langchain_core.messages import HumanMessage
def sales_agent(state):
    query = state["query"]
    context = retrieve_context(query)
    state["retrieved_context"] = context
    prompt = f"""
You are a Sales Support Executive.
Answer ONLY using the provided context.
Context:
{context}
Customer Question:
{query}
"""
    response = llm.invoke([HumanMessage(content=prompt)])
    state["department_response"] = response.content
    return state