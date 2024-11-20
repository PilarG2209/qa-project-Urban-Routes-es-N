from selenium import webdriver
from Urban_RoutesPage import UrbanRoutesPage
import time
import data
import Locators
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

urban_routes_url: str = 'https://cnt-748cc606-13d3-4474-8f39-d90e189d8f41.containerhub.tripleten-services.com?lng=es'

class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        time.sleep(10)
        routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == data.address_from
        assert self.routes_page.get_to() == data.address_to

    def test_full_taxi_request_process(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        # Configurar la dirección
        address_from = data.address_from
        address_to = data.address_to
        self.driver.implicitly_wait(10)  # cambio del timeslep
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

        # Seleccionar taxi
        routes_page.select_taxi_button()

        # Seleccionar la tarifa Comfort
        routes_page.select_comfort_rate()

        # Rellenar el número de teléfono
        phone_number = data.phone_number
        self.driver.implicitly_wait(10)  # cambio del timeslep
        routes_page.set_phone()
        assert routes_page.get_phone() == phone_number

        # Recuperar el código de confirmación del teléfono
        routes_page.the_next_button()
        self.driver.implicitly_wait(50)  # cambio del timeslep
        routes_page.code_number()
        self.driver.implicitly_wait(50)  # cambio del timeslep
        routes_page.send_cell_info()
        self.driver.implicitly_wait(50)  # cambio del timeslep

        # Agregar una tarjeta de crédito
        self.driver.implicitly_wait(20)  # cambio del timeslep
        routes_page.click_card()
        self.driver.implicitly_wait(20)  # cambio del timeslep
        routes_page.add_card()
        self.driver.implicitly_wait(20)  # cambio del timeslep
        routes_page.close_window()
        assert routes_page.get_card_input() == data.card_number  # agregar asserts
        assert routes_page.get_cvv_card() == data.card_code      # agregar asserts

        # Escribir un mensaje para el controlador
        message = data.message_for_driver
        routes_page.write_drive_message(message)
        assert routes_page.get_message() == data.message_for_driver  # agregar assert

        # Pedir una manta y pañuelos
        self.driver.implicitly_wait(20)  # cambio del timeslep
        routes_page.request_blanket_and_tissues()
        assert routes_page.get_blanket_and_scarves() == routes_page.request_blanket_and_tissues()  # agregar assert

        # Pedir 2 helados
        self.driver.implicitly_wait(20)  # cambio del timeslep
        routes_page.request_ice_cream()
        assert routes_page.get_ice_cream() == routes_page.request_ice_cream()  # agregar Assert

        # Buscar un taxi
        self.driver.implicitly_wait(60)
        routes_page.search_taxi()

        # Esperar a que aparezca la información del conductor en el modal
        self.driver.implicitly_wait(60)
        routes_page.wait_for_driver_info()


#_______________________
#from selenium import webdriver # Importar Selenium WebDriver

#from data import comfort, urban_routes_url

#driver = webdriver.Chrome() # Crea un controlador


# Abrir una página
#driver.get('https://google.com/')

#Seleccionar la tarifa comfort
#Comfort = driver.find_element (By.ID, "comfort")

#assert
#___________________
# current_url = driver.current_url # obtener la URL de la página
# assert current_url == 'https://google.com/' #Ahora puedes asegurarte de que esta es exactamente la URL que necesitas. Para eso, necesitarás el método assert
# assert 'google.com' in driver.current_url #comprobar solo una parte de una URL
#find_element() #encuentro de elemento
#find_elements() #devuelve varios elementos
#Cliterios de busqueda
#By.CLASS_NAME # Buscar por nombre de la clase
#By.CSS_SELECTOR # Buscar por selector CSS
#By.ID # Buscar por atributo ID
#By.LINK_TEXT # Buscar por el texto del enlace (no el enlace https:// en sí, sino el texto dentro del objeto del enlace; más sobre eso en la próxima lección)
#By.PARTIAL_LINK_TEXT # Buscar por una parte del texto del enlace, similar a By.linkText(text)
#By.NAME # Buscar por el atributo name
#By.TAG_NAME # Buscar por la etiqueta HTML
#By.XPATH # Buscar por XPath
#ejemplo de busqueda por Xpath
#driver.find_element(By.XPATH, ".//img")
#from selenium.webdriver.common.by import By #Para usar los métodos de la clase By, primero debes importarla:
#driver.quit()
