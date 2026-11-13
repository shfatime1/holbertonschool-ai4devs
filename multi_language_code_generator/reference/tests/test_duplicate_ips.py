import unittest
from log_analyzer import LogAnalyzer

class TestDuplicateIPs(unittest.TestCase):
    def test_duplicate_ips(self):
        logs = [
            '192.168.1.1 - - [12/Nov/2026:10:00:00] "GET /a HTTP/1.1" 200',
            '192.168.1.1 - - [12/Nov/2026:10:01:00] "GET /b HTTP/1.1" 200',
            '192.168.1.1 - - [12/Nov/2026:10:02:00] "GET /c HTTP/1.1" 404'
        ]
        result = LogAnalyzer().analyze(logs)
        self.assertEqual(result["unique_visitors"], 1)
        self.assertEqual(result["total_requests"], 3)
        self.assertEqual(result["error_rate"], 33.33)

if __name__ == "__main__":
    unittest.main()
