from mcp.server.fastmcp import FastMCP

from services.customer_service import CustomerService
from utils.logger import get_logger
from config.settings import settings

logger = get_logger(__name__)

mcp = FastMCP(settings.SERVER_NAME)
service = CustomerService()


@mcp.tool()
def get_customer(customer_id: int) -> dict:
    """Retrieve a customer's information by their ID."""
    try:
        return service.get_customer(customer_id)
    except ValueError as e:
        logger.error(f"get_customer failed: {e}")
        return {"error": str(e)}


@mcp.tool()
def create_customer(customer_id: int, name: str, city: str) -> dict:
    """Create a new customer record."""
    try:
        return service.create_customer(customer_id, name, city)
    except ValueError as e:
        logger.error(f"create_customer failed: {e}")
        return {"error": str(e)}


if __name__ == "__main__":
    logger.info(
        f"Starting {service.__class__.__name__.replace('Service', '')} MCP server"
    )
    mcp.run()
