"""pythonista.cloud is the package manager for Pythonista.

This module serves as the main interface.
"""

import sys

import _cloud


class CloudImportHandler(object):
    """Implements custom behavior when running 'from cloud import x'"""
    def __getattr__(self, key):
        """ Add a module named 'key' from the index into your namespace """
        mod = _cloud.Module(key)
        mod.download()
        mod.install()
        return mod.importme()

    def __contains__(self, key):
        """ Allows syntax of 'x in cloud' """
        pass


if __name__ != "__main__":
    # This is being imported
    sys.modules[__name__] = CloudImportHandler()
else:
    # This is being run normally
    pass
