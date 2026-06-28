from llm.groq_llm import llm
from langchain_core.messages import HumanMessage
def supervisor_agent(state):
    """
    Final quality check before responding to the customer.
    """
    prompt = f"""
You are the Senior Customer Support Supervisor at ABC Technologies.
Review the AI-generated response.
Rules:
- Be professional.
- Be polite.
- Keep it concise.
- Do NOT invent facts.
- Do NOT add signatures.
- Do NOT add placeholders.
- Use only the provided information.
Customer Query:
{state['query']}
Draft Response:
{state['department_response']}
Return only the improved response.
"""
    response = llm.invoke([HumanMessage(content=prompt)])
    state["final_response"] = response.content
    return state