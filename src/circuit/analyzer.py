"""
LoadFolders is a class that should create a list of files and folders for further processing
ProcessingQueue is a class that is responsible for the sequence of processing of folders and files
StartProcessing is a class that is responsible for the analysis and for the interaction of classes during the processing
"""

import os
from typing import List
from dataclasses import dataclass


@dataclass
class Detection:
    detection_id: str
    detection_path: str
    detection_line: int = 0

    """
     Style # return                                              
     ------------------------------------------------------------
     Full  # C<id><type> in <path> on <line> line: <desc>        
     ------------------------------------------------------------
     File  # C<id><type> in <path> on <line> line                
     ------------------------------------------------------------
     Dir   # C<id><type> in <path>: <desc>                       
     ------------------------------------------------------------
    """
    def to_str(self, style: str, detection_type: str = "W") -> str:
        """
        Converts detection to str
        :param detection_type:
        :param style:
        :return:
        """
        detection_shortname = f"C{self.detection_id}{detection_type}"
        detection_desc = ''   # Detection description
        if style == 'Full':
            return f"{detection_shortname} in {self.detection_path} on " \
                   f"{self.detection_line} {detection_desc}"


@dataclass
class Detections:
    pass


@dataclass
class FolderTreeBranch:
    root: str
    dirs: list
    files: list

    def is_empty_dir(self):
        return not (self.files or self.dirs)


class ProcessingQueue:
    """
    This is a class that is responsible for the sequence of processing of folders and files
    """

    def __init__(self, args) -> None:
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

    def __init__(self, path: str) -> None:
        self.path = path

    def start(self):
        folder_tree = os.walk(self.path)
        folder_tree_branches = []

        for root, dirs, files in folder_tree:
            folder_tree_branches.append(
                FolderTreeBranch(root, dirs, files)
            )

        return folder_tree_branches


class StartProcessing:
    """
    This is a class that is responsible for the analysis and for the interaction of classes during the processing
    :param args:
    :param folder_tree:
    """

    def __init__(self, args: 'Namespace',
                 folder_tree: List[FolderTreeBranch]):

        self.args = args
        self.folder_tree = folder_tree

    def start(self):
        for branch in self.folder_tree:
            if branch.is_empty_dir():
                pass
