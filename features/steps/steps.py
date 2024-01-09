from time import sleep
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
    first_name = context.driver.find_element(By.ID, "firstName")
    first_name.send_keys("John")
    sleep(1)

    last_name = context.driver.find_element(By.ID, "lastName")
    last_name.send_keys("Silva")
    sleep(1)

    user_email = context.driver.find_element(By.ID, "userEmail")
    user_email.send_keys("john.silva67@selenium.com")
    sleep(1)

    gender_radio = context.driver.find_element(By.ID, "gender-radio-1")
    webdriver.ActionChains(context.driver).click(gender_radio).perform()
    sleep(1)

    user_number = context.driver.find_element(By.ID, "userNumber")
    user_number.send_keys("8590716243")
    sleep(1)

    date_of_birth = context.driver.find_element(By.ID, "dateOfBirthInput")
    webdriver.ActionChains(context.driver).click(date_of_birth).perform()

    for _ in range(0, 10):
        date_of_birth.send_keys(Keys.BACKSPACE)

    date_of_birth.send_keys("6 Jul 2002")
    date_of_birth.send_keys(Keys.RETURN)
    sleep(1)

    subjects_input = context.driver.find_element(By.ID, "subjectsInput")
    subjects_input.send_keys("Computer Science")
    subjects_input.send_keys(Keys.RETURN)
    sleep(1)

    hobbies_checkbox_2 = context.driver.find_element(By.ID, "hobbies-checkbox-2")
    webdriver.ActionChains(context.driver).click(hobbies_checkbox_2).perform()
    sleep(1)

    hobbies_checkbox_3 = context.driver.find_element(By.ID, "hobbies-checkbox-3")
    webdriver.ActionChains(context.driver).click(hobbies_checkbox_3).perform()
    sleep(1)

    upload_picture = context.driver.find_element(By.ID, "uploadPicture")
    upload_picture.send_keys("C:/Users/gjaci/PycharmProjects/Behave-Selenium/features/test.feature")
    sleep(1)

    current_address = context.driver.find_element(By.ID, "currentAddress")
    current_address.send_keys("Aggarwal Marg, 205")
    sleep(1)

    select_state = context.driver.find_element(By.ID, "react-select-3-input")
    select_state.send_keys("NCR")
    select_state.send_keys(Keys.RETURN)
    sleep(1)

    select_city = context.driver.find_element(By.ID, "react-select-4-input")
    select_city.send_keys("Delhi")
    select_city.send_keys(Keys.RETURN)
    sleep(1)


@when('I complete the form with incorrect data')
def step_fill_form_with_incorrect_data(context):
    first_name = context.driver.find_element(By.ID, "firstName")
    first_name.send_keys("Aeeee")
    sleep(1)

    last_name = context.driver.find_element(By.ID, "lastName")
    last_name.send_keys("Casinooo")
    sleep(1)

    user_email = context.driver.find_element(By.ID, "userEmail")
    user_email.send_keys("lol_kkkkkkk_lmao")
    sleep(1)

    user_number = context.driver.find_element(By.ID, "userNumber")
    user_number.send_keys("007-1962")
    sleep(1)

    current_address = context.driver.find_element(By.ID, "currentAddress")
    current_address.send_keys("Testando se o Forms aceita qualquer coisa...")
    sleep(1)


@when('I click Submit')
def step_click_submit(context):
    submit = context.driver.find_element(By.ID, "submit")
    submit.send_keys(Keys.RETURN)


@when('I remove a single item present in Subjects')
def step_remove_item_in_subjects(context):
    subjects_input = context.driver.find_element(By.ID, "subjectsInput")
    subjects_input.send_keys("Chemistry")
    subjects_input.send_keys(Keys.RETURN)
    sleep(1)

    remove_button = context.driver.find_element(By.CLASS_NAME, "css-19bqh2r")
    webdriver.ActionChains(context.driver).click(remove_button).perform()
    sleep(1)


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
    sleep(5)


@then('I see fields in red demanding to be filled out')
def step_popup_closed(context):
    try:
        popup = context.driver.find_element(By.ID, "example-modal-sizes-title-lg")
    except NoSuchElementException:
        print("There are required fields not filled in!")
    sleep(5)


@then('I see the whole page blank')
def step_check_page_blank(context):
    app = context.driver.find_element(By.ID, "app")
    if app.text == "":
        print("Blank Page")
    sleep(5)
