import data
from Urban_RoutesPage import UrbanRoutesPage
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from data import phone_number, message_for_driver, address_from, address_to


class TestUrbanRoutes:
    driver = None

    @classmethod

    def setup_class(cls):# Configurar las opciones del navegador
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.get(data.urban_routes_url)

    def test_set_route(self):
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        time.sleep(10)
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == data.address_from
        assert routes_page.get_to() == data.address_to

    def test_click_call_taxi_button(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_call_taxi_button()
        assert routes_page.click_call_taxi_button()

    def test_select_comfort_rate(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_comfort_rate()
        assert routes_page.select_comfort_rate()

    # Rellenar el número de teléfono
    def select_number_button(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.phone_number_field()
        assert routes_page.select_number_button

        #phone_number = data.phone_number
        #routes_page.set_phone()
        #routes_page.the_next_button()
    def add_number(self):
        self.driver.implicitly_wait(10)
        routes_page= UrbanRoutesPage(self.driver)
        routes_page.add_phone_number()
        assert routes_page.add_phone_number()

    def phone_number(self):
        self.driver.implicitly_wait(10)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_phone()
        assert routes_page.set_phone()

    def the_next_button(self):
         self.driver.implicitly_wait(10)
         routes_page = UrbanRoutesPage(self.driver)
         routes_page.next_button()
         assert routes_page.next_button()

    def send_cell_inf(self):
         self.driver.implicitly_wait(10)
         routes_page = UrbanRoutesPage(self.driver)
         routes_page.send_cell_info()
         assert routes_page.confirm_button

    def code_number(self):
         self.driver.implicitly_wait(10)  # cambio del timeslep
         routes_page = UrbanRoutesPage
         routes_page.phone_code()
         assert routes_page.phone_code

       #Agregar una tarjeta de crédito

    def payment_method(self):
        self.driver.implicitly_wait(30)
        routes_page = UrbanRoutesPage
        routes_page.pay_click()
        self.driver.implicitly_wait(30)
        routes_page.add_click()
        self.driver.implicitly_wait(30)
        routes_page.click_card()
        self.driver.implicitly_wait(30)
        routes_page.add_code_card()
        self.driver.implicitly_wait(30)
        routes_page.card_submit_button()
        self.driver.implicitly_wait(30)
        routes_page.close_button_payment()
        self.driver.implicitly_wait(30)
        assert routes_page.payment_method_select

    # Escribir un mensaje para el conductor

    def write_driver(self):
        self.driver.implicitly_wait(30)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.write_drive_message()
        assert routes_page.get_message() == 'traiga una aperitivo'

    # Pedir una manta y pañuelos
    def blanket_and_tissues(self):
        self.driver.implicitly_wait(20)  # cambio del timeslep
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.request_blanket_and_tissues().click()
        assert routes_page.request_blanket_and_tissues().click() == True

    # Pedir 2 helados
    def request_ice_cream(self):
        self.driver.implicitly_wait(30)  # cambio del timeslep
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.request_ice_cream()
        assert routes_page.request_ice_cream()

    # Buscar un taxi
    def search_taxi(self):
        self.driver.implicitly_wait(60)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.search_taxi()
        assert routes_page.search_taxi()