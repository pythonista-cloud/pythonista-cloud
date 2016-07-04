"""The client interface to interact with pythonista.cloud.

minus the import trickery
"""

import sys

from _cloud import downloader, installer


class Module(object):
    """The magical API around downloading / installing /Â importing things."""
    def __init__(self, name):
        self.name = name
        self.downloaded = False

    @property
    def installed(self):
        """Returns whether the module in question has been installed."""
        return self.name in sys.modules

    # Main functions for the import process

    def download(self):
        """Download a module to a BytesIO as a zip file."""
        self._zip, self.metadata = downloader.download(self.name)
        self.downloaded = True
        return True

    def install(self):
        """Install a module from an in-memory zip."""
        installer.install(self._zip, self.metadata)

    def importme(self):
        """Return a module object for this module."""
        return __import__(self.name)
