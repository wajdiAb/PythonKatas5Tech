import unittest
from katas.api_response_handler import extract_user_data

class TestApiResponseHandler(unittest.TestCase):
    def test_extract_user_data_complete(self):
        api_response = '''
        {
          "users": [
            {
              "id": "1",
              "name": "Alice",
              "email": "alice@example.com",
              "company": {"name": "Alpha Inc"},
              "address": {"city": "Wonderland"}
            }
          ]
        }
        '''
        expected = [{
            "id": "1",
            "name": "Alice",
            "email": "alice@example.com",
            "company_name": "Alpha Inc",
            "city": "Wonderland"
        }]
        self.assertEqual(extract_user_data(api_response), expected)

    def test_extract_user_data_missing_fields(self):
        api_response = '''
        {
          "users": [
            {
              "id": null,
              "name": null,
              "email": null,
              "company": null,
              "address": null
            }
          ]
        }
        '''
        expected = [{
            "id": "Unknown",
            "name": "Unknown",
            "email": "Unknown",
            "company_name": "Unknown",
            "city": "Unknown"
        }]
        self.assertEqual(extract_user_data(api_response), expected)

    def test_extract_user_data_partial_fields(self):
        api_response = '''
        {
          "users": [
            {
              "id": "2",
              "name": "Bob",
              "email": "bob@example.com",
              "company": {"name": null},
              "address": {"city": null}
            }
          ]
        }
        '''
        expected = [{
            "id": "2",
            "name": "Bob",
            "email": "bob@example.com",
            "company_name": "Unknown",
            "city": "Unknown"
        }]
        self.assertEqual(extract_user_data(api_response), expected)

    def test_extract_user_data_empty_users(self):
        api_response = '{"users": []}'
        expected = []
        self.assertEqual(extract_user_data(api_response), expected)

    def test_extract_user_data_invalid_json(self):
        api_response = 'invalid json'
        with self.assertRaises(ValueError):
            extract_user_data(api_response)

if __name__ == '__main__':
    unittest.main()