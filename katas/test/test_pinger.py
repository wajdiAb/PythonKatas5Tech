import unittest
from unittest.mock import patch, MagicMock
from katas.pinger import ping_host

# filepath: /home/wajdi/PythonKatas5Tech/katas/test/test_pinger.py

class TestPingHost(unittest.TestCase):
    @patch("subprocess.run")
    def test_ping_success(self, mock_run):
        # Simulate successful ping output
        mock_result = MagicMock()
        mock_result.stdout = (
            "PING google.com (8.8.8.8): 56 data bytes\n"
            "--- google.com ping statistics ---\n"
            "5 packets transmitted, 5 received, 0% packet loss, time 4008ms\n"
            "rtt min/avg/max/mdev = 14.123/15.456/16.789/0.123 ms\n"
        )
        mock_run.return_value = mock_result

        result = ping_host("google.com", 5)
        self.assertEqual(result['host'], "google.com")
        self.assertEqual(result['avg_response_time_ms'], 15.456)
        self.assertTrue(result['success'])

    @patch("subprocess.run")
    def test_ping_no_rtt_line(self, mock_run):
        # Simulate ping output without rtt line
        mock_result = MagicMock()
        mock_result.stdout = (
            "PING google.com (8.8.8.8): 56 data bytes\n"
            "--- google.com ping statistics ---\n"
            "5 packets transmitted, 0 received, 100% packet loss, time 4008ms\n"
        )
        mock_run.return_value = mock_result

        result = ping_host("google.com", 5)
        self.assertEqual(result['host'], "google.com")
        self.assertIsNone(result['avg_response_time_ms'])
        self.assertFalse(result['success'])

    @patch("subprocess.run")
    def test_ping_subprocess_raises(self, mock_run):
        # Simulate subprocess.run raising CalledProcessError
        mock_run.side_effect = Exception("Ping failed")

        result = ping_host("example.com", 3)
        self.assertEqual(result['host'], "example.com")
        self.assertIsNone(result['avg_response_time_ms'])
        self.assertFalse(result['success'])

    @patch("subprocess.run")
    def test_ping_different_host(self, mock_run):
        mock_result = MagicMock()
        mock_result.stdout = (
            "PING 8.8.8.8 (8.8.8.8): 56 data bytes\n"
            "--- 8.8.8.8 ping statistics ---\n"
            "3 packets transmitted, 3 received, 0% packet loss, time 3003ms\n"
            "rtt min/avg/max/mdev = 10.000/12.000/14.000/1.000 ms\n"
        )
        mock_run.return_value = mock_result

        result = ping_host("8.8.8.8", 3)
        self.assertEqual(result['host'], "8.8.8.8")
        self.assertEqual(result['avg_response_time_ms'], 12.000)
        self.assertTrue(result['success'])

if __name__ == "__main__":
    unittest.main()