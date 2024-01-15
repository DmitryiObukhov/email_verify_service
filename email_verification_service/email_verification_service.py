from typing import List, Dict, Any


class EmailVerificationClient:
    def __init__(self, client: Any) -> None:
        self.client = client

    def verify_email(self, email: str) -> Dict[str, Any]:
        return self.client.verify_email(email)


class EmailVerificationResultManager:
    def __init__(self):
        self.results: List[Dict[str, Any]] = []

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


class EmailVerificationService:
    def __init__(self, client: EmailVerificationClient, result_manager: EmailVerificationResultManager):
        self.client = client
        self.result_manager = result_manager

    def verify_email(self, email: str) -> None:
        verification_result: Dict[str, Any] = self.client.verify_email(email)
        self.result_manager.create_result(verification_result)

    def get_results(self) -> List[Dict[str, Any]]:
        return self.result_manager.read_results()

    def update_result(self, index: int, new_result: Dict[str, Any]) -> None:
        self.result_manager.update_result(index, new_result)

    def delete_result(self, index: int) -> None:
        self.result_manager.delete_result(index)
