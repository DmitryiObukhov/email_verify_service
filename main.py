import os
from dotenv import load_dotenv
from service_client.client import YourServiceClient
from email_verification_service.email_verification_service import EmailVerificationService

load_dotenv()


def main():
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY not founded")

    base_url = "https://api.hunter.io/v2"
    client = YourServiceClient(base_url, api_key)
    verification_service = EmailVerificationService(client)
    emails_to_verify = ["test@example.com", "another@test.com"]

    for email in emails_to_verify:
        verification_service.verify_email(email)

    results = verification_service.get_results()
    print("Verification results:", results)


if __name__ == "__main__":
    main()
