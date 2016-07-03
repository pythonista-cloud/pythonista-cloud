"""Handles the installation of downloaded modules."""
import cloud.downloader


def install(zip_path, py_versions):
    """Install a module once it has been downloaded locally.

    Takes the path to the downloaded zip file as well as a list of supported
    Python versions.
    """
    raise NotImplementedError()
