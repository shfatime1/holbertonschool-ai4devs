import unittest
from log_analyzer import LogAnalyzer

class TestMissingIP(unittest.TestCase):
    def test_missing_ip(self):
        logs = [
            '- - - [12/Nov/2026:10:00:00] "GET /a HTTP/1.1" 200'
        ]
        result = LogAnalyzer().analyze(logs)
        self.assertEqual(result["total_requests"], 0)
        self.assertEqual(result["unique_visitors"], 0)

if __name__ == "__main__":
    unittest.main()
