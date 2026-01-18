# AI Code Review Assignment (Python)

## Candidate
**Name:** Emmanuel Rono  
**Approximate time spent:** 70 mins

# Task 1 — Average Order Value

## 1) Code Review Findings

### Critical bugs
- The function adds only non-cancelled orders but divides by all orders. This gives the wrong average if some orders are cancelled.
- If the orders list is empty, the function will crash with a division by zero error.

### Edge cases & risks
- If all orders are cancelled, the total is zero but the function still divides by the number of orders. This gives a misleading average.
- If some orders do not have the keys `"status"` or `"amount"`, the function will crash with a KeyError.
- If `"amount"` is negative or not a number, the function does not handle it.

### Code quality / design issues
- Counts all orders instead of only non-cancelled ones, so the logic does not match the intent.
- Assumes every order has the correct keys and values, which can cause crashes.
- The code is simple but not safe, and it does not do what the explanation says.

## 2) Proposed Fixes / Improvements

### Summary of changes
- Count only non-cancelled orders when calculating the average.
- Add a check to return 0 if there are no non-cancelled orders, so it does not crash.
- Use safe dictionary access to handle missing keys.
- Keep the code simple but correct, so it matches the explanation.

### Corrected code
See `correct_task1.py`

### Testing Considerations
- Test with mixed cancelled and non-cancelled orders to check correct average.
- Test with empty orders list to make sure no crash happens.
- Test with all cancelled orders to see if the function returns 0 safely.
- Test with orders missing `"status"` or `"amount"` keys to check safe handling.
- Test with negative or zero `"amount"` to confirm proper calculation.

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- Says cancelled orders are excluded, but the code still counts them in the divisor.
- The explanation does not match the code.
### Rewritten explanation
> This function calculates the average order value by summing only the amounts of non-cancelled orders and dividing by the number of non-cancelled orders. If there are no non-cancelled orders, it returns 0 safely.

## 4) Final Judgment
- **Decision**: Reject  
- **Justification**: The code does not calculate the correct average and can crash on empty or malformed input. The explanation is also wrong.  
- **Confidence & unknowns**: High confidence. Assumes the business rule is to ignore cancelled orders entirely.


# Task 2 — Count Valid Emails

## 1) Code Review Findings

### Critical bugs
- Only checks for "@" in the email, which is not enough to validate emails.
- Emails like "@example" or "user@" will be counted as valid incorrectly.

### Edge cases & risks
- If some items in the list are not strings (None, numbers), the function will crash.
- If emails have multiple "@" symbols or missing local/domain parts, they are counted incorrectly.
- If the list is empty, the function correctly returns 0, but this should be explicitly handled in testing.

### Code quality / design issues
- Simple logic, but does not follow proper email rules.
- Assumes all list items are strings.
- No input validation or error handling.

## 2) Proposed Fixes / Improvements

### Summary of changes
- Count only emails that are strings and have exactly one "@".
- Check that local and domain parts are not empty.
- Skip non-string items to avoid crashes.
- Keep the code simple and readable.

### Corrected code
See `correct_task2.py`

### Testing Considerations
- Test with valid emails like "user@example.com".
- Test with missing "@" → should not count.
- Test with "@example.com" or "user@" → should not count.
- Test with multiple "@" → should not count.
- Test with empty strings, None, or numbers → should not crash.

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- Says it safely ignores invalid entries, but the code does not. Non-string items will crash.
- Does not check local/domain parts or multiple "@", so explanation is misleading.

### Rewritten explanation
This function counts the number of valid emails in a list. An email is valid if it is a string, has exactly one "@", and both local and domain parts are not empty. Invalid emails and non-string items are ignored.

## 4) Final Judgment
- Decision: Reject  
- Justification: The code counts invalid emails and can crash on non-string items. The explanation is misleading.  
- Confidence & unknowns: High confidence. Assumes basic email validation is required.
---

# Task 3 — Average of Valid Measurements

## 1) Code Review Findings

### Critical bugs
- The function adds only non-None values, but divides by **all values**, including `None`. This gives a wrong average when some values are `None`.
- If the input list is empty, it will crash with a `ZeroDivisionError`.

### Edge cases & risks
- If some values are not numbers or cannot be converted to float, the function will crash.
- If all values are None, the total is 0 but the function still divides by the number of items. This gives a wrong average.
- If some values are negative or zero, the function does not check them, which may or may not be valid depending on context.

### Code quality / design issues

### Code quality / design issues
- Counts all values instead of only valid (non-None) values.
- Assumes all values can be converted to float.
- Simple, but not safe for real-world inputs.

## 2) Proposed Fixes / Improvements

### Summary of changes
- Count only valid (non-None) values for the denominator.
- Convert to float safely, skip items that cannot be converted.
- Return 0 if there are no valid values to avoid division by zero.
- Keep the code simple and readable.

### Corrected code
See `correct_task3.py`

### Testing Considerations
- Test with a mix of numbers and `None` → check correct average.
- Test with empty list → should return 0 safely.
- Test with all `None` → should return 0.
- Test with non-numeric strings → should skip or raise a safe error depending on design.
- Test with negative and zero values → confirm correct average.

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)
> This function calculates the average of a list of measurements, ignoring `None` values.

### Issues in original explanation
- Says it ignores `None`, but divides by all values, so the calculation is wrong.
- Does not mention crash risk on empty list or non-numeric values.

### Rewritten explanation
This function calculates the average of valid measurements in a list. It adds only non-None values and divides by the number of valid values. If there are no valid measurements, it returns 0 safely.

## 4) Final Judgment
- Decision: Reject  
- Justification: The code divides by the total number of items instead of valid values, causing wrong averages. It can also crash on empty or non-numeric inputs.  
- Confidence & unknowns: High confidence. Assumes only non-None numeric values should be counted.

