from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from options import nms_connection_options

def nms_login(driver):
    driver.get(nms_connection_options()[1])
    login = driver.find_element_by_id("login[login]")
    login.send_keys("admin")
    password = driver.find_element_by_id("login[password]")
    password.send_keys("12345")
    password.send_keys(Keys.RETURN)


def get_element_id(driver, selector):
    return WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, selector))
    )

def get_element_xpath(driver, selector):
    return WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.XPATH, selector))
    )

