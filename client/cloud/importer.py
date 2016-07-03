"""Downloads modules via cloud.downloader and returns them.

This might be more complicated later.
"""

import sys

import cloud.installer


def Import(module_name):
    """Return a module object for a module with a given name."""
    # The module is already installed
    if module_name in sys.modules:
        return sys.modules[module_name]
    # The module needs to be installed
    else:
        cloud.installer.install(
            cloud.downloader.download(module_name)
        )
        return __import__(module_name)
