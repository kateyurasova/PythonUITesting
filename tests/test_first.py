from selenium.webdriver import DesiredCapabilities
from testcontainers.selenium import BrowserWebDriverContainer
import pytest
import allure
from strgen import StringGenerator
import logging
import webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from faker import Faker

logger = logging.getLogger('foo')
fake = Faker()


class Test(object):
    @allure.feature('Google test')
    @allure.story('search')
    def test_one(self):
        url = "https://www.google.com/"

        logger.info("WHEN User navigates to the %s" % url)
        browser = BrowserWebDriverContainer(DesiredCapabilities.CHROME)
        browser.get(url)
        assert True == True
