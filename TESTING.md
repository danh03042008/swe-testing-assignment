# Testing strategy

## What i tested
I tested all four core calculator operations: addition, subtraction, multiplication, and division. I also tested edge cases such as division by zero, negative numbers, decimal numbers, and large numbers. Finally I tested the clear function to verify it resets to zero.

## What i didn't test
I didnt test any UI or user input validation since this project uses pure functions with no interface. Non-functional aspects such as performance and security were also not tested as they are not relevant for a simple calculator.

## Lecture Concepts

### 1. The Testing Pyramid
My test follows the testing pyramid. The majority of my tests are unit tests which form the base of the pyramid, and I have 2 integration tests at the higher level. This is the correct proportion, many small fast unit tests and fewer integration tests.

### 2. Black-box vs White-box Testing
For unit tests i used white-box testing since i wrote the functions myself and tested them knowing exactly how they work internally. For integration tests i used black-box testing, focusing only on inputs and outputs of the combined functions without caring about internal implementation.

### 3. Regression Testing
If new features are added to Quick-Calc in the future, the existing test suite can be run with a single `pytest` command to immediately check if anything broke. This makes the test suite a safety net for future development.

### 4. Functional vs Non-Functional Testing
All my tests are functional, they verify that the calculator produces correct results. I intentionally did not write non-functional tests such as performance or load tests as they are unnecessary for a basic calculator.

## Test Results Summary
test_add, unit - Pass
test_subtract, unit - Pass
test_multiply, unit - Pass
test_divide, unit - Pass
test_divide_by_zero, unit, pass
test_negative_numbers, unit - Pass
test_decimal_numbers, unit - Pass
test_large_numbers, unit - Pass
test_clear, unit - Pass
test_full_calculation_sequence, integration - Pass
test_clear_resets_to_zero, integration - Pass
