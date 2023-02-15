import argparse
from typing import List
from pathlib import Path


def check_python_init_files(arguments: List[str]):
    init_file_paths = set([Path(arg).parent.resolve() / "__init__.py" for arg in arguments if arg.endswith(".py")])

    for init_file_path in init_file_paths:
        if not init_file_path.exists():
            init_file_path.touch()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args()

    check_python_init_files(args.filenames)


if __name__ == "__main__":
    main()
