"""pythonista.cloud is the package manager for Pythonista.

This module serves as the main interface.
"""

import sys

import _cloud

special_cases = {
    # Python stuff. I have no idea what these should actually be, but None
    # seems to work for now.
    "__spec__": None,
    "__path__": None,
    # Other parts of pythonista.cloud
    "config": lambda: exec("raise NotImplementedError('Coming soon!')"),
    "update": lambda: exec("raise NotImplementedError('Coming soon!')")
}


class CloudImportHandler(object):
    """Implements custom behavior when running 'from cloud import x'"""
    def __getattr__(self, key):
        """ Add a module named 'key' from the index into your namespace """
        # There are some cases in which we shouldn't retrieve an actual module
        if key in special_cases:
            return special_cases[key]

        # Install the module, return its contents
        else:
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
