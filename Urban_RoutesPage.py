from typing import Tuple
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v129.browser import close
from selenium.webdriver.support.wait import WebDriverWait
import data
from selenium.webdriver.support import expected_conditions
from SMS import retrieve_phone_code
detail_route_XPATH= None
class UrbanRoutesPage:


    from_address = (By.ID, 'from')
    to_address = (By.ID, 'to')
    call_taxi_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    comfort = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[2]')
    phone_number_field = (By.CLASS_NAME, "np-button")
    phone_number_input = (By.ID, "np-text")
    phone_number_section = (By.XPATH, 'section active"><button class')
    close_button = (By.CLASS_NAME, 'close-button')
    number = (By.XPATH, '//*[@id="phone"]')
    next_button = (By.XPATH, '//*[text()="Siguiente"]')
    click_code = (By.ID, 'code_input')
    phone_code = (By.ID, 'code') #codigo de comprobacion SMS
    confirm_button = (By.XPATH,'//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]') #Botón confirmar
    phone_send_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')
    select_taxi = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    payment_method_select = (By.CLASS_NAME, 'pp-text') #Metodo de pago
    current_payment_method = (By.CLASS_NAME, 'pp-value-text')
    add_card = (By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]')  #agregar tarjera
    number_card_input = (By.ID,"number")# número de tarjeta
    code_card_input = (By.NAME,"code") #codigo de tarjeta
    click_add_card = (By.CLASS_NAME,"card-wrapper") # click pantalla agregar tarjeta
    add_button = (By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')  # agregar
    close_button_payment_method = (By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[1]/button')  #cerrar boton metodo de pago
    message_for_driver = (By.ID, 'comment') #Mensaje
    reqs_body = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]')#Cuerpo del requerimiento
    reqs_button = (By.CLASS_NAME, 'reques head') #Botón
    blanket_and_scarves = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span') #pañuelos y mantas
    ice_cream = (By.CLASS_NAME, 'counter-plus') #Solicitud de helado
    counter_value = (By.CLASS_NAME, 'counter-value') #contador
    quantity_2 = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')
    order_number = (By.ID, "number>h_180")
    taxi_search_button = (By.CLASS_NAME, "smart-button")
    Button_x = (By.XPATH, '//*[@id="root"]/div/div[5]/div[2]/div[2]/div[1]/div[2]/div')


    def __init__(self, driver):
        self.imput_add_card_code = None
        self.imput_add_card_number = None
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_address).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_address).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_address).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_address).get_property('value')

    def set_route(self,address_from,address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def click_call_taxi_button(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.call_taxi_button))
        self.driver.find_element(*self.call_taxi_button).click()

    def select_comfort_rate(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*self.comfort).click()

    def select_number_button(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*self.phone_number_field).click()

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
        self.driver.find_element(*self.confirm_button).click()

    def get_phone(self):
        return self.driver.find_element(*self.phone_number_input).text

    def code_click(self):
        self.driver.find_element(*self.click_code).click()

    def code_number(self):
        self.driver.implicitly_wait(30)
        phone_code = retrieve_phone_code(driver=self.driver)
        self.driver.implicitly_wait(30)
        self.driver.find_element(*self.phone_code).send_keys(phone_code)

    def pay_click(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*self.payment_method_select).click()

    def add_click(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*self.add_card).click()

    def click_card(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*self.number_card_input).click()
        self.driver.find_element(*self.number_card_input).send_keys("1234 4321 1408")

    def add_code_card(self):
        self.driver.find_element(*self.code_card_input).click()
        self.driver.find_element(*self.code_card_input).send_keys("12"+Keys.TAB)

    def card_submit_button(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*self.add_button).click()

    def close_button_payment(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*self.close_button_payment_method).click()

    def write_drive_message(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*self.message_for_driver).send_keys('traiga una aperitivo')

    def get_message(self):
        return self.driver.find_element(*self.message_for_driver).get_property('value')

    def request_blanket_and_tissues(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*self.blanket_and_scarves).click()

    def request_ice_cream(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*self.ice_cream).click()
        self.driver.find_element(*self.counter_value)
        self.driver.find_element(*self.quantity_2).click()

    def search_taxi(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*self.taxi_search_button).click()

    def get_taxi(self):
        return self.driver.find_element(*self.taxi_search_button).get_property('value')

    def close_window(self):
         self.driver.implicitly_wait(0)