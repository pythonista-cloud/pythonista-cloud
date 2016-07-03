"""Handles the fetching of modules.

First queries the index at db.pythonista.cloud, then downloads the modules as
zip files via GitHub.
"""


class DownloadedModule(object):
    """A class to store basic information about a downloaded module.
    
    Stores the path to a downloaded zip file, as well as metadata like GitHub
    URL and supported Python versions.
    """
    def __init__(self, zip_path, metadata):
        self.zip_path = zip_path
        for i in metadata:
            setattr(self, i, metadata[i])

def download(module_name):
    """Download a zip archive for a remote module."""
    
    return DownloadedModule(extracted_path, metadata)
