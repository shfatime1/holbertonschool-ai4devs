import unittest
from log_analyzer import LogAnalyzer

class TestMalformedEntries(unittest.TestCase):
    def test_malformed_entries(self):
        logs = [
            '192.168.1.1 - - [12/Nov/2026:10:00:00] "GET /home HTTP/1.1" 200',
            'This is not a valid log',
            'Invalid log entry'
        ]
        result = LogAnalyzer().analyze(logs)
        self.assertEqual(result["total_requests"], 1)
        self.assertEqual(result["successful_requests"], 1)

if __name__ == "__main__":
    unittest.main()
