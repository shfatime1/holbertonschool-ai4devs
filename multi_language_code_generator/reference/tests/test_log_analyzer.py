
import unittest
import sys
import os

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from log_analyzer import LogAnalyzer


class TestLogAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = LogAnalyzer()

    def test_normal_logs(self):
        logs = [
            '192.168.1.1 - - [12/Nov/2026:10:00:00] "GET /home HTTP/1.1" 200',
            '192.168.1.2 - - [12/Nov/2026:10:01:00] "POST /login HTTP/1.1" 401',
            '192.168.1.1 - - [12/Nov/2026:10:02:00] "GET /about HTTP/1.1" 200',
            '192.168.1.3 - - [12/Nov/2026:10:03:00] "GET /data HTTP/1.1" 500'
        ]
        result = self.analyzer.analyze(logs)
        self.assertEqual(result["total_requests"], 4)
        self.assertEqual(result["error_rate"], 50.0)

    def test_empty_logs(self):
        result = self.analyzer.analyze([])
        self.assertEqual(result["total_requests"], 0)
        self.assertEqual(result["error_rate"], 0.0)

    def test_duplicate_ips(self):
        logs = [
            '192.168.1.1 - - [12/Nov/2026:10:00:00] "GET /a HTTP/1.1" 200',
            '192.168.1.1 - - [12/Nov/2026:10:01:00] "GET /b HTTP/1.1" 200',
            '192.168.1.1 - - [12/Nov/2026:10:02:00] "GET /c HTTP/1.1" 404'
        ]
        result = self.analyzer.analyze(logs)
        self.assertEqual(result["unique_visitors"], 1)
        self.assertEqual(result["error_rate"], 33.33)

    def test_only_server_errors(self):
        logs = [
            '192.168.1.1 - - [12/Nov/2026:10:00:00] "GET /a HTTP/1.1" 500',
            '192.168.1.2 - - [12/Nov/2026:10:01:00] "GET /b HTTP/1.1" 503',
            '192.168.1.3 - - [12/Nov/2026:10:02:00] "GET /c HTTP/1.1" 500'
        ]
        result = self.analyzer.analyze(logs)
        self.assertEqual(result["server_errors"], 3)
        self.assertEqual(result["error_rate"], 100.0)

    def test_malformed_entries(self):
        logs = [
            '192.168.1.1 - - [12/Nov/2026:10:00:00] "GET /home HTTP/1.1" 200',
            'This is not a valid log',
            'Invalid log entry'
        ]
        result = self.analyzer.analyze(logs)
        self.assertEqual(result["total_requests"], 1)

    def test_only_successful_requests(self):
        logs = [
            '192.168.1.1 - - [12/Nov/2026:10:00:00] "GET /a HTTP/1.1" 200',
            '192.168.1.2 - - [12/Nov/2026:10:01:00] "POST /b HTTP/1.1" 201',
            '192.168.1.3 - - [12/Nov/2026:10:02:00] "GET /c HTTP/1.1" 204'
        ]
        result = self.analyzer.analyze(logs)
        self.assertEqual(result["successful_requests"], 3)
        self.assertEqual(result["error_rate"], 0.0)

    def test_client_errors(self):
        logs = [
            '192.168.1.1 - - [12/Nov/2026:10:00:00] "GET /a HTTP/1.1" 400',
            '192.168.1.2 - - [12/Nov/2026:10:01:00] "GET /b HTTP/1.1" 404'
        ]
        result = self.analyzer.analyze(logs)
        self.assertEqual(result["client_errors"], 2)
        self.assertEqual(result["error_rate"], 100.0)

    def test_invalid_status_code(self):
        logs = [
            '192.168.1.1 - - [12/Nov/2026:10:00:00] "GET /a HTTP/1.1" 999',
            '192.168.1.2 - - [12/Nov/2026:10:01:00] "GET /b HTTP/1.1" 200'
        ]
        result = self.analyzer.analyze(logs)
        self.assertEqual(result["total_requests"], 1)

    def test_missing_ip_address(self):
        logs = [
            '- - - [12/Nov/2026:10:00:00] "GET /a HTTP/1.1" 200'
        ]
        result = self.analyzer.analyze(logs)
        self.assertEqual(result["total_requests"], 0)

    def test_redirect_requests(self):
        logs = [
            '192.168.1.1 - - [12/Nov/2026:10:00:00] "GET /a HTTP/1.1" 301',
            '192.168.1.2 - - [12/Nov/2026:10:01:00] "GET /b HTTP/1.1" 302'
        ]
        result = self.analyzer.analyze(logs)
        self.assertEqual(result["total_requests"], 2)
        self.assertEqual(result["error_rate"], 0.0)


if __name__ == "__main__":
    unittest.main()
