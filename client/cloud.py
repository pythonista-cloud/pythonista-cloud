"""pythonista.cloud is the package manager for Pythonista.

This module serves as the main interface.
"""

import sys

from _cloud import module_importer


class CloudHandler(object):
    """Implements custom behavior when running 'from cloud import x'"""
    def __getattr__(self, key):
        """ Add a module named 'key' from the index into your namespace """
        return module_importer.Import(key)

    def __contains__(self, key):
        """ Allows syntax of 'x in cloud' """
        pass


if __name__ != "__main__":
    # This is being imported
    sys.modules[__name__] = CloudImportHandler()
else:
    # This is being run normally
    pass
