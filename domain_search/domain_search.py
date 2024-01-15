"""Module to interact with the Hunter.io API for email verification and domain search."""

import requests

class HunterIOClient(object):
    """Client for interacting with the Hunter.io API."""

    def __init__(self, api_key):
        """Initialize the Hunter.io client with the provided API key."""
        self.api_key = api_key
        self.base_url = 'https://api.hunter.io/v2'

    def verify_email(self, email):
        """Verify the given email address using the Hunter.io API."""
        endpoint = f'{self.base_url}/email-verifier'
        # flake8: noqa
        params = {'email': email, 'api_key': self.api_key}
        response = requests.get(endpoint, params=params)
        data = response.json()
        return data

    def domain_search(self, domain):
        """Search for information related to the given domain using the Hunter.io API."""
        endpoint = f'{self.base_url}/domain-search'
        # flake8: noqa
        params = {'domain': domain, 'api_key': self.api_key}
        response = requests.get(endpoint, params=params)
        data = response.json()
        return data
