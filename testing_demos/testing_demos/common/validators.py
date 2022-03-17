from django.core.exceptions import ValidationError


def validate_only_letters(value):
    invalid_chars = [ch for ch in value if not ch.isalpha()]
    if invalid_chars:
        raise ValidationError(f'Value must contain only letters, but contains: {invalid_chars}')
    # for ch in value:
    #     if not ch.isalpha():
    #         raise ValidationError('Value must contain only letters')

'''
          BEFORE     AFTER
asd =>    valid      valid
a123 =>   invalid    valid
123 =>    invalid    valid
_asd =>   invalid    valid
$123 =>   invalid    invalid
asd#as => invalid    invalid
асдасд => invalid    valid
...
'''