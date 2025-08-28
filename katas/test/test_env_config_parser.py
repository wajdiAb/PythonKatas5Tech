import unittest
from katas.env_config_parser import parse_env_config

class TestEnvConfigParser(unittest.TestCase):
    def test_basic_parsing(self):
        env = """
        DATABASE_URL=postgres://localhost:5432/mydb
        DEBUG=true
        PORT=8080
        APP_NAME="My Application"
        MAX_CONNECTIONS=100
        """
        expected = {
            "DATABASE_URL": "postgres://localhost:5432/mydb",
            "DEBUG": True,
            "PORT": 8080,
            "APP_NAME": "My Application",
            "MAX_CONNECTIONS": 100
        }
        self.assertEqual(parse_env_config(env), expected)

    def test_ignore_comments_and_empty_lines(self):
        env = """
        # This is a comment
        KEY1=value1

        # Another comment
        KEY2=42
        """
        expected = {
            "KEY1": "value1",
            "KEY2": 42
        }
        self.assertEqual(parse_env_config(env), expected)

    def test_boolean_and_quotes(self):
        env = '''
        ENABLE_FEATURE="true"
        DISABLE_FEATURE='false'
        NAME="Test App"
        '''
        expected = {
            "ENABLE_FEATURE": True,
            "DISABLE_FEATURE": False,
            "NAME": "Test App"
        }
        self.assertEqual(parse_env_config(env), expected)

    def test_none_returned_for_empty(self):
        env = """
        # Only comments and empty lines

        # Another comment
        """
        self.assertIsNone(parse_env_config(env))

if __name__ == '__main__':
    unittest.main()