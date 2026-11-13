
# Cross-Language Specification - Log Analyzer

## 1. Algorithm Description

The Log Analyzer reads server log entries and generates useful statistics.

It must calculate:
- Total number of requests.
- Number of successful requests (2xx status codes).
- Number of client errors (4xx status codes).
- Number of server errors (5xx status codes).
- Number of unique IP addresses.
- Overall error rate as a percentage.

The algorithm should produce the same results when implemented in different programming languages.

## 2. Input Format

The input is a list of log entries.

Each entry contains:
- IP address
- Timestamp
- HTTP method
- Requested URL
- HTTP status code

Example:

```text
192.168.1.1 - - [12/Nov/2026:10:00:00] "GET /home HTTP/1.1" 200
192.168.1.2 - - [12/Nov/2026:10:01:00] "POST /login HTTP/1.1" 401
192.168.1.1 - - [12/Nov/2026:10:02:00] "GET /about HTTP/1.1" 200
192.168.1.3 - - [12/Nov/2026:10:03:00] "GET /data HTTP/1.1" 500
```

## 3. Output Format

The algorithm must return a JSON object containing the calculated statistics.

Example:

```json
{
  "total_requests": 4,
  "successful_requests": 2,
  "client_errors": 1,
  "server_errors": 1,
  "unique_visitors": 3,
  "error_rate": 50.0
}
```

The error rate is calculated using:

Error Rate = (Client Errors + Server Errors) / Total Requests * 100

## 4. Edge Cases

- Empty log file: Return zero for all statistics.
- Malformed log entry: Skip the invalid entry.
- Duplicate IP addresses: Count each IP only once.
- Invalid HTTP status code: Skip the invalid entry.
- File with only successful requests: Error rate must be 0%.
- File with only errors: Error rate must be 100%.
- Missing IP address: Skip the invalid entry.

## 5. Test Cases

### Test Case 1 - Normal Log File

**Input:** 4 valid entries with status codes 200, 401, 200, 500.

**Expected Output:**
- Total requests: 4
- Successful requests: 2
- Client errors: 1
- Server errors: 1
- Unique visitors: 3
- Error rate: 50.0%

### Test Case 2 - Empty Log File

**Input:** Empty file.

**Expected Output:**
- Total requests: 0
- Successful requests: 0
- Client errors: 0
- Server errors: 0
- Unique visitors: 0
- Error rate: 0.0%

### Test Case 3 - Duplicate IP Addresses

**Input:** 3 entries from the same IP address with status codes 200, 200, 404.

**Expected Output:**
- Total requests: 3
- Successful requests: 2
- Client errors: 1
- Server errors: 0
- Unique visitors: 1
- Error rate: 33.33%

### Test Case 4 - Only Server Errors

**Input:** 3 valid entries with status codes 500, 503, 500.

**Expected Output:**
- Total requests: 3
- Successful requests: 0
- Client errors: 0
- Server errors: 3
- Unique visitors: 3
- Error rate: 100.0%

### Test Case 5 - Malformed Entries

**Input:** 3 lines: one valid entry with status 200 and two malformed entries.

**Expected Output:**
- Total requests: 1
- Successful requests: 1
- Client errors: 0
- Server errors: 0
- Unique visitors: 1
- Error rate: 0.0%

### Test Case 6 - Only Successful Requests

**Input:** 3 valid entries with status codes 200, 201, 204.

**Expected Output:**
- Total requests: 3
- Successful requests: 3
- Client errors: 0
- Server errors: 0
- Unique visitors: 3
- Error rate: 0.0%

## 6. Cross-Language Requirements

The algorithm can be implemented in Python, JavaScript, Java, or another programming language.

All implementations must:
- Follow the same input and output formats.
- Apply the same validation rules.
- Skip malformed entries.
- Produce identical results for all test cases.
- Calculate the error rate consistently, rounded to two decimal places.
