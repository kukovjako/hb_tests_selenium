# Test suite for HomeBuddy /siding page
### Using Pytest, Selenium, Allure

### First, clone project

Then:
```
> python3 -m venv env
> source env/bin/activate
> pip install -r requirements.txt
```

To run tests:
```
> pytest --alluredir=report_dir . -vv -s
```
Tests are running headless.

### To see the Allure test report:
Install Allure, using Homebrew:
```
> brew install allure 
```
Run report using:
```
> allure serve report_dir
```
### Or, install Allure on WINDOWS using Scoop:
First, install the Scoop command-line installer
In a PoweShell terminal:
```
> Set-ExecutionPolicy RemoteSigned -Scope CurrentUser # Optional: Needed to run a remote script the first time
> irm get.scoop.sh | iex
```
Then:
```
> scoop install allure
```
After that we can run the report:
```
> allure serve report_dir
```