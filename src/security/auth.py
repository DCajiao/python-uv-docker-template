import os
from flask import request, abort

from utils.logger import get_logger
from security.credentials_manager import get_credentials

# Configure logger
logger = get_logger(__name__)


def require_api_key(func):
    def wrapper(*args, **kwargs):
        if request.method == 'OPTIONS':
            # Allow preflight requests without API Key validation
            return func(*args, **kwargs)

        client_key = request.headers.get("x-api-key")
        server_key = get_credentials().get("API_KEY")
        if not client_key or not server_key:
            abort(401, description="Unauthorized: API Key is required")

        if client_key != server_key:
            logger.error("Unauthorized access attempt with invalid API Key")
            abort(401, description="Unauthorized: Invalid API Key")
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__  # for Flask to recognize the function name
    return wrapper