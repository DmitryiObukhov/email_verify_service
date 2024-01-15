"""Script for email verification."""

import os

from dotenv import load_dotenv

from email_verification_service.email_verification_service import (
    EmailVerificationClient,
    EmailVerificationResultManager,
    EmailVerificationService,
)
from service_client.client import YourServiceClient

load_dotenv()


def create_verification_service(api_key, base_url):
    """Create and configure the EmailVerificationService."""
    client = YourServiceClient(base_url, api_key)
    email_verification_client = EmailVerificationClient(client)
    email_verification_result_manager = EmailVerificationResultManager()
    return EmailVerificationService(email_verification_client, email_verification_result_manager)


def main():
    """Perform email verification."""
    api_key = os.getenv('API_KEY')
    if not api_key:
        raise ValueError('API_KEY not found')

    verification_service = create_verification_service(api_key, 'https://api.hunter.io/v2')

    emails_to_verify = ['test@example.com', 'another@test.com']

    for email in emails_to_verify:
        verification_service.verify_email(email)

    verification_results = verification_service.get_results()
    # flake8: noqa
    print('Verification results:', verification_results)


if __name__ == '__main__':
    main()
