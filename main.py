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

    def test_full_taxi_request_process(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_call_taxi_button()

    # Seleccionar la tarifa Comfort
        routes_page.select_comfort_rate()
        self.driver.implicitly_wait(10)

    # Rellenar el número de teléfono
        phone_number = data.phone_number
        self.driver.implicitly_wait(10)  # cambio del timeslep
        routes_page.set_phone()
        routes_page.the_next_button()
        self.driver.implicitly_wait(10)  # cambio del timeslep

    # Recuperar el código de confirmación del teléfono
        routes_page.code_number()
        self.driver.implicitly_wait(10)  # cambio del timeslep
        routes_page.send_cell_info()
        self.driver.implicitly_wait(10)  # cambio del timeslep
        self.driver.implicitly_wait(30)

    # Agregar una tarjeta de crédito
        self.driver.implicitly_wait(30)
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

    # Escribir un mensaje para el conductor
        self.driver.implicitly_wait(30)
        routes_page.write_drive_message()
        assert routes_page.get_message() == 'traiga una aperitivo'

    # Pedir una manta y pañuelos
        self.driver.implicitly_wait(20)  # cambio del timeslep
        routes_page.request_blanket_and_tissues()

    # Pedir 2 helados
        self.driver.implicitly_wait(30)  # cambio del timeslep
        routes_page.request_ice_cream()

    # Buscar un taxi
        self.driver.implicitly_wait(60)
        routes_page.search_taxi()

