import unittest
from service_client.client import YourServiceClient


class TestYourServiceClient(unittest.TestCase):
    def setUp(self):
        base_url = "https://api.hunter.io/v2"
        self.client = YourServiceClient(base_url)

    def test_get_some_data(self):
        result = self.client.get_some_data()
        self.assertIsNotNone(result)

    def test_post_some_data(self):
        data = {"key": "value"}
        result = self.client.post_some_data(data)
        self.assertIsNotNone(result)


if __name__ == "__main__":
    unittest.main()
