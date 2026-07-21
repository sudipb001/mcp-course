def validate_customer_id(customer_id: int) -> None:
    """Raise ValueError if customer_id is not a positive integer."""
    if not isinstance(customer_id, int) or isinstance(customer_id, bool):
        raise ValueError("Customer ID must be an integer.")
    if customer_id <= 0:
        raise ValueError("Customer ID must be a positive number.")


def validate_name(name: str) -> None:
    """Raise ValueError if name is empty or only whitespace."""
    if not name or not name.strip():
        raise ValueError("Name cannot be empty.")
