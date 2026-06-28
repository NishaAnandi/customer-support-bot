from rag.retriever import retrieve_context
from llm.groq_llm import llm
from langchain_core.messages import HumanMessage
HIGH_RISK = [
    "refund",
    "cancel",
    "cancellation",
    "compensation"
]
def billing_agent(state):
    query = state["query"]
    context = retrieve_context(query)
    state["retrieved_context"] = context
    if any(word in query.lower() for word in HIGH_RISK):
        state["requires_approval"] = True
    else:
        state["requires_approval"] = False
    prompt = f"""
You are a Billing Support Executive.
Use ONLY the following company information.
Context:
{context}
Customer Query:
{query}
"""
    response = llm.invoke([HumanMessage(content=prompt)])
    state["department_response"] = response.content
    return state