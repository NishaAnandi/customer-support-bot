from memory.sqlite_memory import SQLiteMemory
memory = SQLiteMemory()
def memory_agent(state):
    customer = state["customer_name"]
    previous = memory.get_last_issue(customer)
    state["department_response"] = (
        f"Your previous support issue was:\n\n{previous}"
    )
    return state