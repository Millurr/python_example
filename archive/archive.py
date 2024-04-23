from interface.execution_process import ExecutionProcess
from errors.failed_to_execute import FailedToExecute, FileNotFoundError

class Archive(ExecutionProcess):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def run(self):
        print("Archiving...")

    def check_if_can_run(self):
        # TODO: check if files exist in output dir, if they do not then this can run
        raise FailedToExecute("Files not found. Files may not exist in the archive.")

