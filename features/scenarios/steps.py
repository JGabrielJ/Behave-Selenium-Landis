from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


@given("that I'm on the Registration Form page")
def step_go_to_registration_form(context):
    context.driver.get("https://demoqa.com/automation-practice-form")


@when('I complete the form with the correct data')
def step_fill_form_with_correct_data(context):
    # Implemente aqui a lógica para preencher o formulário com dados válidos
    pass


@when('I complete the form with incorrect data')
def step_fill_form_with_incorrect_data(context):
    # Implemente aqui a lógica para preencher o formulário com dados válidos
    pass


@when('I click Submit')
def step_click_submit(context):
    submit = context.driver.find_element(By.ID, "submit")
    submit.send_keys(Keys.RETURN)


@when('I remove a single item present in Subjects')
def step_remove_item_in_subjects(context):
    subjects_input = context.driver.find_element(By.ID, "subjectsInput")
    subjects_input.send_keys("Chemistry")
    subjects_input.send_keys(Keys.RETURN)

    remove_button = context.driver.find_element(By.CLASS_NAME, "css-19bqh2r")
    webdriver.ActionChains(context.driver).click(remove_button).perform()


@when('I leave the Date of Birth field empty')
def step_leave_birthday_empty(context):
    date_of_birth = context.driver.find_element(By.ID, "dateOfBirthInput")
    webdriver.ActionChains(context.driver).click(date_of_birth).perform()
    for _ in range(0, 11):
        date_of_birth.send_keys(Keys.BACKSPACE)


@then('I see a pop-up with filled data')
def step_popup_opened(context):
    popup = context.driver.find_element(By.ID, "example-modal-sizes-title-lg")
    if popup.text == "Thanks for submitting the form":
        print("Data was received correctly")


@then('I see fields in red demanding to be filled out')
def step_popup_closed(context):
    try:
        popup = context.driver.find_element(By.ID, "example-modal-sizes-title-lg")
    except NoSuchElementException:
        print("There are required fields not filled in!")


@then('I see the whole page blank')
def step_check_page_blank(context):
    app = context.driver.find_element(By.ID, "app")
    if app.text == "":
        print("Blank Page")
