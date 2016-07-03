"""Handles the fetching of modules.

First queries the index at db.pythonista.cloud, then downloads the modules as
zip files via GitHub.
"""


def download(module_name):
    """Download a zip archive for a remote module."""
    raise NotImplementedError()
    # Something...
    return DownloadedModule(extracted_path, metadata)
