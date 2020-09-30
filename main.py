import json
import os
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def log_print(text):
    print(text)


def exit_(message):
    log_print(message)
    exit(1)


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
        print(f"Please create a '{user_file_path}' file, see README.md for details")


def send_keys_by_id(web_driver, id, text):
    # Try 3 times with wait in between, if fails on third allow Exception to raise
    tries = 3
    element = WebDriverWait(web_driver, 10).until(
        expected_conditions.presence_of_element_located((By.ID, id)))
    for i in range(tries - 1):
        if i > 0:
            log_print(f"Retrying send_keys to element with '{id}' (this is attempt {i+1})")
        try:
            element.send_keys(text)
            return
        except ElementNotInteractableException:
            if i == tries - 1:
                raise
            time.sleep(1)



def login(web_driver, user_email, user_password):
    # Login to messenger (wait until elements are added to DOM before interaction

    send_keys_by_id(web_driver, "email", user_email)

    send_keys_by_id(web_driver, "pass", user_password)

    login_button = WebDriverWait(web_driver, 10).until(
        expected_conditions.element_to_be_clickable((By.ID, 'loginbutton')))
    login_button.click()

    # Element with id 'settings' should appear iff login was successful, so check for this
    #       (exit if not found within 10s)
    try:
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, "settings")))
        log_print("Login Successful")
    except TimeoutException:
        exit_("Login failed or timed out, check your credentials.")


if __name__ == '__main__':

    # Read user credentials from file
    (email, password) = get_user_credentials('user.json')

    # Use Chrome to access web
    driver = webdriver.Chrome()

    # Open Facebook messenger
    driver.get('https://www.messenger.com/t/bennetcobley')

    # Perform and verify login
    login(driver, email, password)








