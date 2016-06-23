# [pythonista.cloud](http://pythonista.cloud/)
A module for easily accessing public community Pythonista modules by downloading them automatically.

## Project Structure + Tasklist

- Server
  - [ ] Allow uploading of files
    - [ ] **Short term**: Upload URLs
    - [ ] **Long term**: Upload entire files and packages via POST requests (upload to `https://gist.github.com`?)
  - [ ] Allow retrieving files
    - Return data with `Content-Type` header
      - `application/x-gzip` for `.tar.gz` files, used to distribute multi-file packages
      - `text/plain` for single-file modules

- Client
  - [ ] Allow downloading files through standard import interface
    - `from cloud import my_module`
  - [ ] Allow installing from PyPI
    - `from cloud.pypi import my_module`
