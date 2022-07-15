"""
LoadFolders is a class that should create a list of files and folders for further processing
ProcessingQueue is a class that is responsible for the sequence of processing of folders and files
StartProcessing is a class that is responsible for the analysis and for the interaction of classes during the processing
"""

import os

import colorama
from colorama import Fore
from typing import List, Union
from dataclasses import dataclass
from argparse import Namespace

from .detections import DetectionTypes


colorama.init()

@dataclass
class Detection:
    """
    detection_id: str
    detection_path: str
    detection_line: int = 0
    """
    detection_id: str
    detection_path: str
    detection_line: int = 0
    path_addon: Union[str, None] = None

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
    def to_str(self, detection_type: str = "W") -> str:
        """
        Converts detection to str
        :param detection_type:
        :return:
        """

        # Return style ^ Look on table ^
        style = "Full"

        # Detection short name " C<ID><type> "
        detection_shortname = f"C{self.detection_id}{detection_type}"

        # Detection description
        detection_desc = DetectionTypes.descriptions[self.detection_id]

        if style == 'Full':
            return f"{Fore.YELLOW}{detection_shortname}{Fore.WHITE} in {self.detection_path}{self.path_addon if self.path_addon else ''} on " \
                   f"{self.detection_line}: {Fore.YELLOW}{detection_desc}{Fore.WHITE}"


@dataclass
class FolderTreeBranch:
    root: str
    dirs: list
    files: list

    def is_empty_dir(self):
        return not (self.files or self.dirs)

    def extract_too_long(self):
        return (
            list(filter(lambda name: len(name) > 75, self.dirs)),
            list(filter(lambda name: len(name) > 75, self.files))
        )


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

    def __init__(self, args: Namespace,
                 folder_tree: List[FolderTreeBranch]):

        self.args: Namespace = args
        self.folder_tree: List[FolderTreeBranch] = folder_tree
        self.detections: List[Detection] = []

    def check_branch(self, branch: FolderTreeBranch) -> None:
        folders_with_long_name, files_with_long_name = branch.extract_too_long()
        if folders_with_long_name:
            for folder in folders_with_long_name:
                self.detections.append(Detection('0003', branch.root + folder))
            del folders_with_long_name
        if files_with_long_name:
            for file in files_with_long_name:
                self.detections.append(Detection('0004', branch.root + file))
            del files_with_long_name
        if branch.is_empty_dir():
            self.detections.append(Detection('0005', branch.root))

    def start(self) -> List[Detection]:
        for branch in self.folder_tree:
            self.check_branch(branch)
        return self.detections
