from interface.execution_process import ExecutionProcess
from errors.failed_to_execute import FailedToExecute, FileNotFoundError

class QAQC(ExecutionProcess):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def run(self):
        print("QAQC...")

    def check_if_can_run(self):
        raise FileNotFoundError("Files not found. Archive probably needs to be executed first.")
    
