# test_datasieve.py

import unittest
from datasieve import DataSieve

class TestDataSieve(unittest.TestCase):
    
    def setUp(self):
        self.sample_text = """
        Email: test.user@example.com
        URL: https://www.example.com
        Phone: (123) 456-7890
        Card: 1234-5678-9012-3456
        Time: 2:30 PM
        HTML: <div class="content">
        Hashtag: #TestProject
        Price: $1,234.56
        """
        self.sieve = DataSieve(self.sample_text)

    def test_extract_emails(self):
        self.assertIn("test.user@example.com", self.sieve.extract_emails())

    def test_extract_urls(self):
        self.assertIn("https://www.example.com", self.sieve.extract_urls())

    def extract_phone_numbers(self):
        self.assertIn("(123) 456-7890", self.sieve.extract_phones())

    def test_extract_credit_cards(self):
        self.assertIn("1234-5678-9012-3456", self.sieve.extract_credit_cards())

    def test_extract_times(self):
        self.assertIn("2:30 PM", self.sieve.extract_time())

    def test_extract_html_tags(self):
        self.assertIn('<div class="content">', self.sieve.extract_html_tags())

    def test_extract_hashtags(self):
        self.assertIn("#TestProject", self.sieve.extract_hashtags())

    def test_extract_currency(self):
        self.assertIn("$1,234.56", self.sieve.extract_currency())

if __name__ == "__main__":
    unittest.main()
# test_datasieve.py