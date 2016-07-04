# [pythonista.cloud](http://pythonista.cloud/)
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
  - [ ] Allow downloading files through standard import interface (`from cloud import my_module`)
  - [ ] Store a `~/cloud.json` file to track package metadata, because nobody looks above `~/Documents`.
### For later releases
`pythonista.cloud` will expand into a larger service. It will, like `npm`, track package versions, descriptions of packages, and more.

#### A non-exhaustive list of planned features for the longer-term future
Sorted roughly by order of planned implementation

1. **User login system**: Turn `pythonista.cloud` into a full platform with user accounts, etc. through GitHub OAuth. This will allow things like removing packages to take place without contacting me.
  - Each package is tied to a user
  - Package analytics
  - Delete packages
2. **Basic update system**: the `cloud.update("my_module")` method will retrieve `my_module` from the index, then check the GitHub repo for new releases. If the latest release is beyond the release version stored in `~/cloud.json`, the new version will be downloaded and installed.
3. **Easy installers**: `pythonista.cloud` will be able to generate short snippets like
```python
import requests as r; exec(r.get("http://i.pythonista.cloud/livejson"))
```
to install modules

## Contribute
Pull Requests are more than welcome, as are bug reports.

If you'd like to support this project, please consider a donation via PayPal to cover server costs:

[![PayPal Donation](https://www.paypalobjects.com/webstatic/mktg/logo/bdg_now_accepting_pp_2line_w.png)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=Z6PB7YRG6PBN4&lc=US&currency_code=USD)
