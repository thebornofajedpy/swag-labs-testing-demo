import pytest
import logging
import os
from selenium import webdriver

driver = None

@pytest.fixture(scope="class")
def setup(request):
    global driver
    driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(url='https://www.saucedemo.com/')
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(scope="class")
def logger(request):
    full_name = os.environ.get('PYTEST_CURRENT_TEST').split(' ')[0].split('::')[1]
    class_name = request.node.name
    logger = logging.getLogger(f'{full_name}')
    file_handler = logging.FileHandler('../logfile.log')
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s:%(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)  # filehandler object
    logger.setLevel(logging.DEBUG)
    request.cls.log = logger
    logger.info(f"   #### {class_name} SCENARIO STARTED ####")
    yield
    logger.info(f"   #### {class_name} SCENARIO ENDED ####")


@pytest.fixture(
    params=[("", ""), ("standard_user", ""), ("", "secret_sauce"), ("locked_out_user", ""), ("problem_user", ""),
            ("performance_glitch_user", "")])
def invalid_login_data(request):
    return request.param


@pytest.fixture(
    params=[("standard_user", "secret_sauce"), ("problem_user", "secret_sauce"),
            ("performance_glitch_user", "secret_sauce")])
def valid_login_data(request):
    return request.param

@pytest.fixture(params=[("standard_user", "secret_sauce")])
def standard_user_cred(request):
    return request.param
