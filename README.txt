importfix: Utilities for fixing Python imports

Put these two lines at the top of your runnable scripts:

import importfix
importfix.fix_imports(__file__)

The fix_imports function walks up the directory structure from the
location of your script file to find the first directory that does
not contain an __init__.py file.  That directory is inserted at the
front of sys.path if it is not already included.
