"""Handles the fetching of modules.

First queries the index at db.pythonista.cloud, then downloads the modules as
zip files via GitHub.
"""
import io
import os

import requests

from _cloud import utils

# The index from which we fetch modules. This points to a CouchDB database, not
# an entire CouchDB instance.
INDEX_URL = "http://db.pythonista.cloud/"


def fetch_from_index(module_name):
    """Fetch details about a module from the db.pythonista.cloud index."""
    url = os.path.join(INDEX_URL, module_name)
    req = requests.get(url)
    req.raise_for_status()  # Raise an error if any occured
    module_data = req.json()
    return module_data


def download(module_name):
    """Download a zip archive for a remote module."""
    metadata = fetch_from_index(module_name)
    url = metadata["url"]
    zip_url = os.path.join(url, "archive/master.zip")
    req = requests.get(zip_url)
    bytes = io.BytesIO(req.content)

    return metadata, bytes
