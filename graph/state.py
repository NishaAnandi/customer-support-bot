from typing import TypedDict
class CustomerState(TypedDict):
    customer_name: str
    query: str
    intent: str
    retrieved_context: str
    department_response: str
    requires_approval: bool
    approval_status: str
    final_response: str