import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

class AzureConfig:
    """Configuration class for connecting to Azure Blob Storage."""

    def __init__(self):
        load_dotenv()
        self.connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
        self.container_name = os.getenv("AZURE_CONTAINER_NAME")
        self._blob_service_client = None
        self._container_client = None

    @property
    def blob_service_client(self):
        """Initialize and return the Azure BlobServiceClient."""
        if not self._blob_service_client:
            self._blob_service_client = BlobServiceClient.from_connection_string(
                self.connection_string
            )
        return self._blob_service_client

    @property
    def container_client(self):
        """Return the client for an existing container."""
        if not self._container_client:
            self._container_client = self.blob_service_client.get_container_client(
                self.container_name
            )
        return self._container_client


# створюємо глобальний об’єкт для підключення
azure_config = AzureConfig()
