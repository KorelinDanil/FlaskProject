class BlockErrors:
    def __init__(self, error_types):
        self.error_types = tuple(error_types)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return issubclass(exc_type, self.error_types) if exc_type else False
