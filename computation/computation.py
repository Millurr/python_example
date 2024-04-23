
from interface.execution_process import ExecutionProcess

class Computation(ExecutionProcess):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def run(self):
        print("Computing...")

    def check_if_can_run(self):
        # TODO: check if files exist in the source dir, if they do not then this can't run
        return False
