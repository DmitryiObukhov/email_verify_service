"""Module providing email verification functionality."""
from typing import Any, Dict, List

from domain_search.domain_search import HunterIOClient


class EmailVerificationClient(object):
    """Client for email verification."""

    def __init__(self, client: Any) -> None:
        """Initialize the EmailVerificationClient."""
        self.client = client

    def verify_email(self, email: str) -> Dict[str, Any]:
        """Verify the given email using the client."""
        return self.client.verify_email(email)

    def domain_search(self, domain: str) -> Dict[str, Any]:
        """Search for information related to the given domain using the client."""
        return self.client.domain_search(domain)


class EmailVerificationResultManager(object):
    """Manager for email verification results."""

    def __init__(self):
        """Initialize the EmailVerificationResultManager."""
        self._results: List[Dict[str, Any]] = []

    def create_result(self, result_data: Dict[str, Any]) -> None:
        """Create a new result and add it to the list."""
        self._results.append(result_data)

    def read_results(self) -> List[Dict[str, Any]]:
        """Read and return the list of results."""
        return self._results

    def update_result(self, index: int, new_result: Dict[str, Any]) -> None:
        """Update the result at the specified index."""
        if 0 <= index < len(self._results):
            self._results[index] = new_result

    def delete_result(self, index: int) -> None:
        """Delete the result at the specified index."""
        if 0 <= index < len(self._results):
            self._results.pop(index)


class EmailVerificationService(object):
    """Service for email verification."""

    def __init__(self, client: EmailVerificationClient, result_manager: EmailVerificationResultManager):
        """Initialize the EmailVerificationService."""
        self.client = client
        self.result_manager = result_manager

    def verify_email(self, email: str) -> None:
        """Verify the given email and store the result."""
        verification_result: Dict[str, Any] = self.client.verify_email(email)
        self.result_manager.create_result(verification_result)

    def domain_search(self, domain: str) -> None:
        """Search for information related to the given domain and store the result."""
        domain_result: Dict[str, Any] = self.client.domain_search(domain)
        self.result_manager.create_result(domain_result)

    def get_results(self) -> List[Dict[str, Any]]:
        """Get and return the list of verification results."""
        return self.result_manager.read_results()

    def update_result(self, index: int, new_result: Dict[str, Any]) -> None:
        """Update the result at the specified index."""
        self.result_manager.update_result(index, new_result)

    def delete_result(self, index: int) -> None:
        """Delete the result at the specified index."""
        self.result_manager.delete_result(index)
