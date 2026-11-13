import unittest
from log_analyzer import LogAnalyzer

class TestSuccessfulRequests(unittest.TestCase):
    def test_successful_requests(self):
        logs = [
            '192.168.1.1 - - [12/Nov/2026:10:00:00] "GET /a HTTP/1.1" 200',
            '192.168.1.2 - - [12/Nov/2026:10:01:00] "POST /b HTTP/1.1" 201',
            '192.168.1.3 - - [12/Nov/2026:10:02:00] "GET /c HTTP/1.1" 204'
        ]
        result = LogAnalyzer().analyze(logs)
        self.assertEqual(result["successful_requests"], 3)
        self.assertEqual(result["error_rate"], 0.0)

if __name__ == "__main__":
    unittest.main()
