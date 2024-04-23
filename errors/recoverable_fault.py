

class RecoverableFault(Exception):
    """
    This class is used to raise an exception when a process fails to execute.
    TODO: Reoverable means something failed but should be retried or something else needs to be attempted.
    """
    def __init__(self, message):
        super().__init__(message)

