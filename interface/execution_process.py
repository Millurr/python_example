from abc import ABC, abstractmethod

class ExecutionProcess(ABC):
    @abstractmethod
    def run(self):
        """
        This function should hold the code that will be executed by the process.
        """
        raise NotImplementedError("run() not implemented")
    
    @abstractmethod
    def check_if_can_run(self): 
        """
        This function should return a boolean value that indicates if the process can be executed or not.
        An example of this is to check if files exist and a given directory. If so that means the previous step ran so this process can be executed.
        """
        raise NotImplementedError("check_if_can_run() not implemented")
    
