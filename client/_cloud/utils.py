"""Various utilities and helper functions used by the pythonista.cloud client
"""

import os


def pick_site_dir(py_versions):
    """ Decide in which site-packages directory a module belongs.

    Takes a list of Python versions that a module supports.
    """
    if len(py_versions) == 1:
        assert py_versions[0] in [2, 3]
        directory = "site-packages-" + str(py_versions[0])
    else:
        directory = "site-packages"
    return os.path.expanduser("~/Documents/{}".format(directory))
