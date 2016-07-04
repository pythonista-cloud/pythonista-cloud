"""The client interface to interact with pythonista.cloud.

minus the import trickery
"""

import sys

from _cloud import downloader, installer


class CloudModule(object):
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
        self.metadata, self._zip = downloader.download(self.name)
        self.downloaded = True
        return True

    def install(self):
        """Install a module from an in-memory zip."""
        installer.install(self.metadata, self._zip)

    def importme(self):
        return __import__(self.name)
