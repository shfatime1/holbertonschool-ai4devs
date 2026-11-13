# Fix Validation Report

## Overview

This document describes the fixes applied to four buggy code snippets and the test cases used to verify the corrected behavior.

## bug1_fixed.py

### Original Issues
- Incorrect list slicing.
- Division by zero for empty lists.
- Incorrect behavior when a user ID is not found.

### Fixes Applied
- Changed slicing to `items[-n:]`.
- Added an empty-list check in calculate_average().
- Changed find_user() to return None when no match exists.

### Test Cases

| Test | Input | Expected Result |
|---|---|---|
| Last items | [1, 2, 3, 4], n=2 | [3, 4] |
| Zero items | [1, 2, 3], n=0 | [] |
| Average | [10, 20, 30] | 20 |
| Empty average | [] | None |
| Missing user | User ID not found | None |

### Test Results
Expected behavior is defined for all five test cases. Run the tests to confirm the results.

---

## bug2_fixed.js

### Original Issues
- Incorrect discount calculation.
- Array boundary error.
- Assignment used instead of comparison.

### Fixes Applied
- Implemented percentage-based discount calculation.
- Changed loop condition to i < users.length.
- Replaced assignment with strict comparison.
- Added validation for invalid price and discount values.

### Test Cases

| Test | Input | Expected Result |
|---|---|---|
| Discount | price=100, discount=20 | 80 |
| No discount | price=100, discount=0 | 100 |
| Find user | Existing user ID | Matching user |
| Missing user | Unknown ID | null |
| Completed tasks | [true, false, true] | 2 |
| Invalid discount | discount=120 | Error |

### Test Results
Expected behavior is defined for all six test cases. Run the tests with Node.js to confirm the results.

---

## bug3_fixed.java

### Original Issues
- Negative deposits were accepted.
- Withdrawal equal to the balance was rejected.
- Array search used an invalid boundary condition.

### Fixes Applied
- Added validation for positive deposit amounts.
- Allowed withdrawal of the exact available balance.
- Added validation for withdrawal amounts.
- Changed the array loop condition to i < numbers.length.
- Added validation for the initial account balance.

### Test Cases

| Test | Input | Expected Result |
|---|---|---|
| Deposit | Initial balance=100, deposit=50 | Balance=150 |
| Negative deposit | deposit=-20 | IllegalArgumentException |
| Full withdrawal | Balance=100, withdraw=100 | Balance=0 |
| Excess withdrawal | Balance=100, withdraw=150 | IllegalArgumentException |
| Find number | [10, 20, 30], target=20 | Index 1 |
| Missing number | [10, 20, 30], target=40 | -1 |

### Test Results
Expected behavior is defined for all six test cases. Compile and run the Java code to confirm the results.

---

## bug4_fixed.py

### Original Issues
- Uppercase flag was incorrectly set to False.
- Password conditions used OR instead of AND.
- Duplicate removal returned indexes instead of original values.

### Fixes Applied
- Set has_uppercase to True when an uppercase character is found.
- Changed the final condition to require both a digit and an uppercase letter.
- Appended the original item instead of its index.

### Test Cases

| Test | Input | Expected Result |
|---|---|---|
| Valid password | Hello123 | True |
| No uppercase | hello123 | False |
| No digit | HelloWorld | False |
| Too short | Abc123 | False |
| Remove duplicates | [1, 2, 2, 3] | [1, 2, 3] |
| String duplicates | ["a", "b", "a"] | ["a", "b"] |

### Test Results
Expected behavior is defined for all six test cases. Run the tests to confirm the results.

---

## Final Summary

- Four code snippets were reviewed and corrected.
- Input validation and boundary conditions were improved.
- Incorrect calculations and Boolean logic were fixed.
- Expected results were documented for 23 test cases.

**Note:** The test cases and expected results are documented here. Actual test execution must be completed before marking all tests as passed.
