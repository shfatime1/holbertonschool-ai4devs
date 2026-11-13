
import re


class LogAnalyzer:
    def parse_line(self, line: str) -> dict | None:
        """Parse one Apache-style log entry."""
        pattern = (
            r'^(\S+)\s+\S+\s+\S+\s+'
            r'\[.*?\]\s+"[^"]*"\s+(\d{3})(?:\s|$)'
        )

        match = re.match(pattern, line.strip())

        if not match:
            return None

        ip_address = match.group(1)
        status = int(match.group(2))

        if not 100 <= status <= 599:
            return None

        return {
            "ip": ip_address,
            "status": status
        }

    def analyze(self, lines: list) -> dict:
        """Analyze log entries and return statistics."""
        total_requests = 0
        successful_requests = 0
        client_errors = 0
        server_errors = 0
        unique_visitors = set()

        for line in lines:
            entry = self.parse_line(line)

            if entry is None:
                continue

            total_requests += 1
            unique_visitors.add(entry["ip"])

            status = entry["status"]

            if 200 <= status <= 299:
                successful_requests += 1
            elif 400 <= status <= 499:
                client_errors += 1
            elif 500 <= status <= 599:
                server_errors += 1

        if total_requests == 0:
            error_rate = 0.0
        else:
            error_rate = round(
                (client_errors + server_errors)
                / total_requests * 100,
                2
            )

        return {
            "total_requests": total_requests,
            "successful_requests": successful_requests,
            "client_errors": client_errors,
            "server_errors": server_errors,
            "unique_visitors": len(unique_visitors),
            "error_rate": error_rate
        }
