from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('I launch the chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()


@when('I open orangeHRM page')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


# Passing username and password as parameters

@when('Enter username "<username>" and password "<password>"')
def step_impl(context, user, pwd):
    context.driver.implicitly_wait(5)
    context.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(user)
    context.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(pwd)


@when('click the Login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()


@then('User must successfully login and go to Dashboard page')
def step_impl(context):
    try:
        text = context.driver.find_element(By.XPATH,"//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']").text

    except:
        context.driver.close()
        assert False, "Test Failed Unsuccessful Login"

    if text == "Dashboard":
        context.driver.close()
        assert True, "Test Passed Successful Login"
