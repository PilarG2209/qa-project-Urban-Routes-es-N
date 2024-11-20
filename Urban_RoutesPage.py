from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import Locators
import data
from selenium.webdriver.support import expected_conditions

from SMS import retrieve_phone_code

detail_route_XPATH= None

class UrbanRoutesPage:

  def __init__(self, driver):
        self.driver = driver

def set_from(self, from_address):
    self.driver.find_element(*self.from_field).send_keys(from_address)

def set_to(self, to_address):
    self.driver.find_element(*self.to_field).send_keys(to_address)

def set_route(self, from_address, to_address):
    self.set_from(from_address)
    self.set_to(to_address)

def get_from(self):
    return self.driver.find_element(*self.from_field).get_property('value')

def get_to(self):
    return self.driver.find_element(*self.to_field).get_property('value')

def select_taxi_button(self):
    self.driver.implicitly_wait(30)
    self.driver.find_element(*self.select_taxi).click()

def select_comfort_rate(self):
    self.driver.implicitly_wait(30)
    self.driver.find_element(*self.comfort_button).click()

def select_number_button(self):
    self.driver.implicitly_wait(30)
    self.driver.find_element(*self.select_phone_insert).click()

def add_phone_number(self):
    self.driver.implicitly_wait(30)
    self.driver.find_element(*self.number).send_keys(data.phone_number)

def set_phone(self):
    self.driver.implicitly_wait(30)
    self.select_number_button()
    self.driver.implicitly_wait(30)
    self.add_phone_number()

def the_next_button(self):
    self.driver.implicitly_wait(20)
    self.driver.find_element(*self.next_button).click()

def send_cell_info(self):
    self.driver.implicitly_wait(30)
    self.driver.find_element(*self.cell_next).click()

def get_phone(self):
    return self.driver.find_element(*self.phone_input).get_property('value')

def code_click(self):
    self.driver.find_element(*self.click_code).click()

def code_number(self):
    self.driver.implicitly_wait(20)
    phone_code = retrieve_phone_code(driver=self.driver)
    self.driver.implicitly_wait(20)
    self.driver.find_element(*self.code).send_keys(phone_code)

def get_code(self):
    return self.driver.find_element(*self.code).get_property('value')

def pay_click(self):
    self.driver.implicitly_wait(30)
    self.driver.find_element(*self.payment_method).click()

def add_click(self):
    self.driver.implicitly_wait(30)
    self.driver.find_element(*self.card_add_button).click()

def click_card(self):
    self.driver.implicitly_wait(30)
    self.pay_click()
    self.driver.implicitly_wait(30)
    self.add_click()

def number_click(self):
    self.driver.implicitly_wait(20)
    self.driver.find_element(*self.credit_click).click()

def number_input(self):
    self.driver.implicitly_wait(20)
    self.driver.find_element(*self.add_credit_card).send_keys(data.card_number)

def card_input(self):
    self.driver.implicitly_wait(20)
    self.number_click()
    self.driver.implicitly_wait(20)
    self.number_input()

def get_card_input(self):
    return self.driver.find_element(*self.add_credit_card).get_property('value')

def cvv_add(self):
    self.driver.implicitly_wait(30)
    self.driver.find_element(*self.card_cvv).click()

def code_card_input(self):
    self.driver.implicitly_wait(30)
    self.driver.find_element(*self.card_cvv).send_keys(data.card_code)

def cvv_code(self):
    self.driver.implicitly_wait(20)
    self.code_card_input()

def get_cvv_card(self):
    return self.driver.find_element(*self.card_cvv).get_property('value')

def registered_card(self):
    self.driver.implicitly_wait(30)
    self.driver.find_element(*self.agree_card).click()

def add_card(self):
    self.driver.implicitly_wait(30)
    self.card_input()
    self.driver.implicitly_wait(30)
    self.cvv_code()
    self.driver.implicitly_wait(30)
    self.registered_card()

def close_window(self):
    self.driver.implicitly_wait(30)
    self.driver.find_element(*self.x_button).click()

def write_drive_message(self, message):
    self.driver.implicitly_wait(20)
    message_field = self.driver.find_element(*self.driver_message)
    message_field.send_keys(message)

def get_message(self):
    return self.driver.find_element(*self.driver_message).get_property('value')

def request_blanket_and_tissues(self):
    self.driver.implicitly_wait(20)
    self.driver.find_element(*self.blanket_and_scarves).click()

def get_blanket_and_scarves(self):
    return self.driver.find_element(*self.blanket_and_scarves).get_property('value')

def request_ice_cream(self):
    self.driver.implicitly_wait(20)
    self.driver.find_element(*self.ice_cream_counter).click()
    self.driver.find_element(*self.ice_cream_counter).click()

def get_ice_cream(self):
    return self.driver.find_element(*self.ice_cream_counter).get_property('value')

def search_taxi(self):
    self.driver.implicitly_wait(20)
    self.driver.find_element(*self.taxi_search_button).click()

def get_taxi(self):
    return self.driver.find_element(*self.taxi_search_button).get_property('value')

def wait_for_driver_info(self):
    self.driver.implicitly_wait(120)
    self.driver.find_element(*self.modal_taxi)
    self.driver.implicitly_wait(120)
