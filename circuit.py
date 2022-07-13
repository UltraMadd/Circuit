import argparse
import os

from src import circuit

parser = argparse.ArgumentParser(description="-path: Path to project folder (from first .py file)")
parser.add_argument("-path", dest="path", required=True)
parser.add_argument("-patch", dest="patch")
arguments = parser.parse_args()


def prepare(args: argparse.Namespace) -> bool:
    """
    Prepare for analyze
    :param args: argparse.Namespace
    :return: bool do program need an analysis or path is empty
    """
    if not os.path.exists(args.path):
        raise OSError(f"Path {args.path} doesn't exists")

    os.chdir(args.path)   # Moving to analyze path

    if not os.listdir():
        return False
    return True


if __name__ == '__main__':
    if prepare(arguments):
        print(os.listdir())
        circuit.analyzer.LoadFolders(arguments.path).start()
