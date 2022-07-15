import argparse
import os

from src import circuit

parser = argparse.ArgumentParser(description="-path: Path to project folder (from first .py file)")
parser.add_argument("-path", dest="path", required=True)
parser.add_argument("-patch", dest="patch")
arguments = parser.parse_args()


def prepare(args: argparse.Namespace) -> bool and dict:
    """
    Prepare for analyze
    :param args: argparse.Namespace
    :return: bool do program need an analysis or path is empty
    """
    if not os.path.exists(args.path):
        raise OSError(f"Path {args.path} doesn't exists. -path param should be the path to your project")

    # Moving to analyze path
    os.chdir(args.path)

    return bool(os.listdir())


if __name__ == '__main__':
    if prepare(arguments):
        folder_tree = circuit.analyzer.LoadFolders(arguments.path).start()
        a = circuit.analyzer.StartProcessing(arguments, folder_tree).start()
        for i in a:
            print(i.to_str())
