# Testing website for the company

### You need to have Mozilla Firefox web browser.
---

## How to run?

**Step 1 (Optional) :** Create virtual environment

``python -m venv venv`` 
or 
``python3 -m venv venv``



``source venv/bin/activate`` - for Linux and Mac

``venv/Scripts/activate.bat`` - for Windows

**Step 2:** Install the requirenments:

``pip install -r requirenments`` 
or 
``pip3 install -r requirenments``

**Step 3:** Run the automated testing script:

``python script.py`` or ``python3 script.py``

### Output can be found on:
1. terminal where you run script
2. in the reports folder

---

## Information about the package and files.
1. ``tests/`` - in the folder where seperate tests can be found
2. ``tests/settings.py`` - file where different kind of configurations.
3. ``tests/utils.py`` - in the file there is BeautifulSoup script which gets links of the page
4. ``webdriver/`` - in the folder firefox drivers can be found
    
    1) ``./webdriver/geckodriver`` - driver for Linux
    2) ``./webdriver/geckodriver.exe`` - driver for Windows
    3) Ps. change settings.py file. ``WEBDRIVER_PATH`` variable
5. ``reports/`` the folder stores html reports for tests after running script.py
6. ``requirements`` file where you can find requirement modules for script

---
## Additional information

You can run each test seperately:

``python ./tests/TestName.py -v``

or

``python3 ./tests/TestName.py -v``
