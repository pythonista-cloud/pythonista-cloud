# [pythonista.cloud](http://pythonista.cloud/) [![](https://img.shields.io/badge/Donate-PayPal-brightgreen.svg?style=flat-square)](https://paypal.me/luke0)

pythonista-cloud is intended as an easy solution for installing scripts to Pythonista from GitHub. Initially it will be a service for modules, but will eventually expand to scripts designed to be run directly like utilities and games.

# How it works

## Server-side
**Submission**: First, a user authenticates on the web via GitHub OAuth. The user can then visit a dashboard where they can browse their GitHub repositories and select one at a time to add to the index. When the user selects a repository to add, pythonista-cloud uses the GitHub API to check for the presence of and to download a `pythonista-cloud.json` file in the root of the repository. It will fill in known information (author, repo URL) and will validate the existing information (entry point, name, version number, dependencies, supported Python versions). If all checks pass, it will add the JSON file to the CouchDB index.

## Client interfaces
#### 1. The `cloud` module
The `cloud` module is intended as the quick and easy interface to the index. It has functions for programmatically controlling everything, as well as an import syntax which is very useful for modules.

**All-purpose**: `cloud` will have functions like `download_module` and similar.

**Modules**: For modules in the index, `cloud` handles everything in the background so that all a user has to do is `from cloud import something`. For specific versions, the `cloud.config` function is supported:

	import cloud
	cloud.config(
	    sample="0.1.6"
	)
	from cloud import sample  # version 0.1.6 is imported

Inequalities are supported as well:

	import cloud
	cloud.config(
	    sample=(">=", "0.1.6")
	)
	from cloud import sample  # Any cached version after 0.1.6 can be used

In the background, `cloud` caches different versions of modules. When a script executes`from cloud import something`, `cloud` will ask the server what the latest version of `cloud` is. If this version is cached, `cloud` will use that. Otherwise, it will download and use the latest version. Note that this transaction can take place with a single HTTP request if `cloud` sends the latest installed version as a request header and the server handles the logic of determining if this is the latest version Since `cloud` stores all these module versions, a `cloud.clear_cache` function would make sense.

#### 2. Installer snippets
`installers.pythonista.cloud` will dynamically generate scripts to install certain modules to site-packages, or to install other scripts to Documents. The install scripts will vary only by an inserted variable at the beginning of the script. For example:

	PACKAGE_NAME = "something"
	# All the rest of the code is completely identical regardless of the package. The full JSON file will be downloaded from the server.

The server will shorten the `http://installers.pythonista.cloud/something` links and keep a shortlink with every package. So an actual installer snippet will look something like

	import requests as r; exec(r.get('http://goo.gl/abcdef').text)
These installer scripts will present a UI displaying download progress and displaying options like cancel, etc.

#### 3. An in-app package browser 
There will be a cloud manager UI that users can use from the app. Users will be able to:
- Browse packages and install them
- View installed packages and uninstall either entire packages or specific versions
- (maybe) submit packages if OAuth works in Pythonista, but I suspect this will require a WebView.

#### Web browser
Hooks for installing packages via websites will be included in the `cloud` module. Users of the website will be able to click an "install" button on any package and the URL scheme will be used to activate a script in `site-packages` with arguments including package name and callback URL. Among the tools available to package authors will be copiable HTML and markdown snippets for install buttons.

**Verifying that the `cloud` module is installed**: The install links will be to `install.pythonista.cloud` URLs. This subdomain will be an important intermediary because it will be able to make sure users have `cloud` installed. When users are directed to `install.pythonista.cloud`:
1. The website will check for the presence of a cookie on the user's device.
2. If the cookie is present, the website will redirect the user to the Pythonista app and use the URL scheme to execute the install script
3. If the cookie is *not* present, the user will be prompted to install the `cloud` module by pasting a snippet. This snippet will be a special installer that installs `cloud` and then redirects the user back to a new install page. This second install page will set the cookie, and proceed to installation of the desired package. The snippet will just redirect if the `cloud` module is already installed, so that the cookie is set.

In this way, users only have to copy a snippet once to be able to one-click install scripts forever. The users won't have to know to run the snippet beforehand, they'll be prompted when they try to install. 

## Goals
The hope is that `pythonista-cloud` will grow into a standard widely used by the community.

**Future features**:
- Monetization (?)
	- paid packages
		- encrypted packages that can only be downloaded via a purchase and can't be easily run on other devices
		- packages that are free but closed-source without payment (obfusticated)
	- donations
	- Package authors can pay for access to premium convenience features such as:
		- automatically adding scripts to the wrench menu
		- scripts that are run on startup automatically
		- custom install locations without writing a whole new install script


## Contribute
Pull Requests are more than welcome, as are bug reports.

If you'd like to support this project, please consider a donation via PayPal to cover server costs. You can make a donation [here](https://paypal.me/luke0).
