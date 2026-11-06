# Structured Bug Reports

## Bug Report – bug1.py

- **File Name:** `bug1.py`
- **Bug Summary:** The code had a syntax error because the `if` statement was missing a colon. It could also cause a division-by-zero error when the input list was empty.
- **Root Cause:** The conditional statement was incorrectly written without a colon, and the function did not check for empty input.
- **Resolution:**
  - **AI-Generated:** Suggested adding the missing colon and checking whether the list is empty before calculating the average.
  - **Manual Fix:** Added `if not numbers: return 0` to handle empty lists safely.
- **Lessons Learned:** Always check Python syntax and test edge cases, especially empty lists.

## Bug Report – bug2.js

- **File Name:** `bug2.js`
- **Bug Summary:** The discount calculation increased the original price instead of reducing it.
- **Root Cause:** The code used addition instead of subtraction when calculating the discount.
- **Resolution:**
  - **AI-Generated:** Identified the incorrect arithmetic operation and suggested subtracting the discount amount from the original price.
  - **Manual Fix:** Updated the formula to `price - (price * discount / 100)` and added test assertions.
- **Lessons Learned:** Verify mathematical operations with simple test examples to ensure calculations produce the expected results.

## Bug Report – bug3.py

- **File Name:** `bug3.py`
- **Bug Summary:** The original code attempted to access a user ID that did not exist in the dictionary, causing a `KeyError`.
- **Root Cause:** The code accessed a dictionary entry without checking whether the requested user ID existed.
- **Resolution:**
  - **AI-Generated:** Suggested checking whether the user exists before accessing the dictionary entry.
  - **Manual Fix:** Replaced direct dictionary access with `.get()` and returned `"User not found"` when the user does not exist.
- **Lessons Learned:** Always validate dictionary keys and handle missing data gracefully.

## Bug Report – bug4.js

- **File Name:** `bug4.js`
- **Bug Summary:** The loop used an incorrect boundary condition, causing an extra iteration and accessing an undefined array element.
- **Root Cause:** The loop condition used `i <= numbers.length` instead of `i < numbers.length`.
- **Resolution:**
  - **AI-Generated:** Identified the off-by-one error and recommended using a strict less-than condition.
  - **Manual Fix:** Changed the loop condition to `i < numbers.length` and added tests for normal and empty arrays.
- **Lessons Learned:** Array indexes start at zero, so loop boundaries must be checked carefully.

## Bug Report – bug5.java

- **File Name:** `bug5.java`
- **Bug Summary:** The code attempted to add a String value directly to an integer, causing a compilation error.
- **Root Cause:** The program did not convert the price strings into integers before performing addition.
- **Resolution:**
  - **AI-Generated:** Suggested converting each String value into an integer before adding it to the total.
  - **Manual Fix:** Used `Integer.parseInt(price)` and added assertions to validate the calculation.
- **Lessons Learned:** Pay attention to data types and convert values before performing operations that require a specific type.

## Final Summary

All five bugs were analyzed and fixed. AI assistance helped identify the root causes and suggest solutions. Manual edits were applied to improve error handling and add validation tests.

Testing confirmed that all five corrected programs passed their listed test cases.
