class PrintSelf:
    def __init__(self, message):
        self.message = message

    def __repr__(self):
        print(self.message)
        return super().__repr__()
