class NoTargetFunctionException(Exception):
    """Exception raised when no target function is found with given name.
    Attributes:
        name -- function name given
        message -- explanation of the error
    """

    def __init__(self, name, message):
        self.name = name
        self.message = message
