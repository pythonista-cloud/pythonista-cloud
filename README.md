# [pythonista.cloud](http://pythonista.cloud/) [![](https://img.shields.io/badge/Donate-PayPal-brightgreen.svg?style=flat-square)](https://paypal.me/luke0)
A module for easily accessing public community Pythonista modules by downloading them automatically.

## Project Roadmap
### For initial release
For the initial release, I'll keep things very basic. The server will have as little involvement as possible, and serve purely as an index.
- **Server**
  - [ ] Allow package submission
    - `POST` to some JSON API on `pythonista.cloud`
    - Packages exist as JSON
      - Stores GitHub URL
      - Stores supported Python versions, to determine whether to install into `site-packages`, `site-packages-2`, or `site-packages-3`
    - Upload URL to package, not package files. URL should be to a GitHub repo.
  - [x] Allow retrieving package info
    - This just happens through CouchDB (free http interfaces ftw!)
- **Client**
  - [x] Allow downloading files through standard import interface (`from cloud import my_module`)
  - [ ] Cache modules
  - [ ] Allow updating methods

### For later releases
`pythonista.cloud` will expand into a larger service. It will track package versions, descriptions of packages, and more.

#### A non-exhaustive list of planned features for the longer-term future
Sorted roughly by order of planned implementation

1. **Module versions**: `cloud` will be able to handle multiple cached versions of modules and install different versions. Module versions will be pulled from GitHub. As far as code, this will work like so:
  ```python
  import cloud
  cloud.config(
      livejson=("==", "1.6.2"),
      stash=(">=", "0.5")
  )
  from cloud import livejson  # imports version 1.6.2
  ```
  This will involve several internal restructurings.
  - Modules will be stored in the `~/cloud/modules` directory.
    - multiple versions of packages will be installed, with names like `livejson1.6.2.py`.
    - `from cloud import` will handle returning the correct module based on your configuration. By default, `cloud` will return the latest version installed.

2. **User login system**: Turn `pythonista.cloud` into a full platform with user accounts, etc. through GitHub OAuth. This will allow things like removing packages to take place without contacting me.
  - Each package is tied to a user
  - Package analytics
  - Delete packages
3. **Easy installers**: `pythonista.cloud` will be able to generate short snippets like
```python
import requests as r; exec(r.get("http://i.pythonista.cloud/livejson"))
```
to install modules

## Contribute
Pull Requests are more than welcome, as are bug reports.

If you'd like to support this project, please consider a donation via PayPal to cover server costs. You can make a donation [here](https://paypal.me/luke0).
