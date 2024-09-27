class ModrinthAPIError(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message
        super().__init__(f"Modrinth API Error {status_code}: {message}")