from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge()
driver.get("https://demoqa.com/automation-practice-form")

first_name = driver.find_element(By.ID, "firstName")
first_name.send_keys("John")

last_name = driver.find_element(By.ID, "lastName")
last_name.send_keys("Silva")

user_email = driver.find_element(By.ID, "userEmail")
user_email.send_keys("john.silva67@selenium.com")

gender_radio = driver.find_element(By.ID, "gender-radio-1")
webdriver.ActionChains(driver).click(gender_radio).perform()

user_number = driver.find_element(By.ID, "userNumber")
user_number.send_keys("8590716243")

date_of_birth = driver.find_element(By.ID, "dateOfBirthInput")
webdriver.ActionChains(driver).click(date_of_birth).perform()
for _ in range(0, 10):
    date_of_birth.send_keys(Keys.BACKSPACE)
date_of_birth.send_keys("6 Jul 2002")

subjects_input = driver.find_element(By.ID, "subjectsInput")
subjects_input.send_keys("Computer Science")
subjects_input.send_keys(Keys.RETURN)

hobbies_checkbox_2 = driver.find_element(By.ID, "hobbies-checkbox-2")
webdriver.ActionChains(driver).click(hobbies_checkbox_2).perform()

hobbies_checkbox_3 = driver.find_element(By.ID, "hobbies-checkbox-3")
webdriver.ActionChains(driver).click(hobbies_checkbox_3).perform()

upload_picture = driver.find_element(By.ID, "uploadPicture")
upload_picture.send_keys("C:/Users/gjaci/PycharmProjects/Behave-Selenium/features/test.feature")

current_address = driver.find_element(By.ID, "currentAddress")
current_address.send_keys("Aggarwal Marg, 205")

select_state = driver.find_element(By.ID, "react-select-3-input")
webdriver.ActionChains(driver).click(select_state).perform()
select_state.send_keys("NCR")
select_state.send_keys(Keys.RETURN)

select_city = driver.find_element(By.ID, "react-select-4-input")
webdriver.ActionChains(driver).click(select_city).perform()
select_city.send_keys("Delhi")
select_city.send_keys(Keys.RETURN)

submit = driver.find_element(By.ID, "submit")
submit.send_keys(Keys.RETURN)

sleep(15)
driver.close()


# def before_all(context):
#     context.driver = webdriver.Edge()
#
#
# def after_all(context):
#     context.driver.close()
