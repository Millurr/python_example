

class UnrecoverableFault(Exception):
    """
    This class is used to raise an exception when a process fails to execute.
    TODO: Unrecoverable means something seriously failed and should probably notify the developers.
    """
    def __init__(self, message):
        super().__init__(message)

