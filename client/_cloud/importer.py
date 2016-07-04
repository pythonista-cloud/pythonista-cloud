"""Downloads modules via cloud.downloader and returns them.

This might be more complicated later.
"""

import sys

from _cloud import downloader, installer


def Import(module_name):
    """Return a module object for a module with a given name."""
    # The module is already installed
    if module_name in sys.modules:
        return sys.modules[module_name]
    # The module needs to be installed
    else:
        installer.install(
            downloader.download(module_name)
        )
        return __import__(module_name)
