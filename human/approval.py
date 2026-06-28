HIGH_RISK_INTENTS = [
    "refund",
    "cancel",
    "cancellation",
    "account closure",
    "close my account",
    "compensation",
    "escalate",
    "management"
]


def approval_node(state):
    """
    Simulates a human approval step for high-risk requests.
    """

    if not state["requires_approval"]:
        state["approval_status"] = "Approved"
        return state

    print("\n" + "=" * 60)
    print(" HUMAN SUPERVISOR APPROVAL REQUIRED")
    print("=" * 60)

    print(f"\nCustomer Query:\n{state['query']}\n")

    print("AI Draft Response:\n")
    print(state["department_response"])

    while True:
        decision = input("\nApprove this response? (yes/no): ").strip().lower()

        if decision in ["yes", "y"]:
            state["approval_status"] = "Approved"
            break

        elif decision in ["no", "n"]:
            state["approval_status"] = "Rejected"

            state["department_response"] = (
                "Your request has been forwarded to a senior support executive "
                "for manual review. You will receive an update shortly."
            )

            break

        else:
            print("Please enter yes or no.")

    return state