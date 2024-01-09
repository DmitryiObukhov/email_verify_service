from typing import List, Dict, Any


class EmailVerificationService:
    def __init__(self, client: Any) -> None:
        self.client = client
        self.results: List[Dict[str, Any]] = []

    def verify_email(self, email: str) -> None:
        verification_result: Dict[str, Any] = self.client.verify_email(email)
        self.results.append(verification_result)

    def get_results(self) -> List[Dict[str, Any]]:
        return self.results

    def create_result(self, result: Dict[str, Any]) -> None:
        self.results.append(result)

    def read_results(self) -> List[Dict[str, Any]]:
        return self.results

    def update_result(self, index: int, new_result: Dict[str, Any]) -> None:
        if 0 <= index < len(self.results):
            self.results[index] = new_result

    def delete_result(self, index: int) -> None:
        if 0 <= index < len(self.results):
            del self.results[index]
