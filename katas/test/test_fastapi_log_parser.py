import unittest
from katas.fastapi_log_parser import parse_fastapi_log

class TestFastAPILogParser(unittest.TestCase):
    def test_valid_log(self):
        log = 'INFO:     127.0.0.1:54321 - "GET /api/users HTTP/1.1" 200 OK'
        expected = {
            "client_ip": "127.0.0.1",
            "client_port": "54321",
            "http_method": "GET",
            "endpoint": "/api/users",
            "http_version": "1.1",
            "status_code": "200",
            "status_text": "OK"
        }
        self.assertEqual(parse_fastapi_log(log), expected)

    def test_another_valid_log(self):
        log = 'INFO:     192.168.1.100:45678 - "POST /api/auth/login HTTP/1.1" 401 Unauthorized'
        expected = {
            "client_ip": "192.168.1.100",
            "client_port": "45678",
            "http_method": "POST",
            "endpoint": "/api/auth/login",
            "http_version": "1.1",
            "status_code": "401",
            "status_text": "Unauthorized"
        }
        self.assertEqual(parse_fastapi_log(log), expected)

    def test_invalid_log_format(self):
        log = 'INVALID LOG LINE'
        self.assertEqual(parse_fastapi_log(log), {})

    def test_partial_log(self):
        log = 'INFO:     127.0.0.1:54321 - "GET /api/users HTTP/1.1"'
        self.assertEqual(parse_fastapi_log(log), {})

    def test_status_text_with_spaces(self):
        log = 'INFO:     203.0.113.25:12345 - "DELETE /api/orders/456 HTTP/1.1" 204 No Content'
        expected = {
            "client_ip": "203.0.113.25",
            "client_port": "12345",
            "http_method": "DELETE",
            "endpoint": "/api/orders/456",
            "http_version": "1.1",
            "status_code": "204",
            "status_text": "No Content"
        }
        self.assertEqual(parse_fastapi_log(log), expected)

if __name__ == '__main__':
    unittest.main()