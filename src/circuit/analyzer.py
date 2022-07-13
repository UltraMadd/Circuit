"""
LoadFolders is a class that should create a list of files and folders for further processing
ProcessingQueue is a class that is responsible for the sequence of processing of folders and files
StartProcessing is a class that is responsible for the analysis and for the interaction of classes during the processing
"""


import os
from src.circuit.utils import is_a_long_name
from dataclasses import dataclass


@dataclass
class FolderTreeBranch:
    root: str
    dirs: list
    files: list


class ProcessingQueue:
    """
    This is a class that is responsible for the sequence of processing of folders and files
    """
    def __init__(self, args):
        self._queue_folders = []
        self.analysis_tool = StartProcessing(args)

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
        folder_tree = os.walk(self.path)
        folder_tree_branches = []

        for root, dirs, files in folder_tree:
            folder_tree_branches.append(
                FolderTreeBranch(root, dirs, files)
            )
        print(folder_tree_branches)


class StartProcessing:
    """
    This is a class that is responsible for the analysis and for the interaction of classes during the processing
    """
    def __init__(self, args):
        self.args = args

    def start(self):
        _detected = []

