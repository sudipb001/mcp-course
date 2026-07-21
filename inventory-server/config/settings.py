import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Central place for every configurable value in the app."""

    DATABASE_NAME: str = os.getenv("DATABASE_NAME", "inventory.db")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    SERVER_NAME: str = os.getenv("SERVER_NAME", "Inventory MCP Server")
    API_KEY: str = os.getenv("API_KEY", "")


settings = Settings()
