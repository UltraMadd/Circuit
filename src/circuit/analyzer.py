import os
from utils import is_a_long_name


class AnalysisQueue:
    def __init__(self):
        self._queue_folders = []

    @property
    def folders_count(self):
        return len(self._queue_folders)

    def analyze_latest(self):
        return


class StartAnalysis:
    def __init__(self, args):
        self.args = args

    def start(self):
        pass
