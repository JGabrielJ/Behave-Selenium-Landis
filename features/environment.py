from selenium import webdriver


def before_all(context):
    context.driver = webdriver.Edge()


def after_all(context):
    context.driver.close()
