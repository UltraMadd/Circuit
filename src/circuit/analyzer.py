"""
LoadFolders is a class that should create a list of files and folders for further processing
AnalysisQueue is a class that is responsible for the sequence of analysis of folders and files
StartAnalysis is a class that is responsible for the analysis and for the interaction of classes during the analysis
"""


import os
from src.circuit.utils import is_a_long_name


class AnalysisQueue:
    """
    This is a class that is responsible for the sequence of analysis of folders and files
    """
    def __init__(self):
        self._queue_folders = []
        self.analysis_tool = StartAnalysis()

    @property
    def folders_count(self):
        return len(self._queue_folders)

    def analyze_latest(self):
        return


class LoadFolders:
    """
    This is a class that should create a list of files and folders for further processing
    """
    def __init__(self, path):
        self.path = path

    def start(self):
        _folder = os.listdir()
        current_path = os.getcwd()
        file_stack = []

        for file in _folder:
            if os.path.isdir(current_path):
                pass

class StartAnalysis:
    """
    This is a class that is responsible for the analysis and for the interaction of classes during the analysis
    """
    def __init__(self, args):
        self.args = args

    def start(self):
        _detected = []

