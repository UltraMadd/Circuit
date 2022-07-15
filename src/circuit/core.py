"""
Managing processing
"""


class ProcessingManager:
    def __init__(self, tasks):
        self.tasks = tasks

    def _do_task(self):
        task, task_id = self.tasks.latest

        try:
            task.run()
        finally:
            self.tasks.complete(task_id)


'''
import threading
from typing import List


class FileThread(threading.Thread):
    def __init__(self, files: List[List[str, List, List]], analysis_func):
        """
        Special FileThread class to analyze files
        :param files: files structure
        List[List[root_path, dirs, files]]
        :param analysis_func: methods will call this func to process files
        """
        super().__init__()
        self.files = files   # Files for analysis
        self.analysis_func = analysis_func   # Methods will call this func to process files

    def run(self) -> None:
        pass
'''  # TODO Write threads
