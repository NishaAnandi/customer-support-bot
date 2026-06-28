from llm.groq_llm import llm
from langchain_core.messages import HumanMessage
VALID_INTENTS = [
    "Sales",
    "Technical",
    "Billing",
    "Account",
    "Memory"
]
def classify_intent(state):
    query = state["query"]
    prompt = f"""
You are an intent classifier.
Return ONLY one of these words:
Sales
Technical
Billing
Account
Memory
Rules:
If the customer asks:
- previous issue
- previous conversation
- earlier request
- conversation history
- remember me
Return:
Memory
Customer Query:
{query}
"""
    response = llm.invoke(
        [HumanMessage(content=prompt)]
    )
    intent = response.content.strip()
    if intent not in VALID_INTENTS:
        intent = "Technical"
    state["intent"] = intent
    return state