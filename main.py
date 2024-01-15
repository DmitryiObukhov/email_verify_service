"""Main module for email verification script."""

import os

from dotenv import load_dotenv

from email_verification_service.email_verification_service import (
    EmailVerificationClient,
    EmailVerificationResultManager,
    EmailVerificationService,
)
from service_client.client import YourServiceClient
from domain_search.domain_search import HunterIOClient

load_dotenv()


def create_verification_service(api_key, base_url):
    """Create and configure the EmailVerificationService."""
    client = YourServiceClient(base_url, api_key)
    email_verification_client = EmailVerificationClient(client)
    email_verification_result_manager = EmailVerificationResultManager()
    return EmailVerificationService(
        email_verification_client, email_verification_result_manager,
    )


def main():
    """Verify email addresses using the Email Verification Service."""
    api_key = os.getenv('API_KEY')
    if not api_key:
        raise ValueError('API_KEY not found')

    base_url = 'https://api.hunter.io/v2'
    verification_service = create_verification_service(api_key, base_url)

    emails_to_verify = ['test@example.com', 'another@test.com']

    verification_results = [
        verification_service.verify_email(email) for email in emails_to_verify
    ]

    domain_results = verification_service.domain_search('example.com')
    # flake8: noqa
    print('Domain search results:', domain_results)
    print('Verification results:', verification_results)


if __name__ == '__main__':
    main()
