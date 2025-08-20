import code_analyzer as ca

import os
import argparse

# FIXME -> should add this?
# maybe save code in a cache file?
def analyze_python_code(code):
    pass
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze Python files or code")
    parser.add_argument(
        "--path",
        type=str,
        default=".",
        help="Folder containing Python files to analyze OR a path to a python/notebook file."
    )
    parser.add_argument(
        "--name",
        type=str,
        default="My Awesome Project",
        help="Name of your project."
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        default=True,
        help="Print analyzing results."
    )
    parser.add_argument(
        "--save",
        action="store_true",
        default=True,
        help="Saving Analyzis results into a file."
    )
    parser.add_argument(
        "--save_path",
        type=str,
        action="store_true",
        default="./",
        help="Folderpath for the saving."
    )
    args = parser.parse_args()

    analyze_python_files(args.path)
    ca.analyse_code(args.path, name=args.name, should_print=args.verbose, should_save=args.save, save_path=args.save_path)

