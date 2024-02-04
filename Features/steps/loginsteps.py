from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By



@given('I launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()


@when('I open orangehrm homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


# Passing username and password as parameters

@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.implicitly_wait(10)
    context.driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys(user)
    context.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(pwd)


@when('click on login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()


@then('User must successfully login to the dashboard page')
def step_impl(context):
    text = context.driver.find_element(By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']").text
    assert text == "Dashboard"
    context.driver.close()

