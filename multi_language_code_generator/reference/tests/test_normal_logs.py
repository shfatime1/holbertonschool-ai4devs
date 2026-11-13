import unittest
from log_analyzer import LogAnalyzer


class TestNormalLogs(unittest.TestCase):
    def test_normal_logs(self):
        logs = [
            '192.168.1.1 - - [12/Nov/2026:10:00:00] "GET /home HTTP/1.1" 200',
            '192.168.1.2 - - [12/Nov/2026:10:01:00] "POST /login HTTP/1.1" 401',
            '192.168.1.1 - - [12/Nov/2026:10:02:00] "GET /about HTTP/1.1" 200',
            '192.168.1.3 - - [12/Nov/2026:10:03:00] "GET /data HTTP/1.1" 500'
        ]
        result = LogAnalyzer().analyze(logs)
        self.assertEqual(result["total_requests"], 4)
        self.assertEqual(result["error_rate"], 50.0)


if __name__ == "__main__":
    unittest.main()
