"""Handles the fetching of modules.

First queries the index at db.pythonista.cloud, then downloads the modules as
zip files via GitHub.
"""
import os

import requests

from _cloud import utils

# The index from which we fetch modules. This points to a CouchDB database, not
# an entire CouchDB instance.
INDEX_URL = "http://db.pythonista.cloud/"


class DownloadedModule(object):
    """A class to store basic information about a downloaded module.

    Stores the path to a downloaded zip file, as well as metadata like GitHub
    URL and supported Python versions.
    """
    def __init__(self, zip_path, metadata):
        self.zip_path = zip_path
        for i in metadata:
            setattr(self, i, metadata[i])


def fetch_from_index(module_name):
    """Fetch details about a module from the db.pythonista.cloud index."""
    url = os.path.join(INDEX_URL, module_name)
    req = requests.get(url)
    req.raise_for_status()  # Raise an error if any error occured
    module_data = req.json()
    return module_data


def download(module_name):
    """Download a zip archive for a remote module."""
    # etc.
    return DownloadedModule(extracted_path, metadata)

if __name__ == "__main__":
    print(fetch_from_index("livejson"))
