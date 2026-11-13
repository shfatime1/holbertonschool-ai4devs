
# Coding Benchmark Tasks

This document contains three small coding tasks designed to test coding skills and AI coding assistant performance. Each task should take approximately 15–30 minutes to complete.

## Task 1 - To-Do List API

**Requirements:**
- Create an API endpoint to add a new task.
- Create an endpoint to display all tasks.
- Each task must have an ID, title, and completion status.
- Validate that the task title is not empty.

**Inputs:**
- JSON: `{ "title": "Learn Python" }`

**Outputs:**
- A created task with a unique ID and completion status.
- A list of all saved tasks.

**Acceptance Criteria:**
- Returns a successful response when a task is created.
- Returns an error if the title is empty.
- Displays all existing tasks correctly.

**Estimated Time:** 20 minutes

---

## Task 2 - Password Strength Checker

**Requirements:**
- Create a function that checks password strength.
- A strong password must contain at least 8 characters.
- It must include uppercase letters, lowercase letters, and numbers.
- Return a clear message describing the password strength.

**Inputs:**
- A password string, for example: `"Hello123"`

**Outputs:**
- `"Strong password"` or `"Weak password"`.

**Acceptance Criteria:**
- Accepts passwords that meet all requirements.
- Rejects passwords shorter than 8 characters.
- Rejects passwords without uppercase, lowercase, or numeric characters.
- Handles empty input correctly.

**Estimated Time:** 15 minutes

---

## Task 3 - Expense Calculator

**Requirements:**
- Create a function that calculates total expenses.
- Accept a list of expense amounts.
- Calculate the total and average expense.
- Handle an empty list without errors.

**Inputs:**
- A list of numbers, for example: `[20, 35, 15, 50]`

**Outputs:**
- Total expense: `120`
- Average expense: `30`

**Acceptance Criteria:**
- Calculates the total correctly.
- Calculates the average correctly.
- Returns zero for both total and average when the list is empty.
- Handles multiple expense amounts.

**Estimated Time:** 15 minutes

---

## Conclusion

These three tasks cover different coding skills, including API development, input validation, conditional logic, and basic calculations. They can be used to compare coding speed, accuracy, and the usefulness of an AI coding assistant.
