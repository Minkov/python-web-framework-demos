from django.core.exceptions import ValidationError

'''
# (Developers) Tests where environment/lang matters (if Django => tests in python)
1. Unit tests -> concrete isolated piece of code
2. Integration tests -> integration of coupled pieces of code

# Tests where environment/lang does NOT matter

3. (QAs) API tests -> Check if the API works correctly
    - Check if the result of HTTP call returns the correct JSON
4. Functional/E2E/UI tests

# Other tests
5. Load tests
6. Performance tests
7. Security tests
'''

'''
Unit tests
'''


def validate_greater_than_zero(value):
    if value <= 0:
        raise ValidationError('Value must be  greater than 0')


'''
- check for negative value -> Error
- check for 0 value (corner case) -> Error
- check for positive value -> No error
'''


def get_only_positive_values(values):
    positive_values = []
    for value in values:
        try:
            validate_greater_than_zero(value)
            positive_values.append(value)
        except:
            pass

    return positive_values


'''
# With unit tests:
Mock validate_greater_than_zero
- check for empty list
- check for list with positives
- check for list with negatives

# With integration tests:
- No mocking
- [] => []
- [1, 2, 3] => [1, 2, 3]
- [0, 1, 2] => [1, 2]
- [0, 0, 0] => []
- [.....
'''


'''
- Tests change!
- Tests are part of the code
- Tests give us "Fast fail"
- Tests give us Piece of mind
'''