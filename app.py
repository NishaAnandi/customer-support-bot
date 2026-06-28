from graph.workflow import graph


def run():
    print("=" * 60)
    print("ABC TECHNOLOGIES CUSTOMER SUPPORT BOT")
    print("=" * 60)

    customer_name = input("\nEnter your name: ")

    while True:
        query = input("\nCustomer: ")

        if query.lower() in ["exit", "quit"]:
            print("\nThank you for using ABC Technologies Support.")
            break

        state = {
            "customer_name": customer_name,
            "query": query,
            "intent": "",
            "retrieved_context": "",
            "department_response": "",
            "requires_approval": False,
            "approval_status": "",
            "final_response": ""
        }

        result = graph.invoke(state)

        print("\nBot:\n")
        print(result["final_response"])


if __name__ == "__main__":
    run()