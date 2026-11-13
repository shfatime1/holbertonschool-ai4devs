import unittest
from log_analyzer import LogAnalyzer

class TestRedirectRequests(unittest.TestCase):
    def test_redirect_requests(self):
        logs = [
            '192.168.1.1 - - [12/Nov/2026:10:00:00] "GET /a HTTP/1.1" 301',
            '192.168.1.2 - - [12/Nov/2026:10:01:00] "GET /b HTTP/1.1" 302'
        ]
        result = LogAnalyzer().analyze(logs)
        self.assertEqual(result["total_requests"], 2)
        self.assertEqual(result["error_rate"], 0.0)
        self.assertEqual(result["successful_requests"], 0)

if __name__ == "__main__":
    unittest.main()
