
from errors.recoverable_fault import RecoverableFault
from errors.unrecoverable_fault import UnrecoverableFault


"""
This class is used to raise an exception when a process fails to execute.
TODO: Add more information about errors and send an email to the developers.
"""
class FailedToExecute(UnrecoverableFault):
    def __init__(self, message):
        super().__init__(message)


class FileNotFoundError(RecoverableFault):
    def __init__(self, message):
        super().__init__(message)
