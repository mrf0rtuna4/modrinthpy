class ModrinthAPIError(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message
        super().__init__(f"Modrinth API Error ({status_code}) - {message}")


class MissingArguments(Exception):
    def __init__(self, *arguments):
        self.arguments = arguments
        super().__init__(f"Missing arguments - {', '.join(arguments)}")


class UnauthorizedError(Exception):
    def __init__(self, message):
        super().__init__(message)