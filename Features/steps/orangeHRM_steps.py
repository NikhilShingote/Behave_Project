from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('launch chrome browser')
def launchBrowser(context):
    serv_obj = Service("C:\Drivers\chromedriver.exe")
    context.driver = webdriver.Chrome(service=serv_obj)


@when('open orangehrm homepage')
def openHomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@then('verify that the logo present on page')
def verifyLogo(context):
    my_wait = WebDriverWait(context.driver, 10)
    # status = context.driver.find_element(By.XPATH, "//img[@alt='company-branding']").is_displayed()
    status = my_wait.until(EC.presence_of_element_located((By.XPATH, "//img[@alt='company-branding']"))).is_displayed()
    assert status is True


@then('close browser')
def closeBrowser(context):
    context.driver.close()
