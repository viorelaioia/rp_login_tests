# rp_login_tests
This repository contains automated login tests for Mozilla relying parties (RPs).

Getting involved as a contributor
---------------------------------

We would love to have contributors helping us to improve the Selenium test coverage for RPs login tests. 
In order to do that, we require a few skills. You will need to be familiar with Python, Selenium, and have a working knowledge of GitHub.

If you are comfortable with Python, it's worth having a look at the Selenium framework to understand the basic concepts of browser-based testing and the page objects pattern.

To brush up on Python skills before engaging with us, Dive Into Python is an excellent resource. The programming concepts you will need to know include functions, working with classes, and the basics of object-oriented programming.

How to set up and run Mozillians tests locally
---------------------------------

### You will need to install the following:
#### Git
Download and install the latest version of Git on all platforms: https://help.github.com/articles/set-up-git/ <br>
Set your username in git: https://help.github.com/articles/setting-your-username-in-git/ <br>
Set your email address in git: https://help.github.com/articles/setting-your-commit-email-address-in-git/ <br>
Fork a Git Repo: https://help.github.com/articles/fork-a-repo/ <br>

#### Python
Before you will be able to run these tests you will need to have Python installed (version higher than 2.6.8). You can download Python from https://www.python.org/downloads/, where you can also find installation instructions for your platform.

#### Tox
Tox can be installed by following the instructions from https://tox.readthedocs.io/en/latest/install.html

### Running tests locally
#### Credentials
For passwordless login, we use restmail email address for testing: https://github.com/mozilla/restmail.net. <br>
In order to create a new restmail email address, you just need to call the GET API: "GET /mail/<user>".  <br>
Example: email address "test@restmail.net" springs into existance after calling the GET method  - "GET https://restmail.net.mail/test" <br>
The variables.json file should be copied to a location outside of rp_login_tests and the restmail email address should populate the "passwordless_email" field. <br>

In order to run the tests, you will also need Firefox, which can be downloaded and installed from https://www.mozilla.org/firefox/. It is recommended that you install the latest release to the default location.<br>
In order to automate Firefox, the latest GeckoDriver binary should be downloaded for your platform from https://github.com/mozilla/geckodriver/releases and placed into your system path. The following resources may help here:
    <li>[How to edit your system path in Windows](https://www.howtogeek.com/118594/how-to-edit-your-system-path-for-easy-command-line-access/)
    <li>[How to add a new path to PATH the right way on OS X](http://osxdaily.com/2014/08/14/add-new-path-to-path-command-line/)
    <li>[Understanding environment variables and the Unix path](https://cbednarski.com/articles/understanding-environment-variables-and-the-unix-path/)

The command for running all tests is:
`PYTEST_ADDOPTS="--variables=/path_to_variables.json" tox`

The command for running a single test is:
`PYTEST_ADDOPTS="--variables=/path_to_variables.json" tox -- -k test_name`


Writing tests
-------

The structure of the repository is made of 3 folders:
1. pages - which contains a python file for each mozilla RP that has a test associated. Each class from the python files inherits the Base class and uses method helpers from auth0 class for login purposes.
2. requirements - which contains Python package dependencies:   
    [pytest-selenium](https://pypi.python.org/pypi/pytest-selenium/) - plugin was for browser provisioning<br>
    [pytest-variables](https://pypi.python.org/pypi/pytest-variables/) - plugin that allows to store credentials in a private JSON file (variables.json) that can be simply referenced from the command line
    [flake8](https://pypi.python.org/pypi/flake8) - tool for style guide enforcement
3. tests - which contains test methods for mozilla RPs defined in pages folder
