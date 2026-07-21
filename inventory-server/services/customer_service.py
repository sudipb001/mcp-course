from typing import Optional

from repositories.customer_repository import CustomerRepository
from models.customer import Customer
from utils.validators import validate_customer_id, validate_name
from utils.logger import get_logger

logger = get_logger(__name__)


class CustomerService:
    """Business rules for working with customers."""

    def __init__(self, repository: Optional[CustomerRepository] = None):
        # Accepting an optional repository lets tests inject a mock
        self.repository = repository or CustomerRepository()

    def get_customer(self, customer_id: int) -> dict:
        validate_customer_id(customer_id)

        logger.info(f"Looking up customer {customer_id}")
        customer = self.repository.get_by_id(customer_id)

        if customer is None:
            logger.warning(f"Customer {customer_id} was not found")
            raise ValueError(f"Customer {customer_id} was not found.")

        return customer.to_dict()

    def create_customer(self, customer_id: int, name: str, city: str) -> dict:
        validate_customer_id(customer_id)
        validate_name(name)

        customer = Customer(customer_id, name.strip(), city.strip())
        self.repository.add(customer)
        logger.info(f"Created customer {customer_id}")

        return customer.to_dict()
