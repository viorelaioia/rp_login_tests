# rp_login_tests
This repository contains automated login tests for Mozilla relying parties (RPs).

Getting involved as a contributor
---------------------------------

We love working with contributors to improve the Selenium test coverage for RPs login tests, but it does require a few skills. 
You will need to be familiar with Python, Selenium, and have a working knowledge of GitHub.

If you are comfortable with Python, it's worth having a look at the Selenium framework to understand the basic concepts of browser-based testing and the page objects pattern.

To brush up on Python skills before engaging with us, Dive Into Python is an excellent resource. MIT also has lecture notes on Python available through their open courseware. The programming concepts you will need to know include functions, working with classes, and the basics of object-oriented programming.

How to set up and run Mozillians tests locally
---------------------------------

### You will need to install the following:
#### Git
Download and install the latest version of Git on all platforms: https://help.github.com/articles/set-up-git/
Set your username in git: https://help.github.com/articles/setting-your-username-in-git/
Set your email address in git: https://help.github.com/articles/setting-your-commit-email-address-in-git/
Fork a Git Repo: https://help.github.com/articles/fork-a-repo/

#### Python
Before you will be able to run these tests you will need to have Python installed (version higher than 2.6.8): https://www.python.org/downloads/.

#### Tox
Tox can be installed by following the instructions from https://tox.readthedocs.io/en/latest/install.html

### Running tests locally
#### Credentials
For passwordless login, we use restmail email address for testing: https://github.com/mozilla/restmail.net.
In order to create a new restmail email address, you just need to call the GET API: "GET /mail/<user>". 
Example: email address "test@restmail.net" springs into existance after calling the GET method  - "GET https://restmail.net.mail/test"
The variables.json file should be copied to a location outside of rp_login_tests and the restmail email address should populate the "passwordless_email" field.

In order to run the tests, you will also need Firefox installed. For Firefox versions higher than 47, geckodriver (https://github.com/mozilla/geckodriver/releases) is required and it should be added to the system path.

The command for running all tests is:
'PYTEST_ADDOPTS="--variables=/path_to_variables.json" tox'

The command for running a single test is:
'PYTEST_ADDOPTS="--variables=/path_to_variables.json" tox -- -k test_name'


Writing tests
-------

The structure of the repository is made of 3 folders:
1. pages - which contains a python file for each mozilla RP that has a test associated. Each class from the python files inherits the Base class and uses method helpers from auth0 class for login purposes.
2. requirements - which contains pytest plugins to be used by the tests
3. tests - which contains test methods for mozilla RPs defined in pages folder
