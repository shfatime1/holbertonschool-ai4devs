import unittest
from log_analyzer import LogAnalyzer

class TestClientErrors(unittest.TestCase):
    def test_client_errors(self):
        logs = [
            '192.168.1.1 - - [12/Nov/2026:10:00:00] "GET /a HTTP/1.1" 400',
            '192.168.1.2 - - [12/Nov/2026:10:01:00] "GET /b HTTP/1.1" 404'
        ]
        result = LogAnalyzer().analyze(logs)
        self.assertEqual(result["client_errors"], 2)
        self.assertEqual(result["error_rate"], 100.0)

if __name__ == "__main__":
    unittest.main()
