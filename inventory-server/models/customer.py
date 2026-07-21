class Customer:
    """Represents a single customer record."""

    def __init__(self, customer_id: int, name: str, city: str):
        self.customer_id = customer_id
        self.name = name
        self.city = city

    def to_dict(self) -> dict:
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "city": self.city,
        }
