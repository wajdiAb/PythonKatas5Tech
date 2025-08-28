import unittest
from katas.email_validator import is_valid_email

class TestEmailValidator(unittest.TestCase):
    def test_valid_emails(self):
        self.assertTrue(is_valid_email("user@example.com"))
        self.assertTrue(is_valid_email("john.doe@domain.co.uk"))
        self.assertTrue(is_valid_email("alice+bob@sub.domain.com"))

    def test_invalid_emails(self):
        self.assertFalse(is_valid_email("userexample.com"))
        self.assertFalse(is_valid_email("user@.com"))
        self.assertFalse(is_valid_email("@example.com"))
        self.assertFalse(is_valid_email("user@com"))
        self.assertFalse(is_valid_email("user@domain..com"))

if __name__ == '__main__':
    unittest.main()