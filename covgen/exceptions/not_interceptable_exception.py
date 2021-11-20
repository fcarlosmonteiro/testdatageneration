class NotInterceptableException(Exception):
    """Exception raised for errors when not able to inject trace

    Attributes:
        predicate -- predicate in not expected form
        message -- explanation of the error
    """

    def __init__(self, predicate, message):
        self.predicate = predicate
        self.message = message
