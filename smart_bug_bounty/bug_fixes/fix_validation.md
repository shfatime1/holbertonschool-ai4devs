# Fix Validation Report

## Overview

This report documents the fixes applied to four buggy code snippets and the results of executing validation tests.

## bug1_fixed.py

### Original Issues
- Incorrect list slicing.
- Division by zero for empty lists.
- Incorrect behavior when a user ID is not found.

### Fixes Applied
- Corrected slicing using items[-n:].
- Added empty-list validation.
- Return None when no matching user is found.

### Test Results

| Test | Expected Result | Actual Result | Status |
|---|---|---|---|
| Last items: [1,2,3,4], n=2 | [3,4] | [3,4] | PASS |
| Zero items: n=0 | [] | [] | PASS |
| Average: [10,20,30] | 20 | 20.0 | PASS |
| Empty average: [] | None | None | PASS |
| Missing user | None | None | PASS |

## bug2_fixed.js

### Original Issues
- Incorrect discount calculation.
- Array boundary error.
- Assignment used instead of comparison.

### Fixes Applied
- Corrected percentage discount calculation.
- Fixed array loop boundary.
- Replaced assignment with strict comparison.
- Added input validation.

### Test Results

| Test | Expected Result | Actual Result | Status |
|---|---|---|---|
| Price=100, discount=20 | 80 | 80 | PASS |
| Price=100, discount=0 | 100 | 100 | PASS |
| Find existing user | Matching user | Matching user | PASS |
| Find missing user | null | null | PASS |
| Completed tasks | 2 | 2 | PASS |
| Discount=120 | Error | Error | PASS |

## bug3_fixed.java

### Original Issues
- Negative deposits were accepted.
- Full balance withdrawal was rejected.
- Invalid array boundary in findNumber().

### Fixes Applied
- Added positive deposit validation.
- Allowed withdrawal of the full balance.
- Added withdrawal validation.
- Corrected array loop boundary.

### Test Results

| Test | Expected Result | Actual Result | Status |
|---|---|---|---|
| Deposit 50 into balance 100 | 150 | 150 | PASS |
| Negative deposit | Exception | Exception | PASS |
| Withdraw full balance 100 | 0 | 0 | PASS |
| Withdraw 150 from balance 100 | Exception | Exception | PASS |
| Find 20 in [10,20,30] | Index 1 | Index 1 | PASS |
| Find missing number 40 | -1 | -1 | PASS |

## bug4_fixed.py

### Original Issues
- Incorrect uppercase flag.
- Incorrect Boolean condition.
- Returned indexes instead of original values.

### Fixes Applied
- Corrected uppercase detection.
- Changed OR to AND.
- Appended original items when removing duplicates.

### Test Results

| Test | Expected Result | Actual Result | Status |
|---|---|---|---|
| Password Hello123 | True | True | PASS |
| Password hello123 | False | False | PASS |
| Password HelloWorld | False | False | PASS |
| Password Abc123 | False | False | PASS |
| Remove duplicates [1,2,2,3] | [1,2,3] | [1,2,3] | PASS |
| Remove duplicates ["a","b","a"] | ["a","b"] | ["a","b"] | PASS |

## Final Summary

- bug1_fixed.py: 5/5 test cases passed.
- bug2_fixed.js: 6/6 test cases passed.
- bug3_fixed.java: 6/6 test cases passed.
- bug4_fixed.py: 6/6 test cases passed.

Total: 23/23 test cases passed.

All documented test cases passed during validation.
