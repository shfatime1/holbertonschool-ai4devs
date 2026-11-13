import unittest
from log_analyzer import LogAnalyzer

class TestInvalidStatus(unittest.TestCase):
    def test_invalid_status(self):
        logs = [
            '192.168.1.1 - - [12/Nov/2026:10:00:00] "GET /a HTTP/1.1" 999',
            '192.168.1.2 - - [12/Nov/2026:10:01:00] "GET /b HTTP/1.1" 200'
        ]
        result = LogAnalyzer().analyze(logs)
        self.assertEqual(result["total_requests"], 1)
        self.assertEqual(result["successful_requests"], 1)

if __name__ == "__main__":
    unittest.main()
