# Fix Validation Report

All five corrected code files were executed and tested. All listed assertions passed successfully.

## Bug 1 – bug1_fixed.py

**Test Case 1**
- Input: `[40, 60, 80]`
- Expected: `60`
- Actual: `60.0`
- Status: ✔ PASS

**Test Case 2**
- Input: `[10, 20, 30]`
- Expected: `20`
- Actual: `20.0`
- Status: ✔ PASS

**Test Case 3**
- Input: `[]`
- Expected: `0`
- Actual: `0`
- Status: ✔ PASS

**Execution:** Python execution successful.

## Bug 2 – bug2_fixed.js

**Test Case 1**
- Input: `price = 100, discount = 20`
- Expected: `80`
- Actual: `80`
- Status: ✔ PASS

**Test Case 2**
- Input: `price = 200, discount = 10`
- Expected: `180`
- Actual: `180`
- Status: ✔ PASS

**Execution:** Node.js execution successful.

## Bug 3 – bug3_fixed.py

**Test Case 1**
- Input: `user_id = 1`
- Expected: Alice
- Actual: Alice
- Status: ✔ PASS

**Test Case 2**
- Input: `user_id = 2`
- Expected: Bob
- Actual: Bob
- Status: ✔ PASS

**Test Case 3**
- Input: `user_id = 5`
- Expected: User not found
- Actual: User not found
- Status: ✔ PASS

**Manual Tweak:** Changed the missing-user return value from None to "User not found".

**Execution:** Python execution successful.

## Bug 4 – bug4_fixed.js

**Test Case 1**
- Input: `[10, 20, 30, 40]`
- Expected: `100`
- Actual: `100`
- Status: ✔ PASS

**Test Case 2**
- Input: `[5, 10, 15]`
- Expected: `30`
- Actual: `30`
- Status: ✔ PASS

**Test Case 3**
- Input: `[]`
- Expected: `0`
- Actual: `0`
- Status: ✔ PASS

**Execution:** Node.js execution successful.

## Bug 5 – bug5_fixed.java

**Test Case 1**
- Input: `["10", "20", "30"]`
- Expected: `60`
- Actual: `60`
- Status: ✔ PASS

**Test Case 2**
- Input: `["5", "15"]`
- Expected: `20`
- Actual: `20`
- Status: ✔ PASS

**Test Case 3**
- Input: `[]`
- Expected: `0`
- Actual: `0`
- Status: ✔ PASS

**Execution:** Java compilation and execution successful using assertions.

## Final Summary

- Bug 1: ✔ PASS
- Bug 2: ✔ PASS
- Bug 3: ✔ PASS
- Bug 4: ✔ PASS
- Bug 5: ✔ PASS

All five corrected code files were executed successfully. All listed test cases passed.
