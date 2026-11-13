# Bug Descriptions

## bug1.py

### Intended Behavior
- get_last_items() should return the last n elements of a list.
- calculate_average() should calculate the average of a list of numbers.
- find_user() should return the user matching the given ID.

### Current Issues
- Incorrect slicing causes the wrong number of items to be returned.
- An empty list causes a division-by-zero error.
- Accessing the first user when no match exists may cause an IndexError.

## bug2.js

### Intended Behavior
- calculateDiscount() should subtract a percentage discount from the original price.
- findUser() should search for a user by ID.
- countCompletedTasks() should count tasks whose completed property is true.

### Current Issues
- The discount amount is subtracted directly instead of calculating a percentage.
- The loop uses an incorrect boundary and may access an undefined element.
- Assignment is used instead of comparison when checking task status.

## bug3.java

### Intended Behavior
- BankAccount should allow valid deposits and withdrawals.
- getBalance() should return the current account balance.
- findNumber() should return the index of a target number or -1 if it is not found.

### Current Issues
- Negative deposit amounts are accepted.
- A withdrawal equal to the current balance is rejected.
- The search loop may access an array index outside its valid range.

## bug4.py

### Intended Behavior
- validate_password() should return True if the password contains at least 8 characters, one digit, and one uppercase letter.
- remove_duplicates() should return a list containing unique original values in their original order.

### Current Issues
- The uppercase flag is incorrectly set to False when an uppercase character is found.
- The password validation uses OR instead of requiring all conditions.
- remove_duplicates() adds indexes instead of the original items.

## Testing Notes

- Test normal inputs and edge cases.
- Test empty lists and missing users.
- Test invalid values such as negative amounts.
- Check array and list boundaries.
- Verify that each function returns the expected result.
