import unittest
from service_client.client import YourServiceClient
from dotenv import load_dotenv
import os


class TestYourServiceClient(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        base_url = "https://api.hunter.io/v2"
        api_key = os.getenv("API_KEY")
        self.client = YourServiceClient(base_url, api_key)

    def test_verify_email(self):
        email_to_verify = "test@example.com"
        result = self.client.verify_email(email_to_verify)
        self.assertIsNotNone(result)
        self.assertIn("status", result)
        self.assertIn("result", result)


if __name__ == "__main__":
    unittest.main()
