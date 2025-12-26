import os
from dotenv import load_dotenv


class CredentialsManager:
    @staticmethod
    def get_credentials():
        """
        Loads environment variables from a .env file and returns
        a dictionary.
        """
        load_dotenv()  # Load environment variables from .env file

        credentials = {
            "API_KEY": os.getenv("API_KEY"),
            "PORT": os.getenv("PORT"),
            "LOGGER_LEVEL": os.getenv("LOGGER_LEVEL", "INFO")
        }

        # Basic validation
        if not all(credentials.values()):
            raise ValueError(
                "Missing required environment variables. Please check your .env file.")

        return credentials
