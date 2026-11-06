
# Bug Snippets - Bug Descriptions

This document describes five buggy code examples created for testing AI debugging assistants.

## Bug 1 – bug1.py

**Language:** Python

**Intended Behavior:** Calculate the average of a list of numbers and display whether the average is high or low.

**Issue Type:** Syntax Error.

**Notes:** The if statement is missing a colon. The function should also handle an empty list safely.

## Bug 2 – bug2.js

**Language:** JavaScript

**Intended Behavior:** Calculate the final product price after applying a percentage discount.

**Issue Type:** Logical Error.

**Notes:** The function adds the discount instead of subtracting it from the original price.

## Bug 3 – bug3.py

**Language:** Python

**Intended Behavior:** Retrieve and display a user's name and email using their ID.

**Issue Type:** Runtime Exception.

**Notes:** The function tries to access user ID 5, which does not exist in the dictionary. It should handle missing users.

## Bug 4 – bug4.js

**Language:** JavaScript

**Intended Behavior:** Print all numbers in an array and calculate their total.

**Issue Type:** Off-by-One Error.

**Notes:** The loop condition uses <= instead of <. This causes an additional iteration and produces an undefined value.

## Bug 5 – bug5.java

**Language:** Java

**Intended Behavior:** Calculate the total price from an array of numeric price values stored as strings.

**Issue Type:** Data Type Misuse.

**Notes:** The code attempts to add String values directly to an integer. Each price should be converted to an integer before addition.

## Conclusion

These five examples cover different types of programming errors, including syntax errors, logical errors, runtime exceptions, loop boundary mistakes, and data type misuse. They can be used to test how effectively AI assistants identify and correct programming problems.
