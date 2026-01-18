# Notes 

## Assumptions made
1. For Task 1, I assumed the business rule is that cancelled orders should be completely excluded from the average calculation.
2. For Task 2, I assumed basic email validation only requires one "@" symbol with non-empty local and domain parts.
3. For Task 3, I assumed only numeric, non-None measurements should be counted.

## Known limitations
1. The corrected email validation in Task 2 does not fully validate domains (e.g., "example" without a dot is considered valid). This keeps the code simple and safe.
2. Task 3 skips any non-numeric value silently. A stricter implementation could raise an error instead.

## Alternative approaches considered
1. Task 1: Could have used `filter()` or list comprehensions, but kept a for-loop for clarity.
2. Task 2: Could use regex for full email validation, but kept a simple string check for readability.
3. Task 3: Could use `try/except` outside the loop with `map()`, but kept in-loop handling for clarity and ESL-level readability.
