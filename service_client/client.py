import requests
from typing import Any, Dict


class YourServiceClient:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key

    def _make_request(self, method: str, endpoint: str, data: Dict[str, Any] = None):
        url = f"{self.base_url}/{endpoint}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.request(method, url, json=data, headers=headers)
        return response.json()

    def verify_email(self, email: str):
        endpoint = "email-verifier"
        data = {"email": email}
        return self._make_request("GET", endpoint, data)
