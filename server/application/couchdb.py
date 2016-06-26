import os
import urllib.parse

import jsonschema
import requests


# GLOBALS

COUCH_URL = "http://localhost:5984/"
MAIN_DB = "pythonista-cloud"

PACKAGE_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "url": {"type": "string"},
        "py_versions": {
            "type": "array",
            "items": {
                "type": "integer"
            }
        }
    },
    "required": [
        "name",
        "url"
    ]
}
PACKAGE_VALID_KEYS = PACKAGE_SCHEMA["properties"].keys()


def _add_document(name, data, database=MAIN_DB):
    """ Add a document to a database """
    return requests.put(
        os.path.join(COUCH_URL, database, name),
        json=data,
        headers={"Content-Type": "application/json"}
    )


def validate_package(info):
    """ Verify that package JSON is valid """
    # Confirm general structure and types
    jsonschema.Draft4Validator(PACKAGE_SCHEMA).validate(info)
    url = info["url"]

    # Confirm the GitHub URL
    parts = urllib.parse.urlparse(url)
    if (parts.scheme not in ("https", "http") or
            parts.netloc not in ("github.com", "www.github.com") or
            len(parts.path.strip("/").split("/")) != 2):
        raise ValueError("That's not a GitHub repo!")
    r = requests.get(url)
    r.raise_for_status()


def strip_package(info):
    """ Remove suprerfluous keys from package JSON """
    return {k: v for k, v in info.items() if k in PACKAGE_VALID_KEYS}


def add_package(info):
    """ Add a package to the database from JSON """
    name = info["name"]

    info = strip_package(info)
    validate_package(info)  # This will raise an error if anything is wrong

    if "py_versions" not in info:
        info["py_versions"] = [2, 3]

    _add_document(name, info).raise_for_status()  # If there's an error, throw
    return True
