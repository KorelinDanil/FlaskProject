from wtforms import ValidationError

# Функциональный способ
def phone_length(min_len: int, max_len: int, message=None):
    def _validator(form, field):
        length = len(str(field.data))
        if length < min_len or length > max_len:
            raise ValidationError(message or f"Phone must be between {min_len} and {max_len} digits")
    return _validator

# Классовый способ
class PhoneLength:
    def __init__(self, min_len, max_len, message=None):
        self.min_len = min_len
        self.max_len = max_len
        self.message = message

    def __call__(self, form, field):
        length = len(str(field.data))
        if length < self.min_len or length > self.max_len:
            raise ValidationError(self.message or f"Phone must be between {self.min_len} and {self.max_len} digits")
