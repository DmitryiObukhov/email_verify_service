"""Module providing YourServiceClient for interacting with an external service."""

from typing import Any, Dict
from domain_search.domain_search import HunterIOClient
import requests


class YourServiceClient(object):
    """Client for interacting with an external service."""

    def __init__(self, base_url: str, api_key: str):
        """
        Initialize YourServiceClient.

        :param base_url: The base URL of the external service.
        :param api_key: The API key for authentication.
        """
        self.base_url = base_url
        self.api_key = api_key

    def verify_email(self, email: str):
        """
        Verify the given email using the external service.

        :param email: The email address to be verified.
        :return: JSON response from the external service.
        """
        endpoint = 'email-verifier'
        request_data = {'email': email}
        return self._make_request('GET', endpoint, request_data)
    
    def domain_search(self, domain: str):
        """
        Search for information related to the given domain using HunterIOClient.

        :param domain: The domain to search.
        :return: JSON response from HunterIOClient.
        """
        return self.hunter_io_client.domain_search(domain)

    def _make_request(self, method: str, endpoint: str, request_data: Dict[str, Any] = None):
        """
        Make an HTTP request to the external service.

        :param method: The HTTP method (GET, POST, etc.).
        :param endpoint: The API endpoint.
        :param data: Optional data to be sent with the request.
        :return: JSON response from the external service.
        """
        # flake8: noqa
        url = f'{self.base_url}/{endpoint}'
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.request(method, url, json=request_data, headers=headers)
        return response.json()
