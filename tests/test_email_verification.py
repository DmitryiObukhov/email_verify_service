"""Unit tests for the EmailVerificationService module."""

import unittest
from unittest.mock import MagicMock

from email_verification_service.email_verification_service import EmailVerificationService


class TestEmailVerificationService(unittest.TestCase):
    """Test case for the EmailVerificationService module."""

    def test_verify_email_adds_result(self):
        """Test if verify_email adds a result to the service."""
        mock_client = MagicMock()
        service = EmailVerificationService(mock_client)
        email = 'test@example.com'
        service.verify_email(email)
        self.assertEqual(len(service.get_results()), 1)

    def test_update_result_updates_result(self):
        """Test if update_result updates a result in the service."""
        mock_client = MagicMock()
        service = EmailVerificationService(mock_client)
        email = 'test@example.com'
        service.verify_email(email)
        new_result = {'status': 'valid'}
        service.update_result(0, new_result)
        self.assertEqual(service.get_results()[0], new_result)
