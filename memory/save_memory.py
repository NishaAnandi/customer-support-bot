from memory.sqlite_memory import SQLiteMemory

memory = SQLiteMemory()


def save_memory(state):
    # Don't store memory recall queries
    if state["intent"] == "Memory":
        return state

    memory.save(
        state["customer_name"],
        state["query"],
        state["final_response"]
    )

    return state