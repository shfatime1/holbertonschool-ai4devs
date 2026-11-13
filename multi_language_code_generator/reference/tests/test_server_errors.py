import unittest
from log_analyzer import LogAnalyzer

class TestServerErrors(unittest.TestCase):
    def test_server_errors(self):
        logs = [
            '192.168.1.1 - - [12/Nov/2026:10:00:00] "GET /a HTTP/1.1" 500',
            '192.168.1.2 - - [12/Nov/2026:10:01:00] "GET /b HTTP/1.1" 503',
            '192.168.1.3 - - [12/Nov/2026:10:02:00] "GET /c HTTP/1.1" 500'
        ]
        result = LogAnalyzer().analyze(logs)
        self.assertEqual(result["server_errors"], 3)
        self.assertEqual(result["error_rate"], 100.0)

if __name__ == "__main__":
    unittest.main()
