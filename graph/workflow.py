from langgraph.graph import StateGraph
from graph.state import CustomerState
from agents.classifier import classify_intent
from agents.sales import sales_agent
from agents.technical import technical_agent
from agents.billing import billing_agent
from agents.account import account_agent
from agents.supervisor import supervisor_agent
from human.approval import approval_node
from agents.memory_agent import memory_agent
from memory.save_memory import save_memory
def router(state):
    return state["intent"]
builder = StateGraph(CustomerState)
builder.add_node("Classifier", classify_intent)
builder.add_node("Sales", sales_agent)
builder.add_node("Technical", technical_agent)
builder.add_node("Billing", billing_agent)
builder.add_node("Account", account_agent)
builder.add_node("Approval", approval_node)
builder.add_node("Supervisor", supervisor_agent)
builder.add_node(
    "Memory",
    memory_agent
)
builder.add_node(
    "SaveMemory",
    save_memory
)
builder.set_entry_point("Classifier")
builder.add_conditional_edges(
    "Classifier",
    router,
    {
        "Sales": "Sales",
        "Technical": "Technical",
        "Billing": "Billing",
        "Account": "Account",
        "Memory":"Memory"
    }
)
builder.add_edge("Sales", "Approval")
builder.add_edge("Technical", "Approval")
builder.add_edge("Billing", "Approval")
builder.add_edge("Account", "Approval")
builder.add_edge("Memory", "Supervisor")
builder.add_edge("Approval", "Supervisor")
builder.add_edge("Supervisor", "SaveMemory")
builder.set_finish_point("SaveMemory")
graph = builder.compile()