import pytest
from unittest.mock import MagicMock

from services.customer_service import CustomerService
from models.customer import Customer


def test_get_customer_success():
    mock_repo = MagicMock()
    mock_repo.get_by_id.return_value = Customer(1, "Aiden", "Chicago")

    service = CustomerService(repository=mock_repo)
    result = service.get_customer(1)

    assert result == {"customer_id": 1, "name": "Aiden", "city": "Chicago"}


def test_get_customer_not_found():
    mock_repo = MagicMock()
    mock_repo.get_by_id.return_value = None
    service = CustomerService(repository=mock_repo)

    with pytest.raises(ValueError):
        service.get_customer(1)


def test_get_customer_invalid_id():
    service = CustomerService(repository=MagicMock())

    with pytest.raises(ValueError):
        service.get_customer(-5)


def test_create_customer_success():
    mock_repo = MagicMock()
    service = CustomerService(repository=mock_repo)

    result = service.create_customer(2, "Priya", "Seattle")

    assert result == {"customer_id": 2, "name": "Priya", "city": "Seattle"}
    mock_repo.add.assert_called_once()


def test_create_customer_empty_name_raises():
    service = CustomerService(repository=MagicMock())

    with pytest.raises(ValueError):
        service.create_customer(3, "   ", "Denver")
