from interface.execution_process import ExecutionProcess
        # TODO: check if files exist in the source dir, if they do not then this can't run

class Curate(ExecutionProcess):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def run(self):
        print("Curating...")

    def check_if_can_run(self):
        # TODO: check if files exist in the source dir, if they do not then this can't run
        return True
    