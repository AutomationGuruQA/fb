import time

import pytest
from Common.browsersetup import launch_browser
import sys
import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the project directory to sys.path
project_dir = os.path.join(current_dir, "..")
sys.path.insert(0, project_dir)


@pytest.mark.smoke
@pytest.mark.login
def test_login(launch_browser):
    print("\nIn test_login")
    time.sleep(10)
    assert 4==4

@pytest.mark.regression
@pytest.mark.login
def test_login_negative(launch_browser):
    print("\nIn test_login")
    time.sleep(10)
    assert (4==4)

@pytest.mark.regression
@pytest.mark.login
def test_login_negative1(launch_browser):
    print("\nIn test_login")
    time.sleep(10)
    assert 4==4