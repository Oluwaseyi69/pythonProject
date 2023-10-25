


class IncorrectPinException (Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class EntryNotFoundException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class IncorrectCredentialsException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

