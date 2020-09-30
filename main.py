import json
import os

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def get_user_credentials(user_file_path):
    if os.path.exists(user_file_path):
        with open(user_file_path, 'r') as json_file:
            try:
                data = json.load(json_file)
                return data['email'], data['password']
            except:
                print(f"Failed to read 'email' and 'password' from '{user_file_path}' file")
                raise
    else:
        print(f"Please create a '{user_file_path}' file")


if __name__ == '__main__':

    # Read user credentials from file
    (user_email, user_password) = get_user_credentials('user.json')

    # Use Chrome to access web
    driver = webdriver.Chrome()

    # Open Facebook messenger
    driver.get('https://www.messenger.com/t/bennetcobley')

    # Login to messenger (wait until elements are added to DOM before interaction
    email_input = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.ID, "email")))
    email_input.send_keys(user_email)

    email_input = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.ID, "pass")))
    email_input.send_keys(user_password)

    login_button = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable((By.ID, 'loginbutton')))
    login_button.click()
