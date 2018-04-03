import time

from behave import *

@given('the page is loaded')
def step_impl(context):
    context.browser.get('https://www.tumblr.com')

@when('I click on log in button')
def step_impl(context):
    context.browser.find_element_by_css_selector(
        '[id="signup_login_button"]'
    ).click()
    time.sleep(2)

@when('I fill in username')
def step_impl(context):
    context.browser.find_element_by_css_selector(
        '[id="signup_determine_email"]'
    ).send_keys('iwosub@gmail.com')
    context.browser.find_element_by_css_selector(
        '[id="signup_forms_submit"]'
    ).click()
    time.sleep(2)

@when('I fill in password')
def step_impl(context):
    context.browser.find_element_by_css_selector(
        '[id="signup_password"]'
    ).send_keys('grobdrob')

@when('I submit the data')
def step_impl(context):
    context.browser.find_element_by_css_selector(
        '.signup_login_btn'
    ).click()
    time.sleep(2)

@then('I am logged user')
def step_impl(context):
    context.browser.find_element_by_css_selector(
        '[id="new_post_notice_container"]'
    )