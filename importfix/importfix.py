"""Utilities for "fixing" Python imports."""


def fix_imports(file_path):
    """Walks up the directory hierarchy to find the appropriate path to add to PYTHONPATH.

    The first directory that does not contain an __init__.py file is the chosen directory. When you call this function,
    you usually pass in __file__ as the argument:

        import importfix
        importfix.fix_imports(__file__)

    These two lines can be used as the first two lines of a script file.

    :param file_path: The path of a file in a Python package. Usually this argument is given as __file__.
    """
    from os.path import abspath, dirname, isfile, join
    import sys

    directory = dirname(abspath(file_path))
    while isfile(join(directory, '__init__.py')):
        directory = abspath(join(directory, '..'))
    if directory not in sys.path:
        sys.path.insert(0, directory)
