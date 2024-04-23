from archive.archive import Archive
from computation.computation import Computation
from errors.recoverable_fault import RecoverableFault
from errors.unrecoverable_fault import UnrecoverableFault
from quality_assurance.qaqc import QAQC
from curate.curate import Curate
from interface.execution_process import ExecutionProcess

def run():
    archive = Archive()
    qaqc = QAQC()
    curate = Curate()
    computation = Computation()

    executions = [
        archive,
        qaqc,
        curate,
        computation
    ]

    for execution in executions:
        if isinstance(execution, ExecutionProcess):
            try:
                if execution.check_if_can_run():
                    execution.run()
                else:
                    print(f"Can not run {execution.__class__.__name__}")
            except RecoverableFault as e:
                # TODO: recoverable so determine the error and try again
                print(e)
            except UnrecoverableFault as e:
                # TDOO: break and notify of failure
                print(e)
                break

if __name__ == "__main__":
    run()
