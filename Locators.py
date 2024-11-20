from selenium.webdriver.common.by import By
import data
class UrbanRoutesLoc:
    from_address =(By.ID,'from')
    to_address= (By.ID,'to')

    taxi_button = (By.CLASS_NAME,'//button[@class="button taxi"]')
    comfort = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[2]')
    phone_number_field = (By.CLASS_NAME, "np-button")
    phone_number_input = (By.ID, "np-text")
    phone_number_section = (By.XPATH,'section active"><button class')
    close_button = (By.CLASS_NAME,'close-button')
    number = (By.XPATH, '//*[@id="phone"]')
    next_button = (By.XPATH, '//*[text()="Siguiente"]')
    click_code = (By.ID, 'code_input')
    code = (By.ID, 'code')
    select_taxi = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    phone_send_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')
    payment_method_select = (By.CLASS_NAME, 'pp-button')
    close_button_payment_method = (By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[2]/button')
    imput_add_card_number =  (By.CLASS_NAME, "pp-plus")
    credit_click = (By.CLASS_NAME, "card-number-imput")
    imput_add_card_code = (By.CLASS_NAME,"code_card")
    add_card = (By.XPATH, '//*[text()="Agregar"]')
    message_for_driver= (By.CSS_SELECTOR, 'comment')
    reqs_body = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]')
    reqs_button = (By.CLASS_NAME,'reques head')
    blanket_and_scarves = (
    By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')
    ice_crem = (By.NAME,'container')
    counter_value = (By.ID,'value 2')
    order_number = (By.ID,"number>h_180")
    taxi_search_button = (By.CLASS_NAME, "smart-button-main")
    modal_taxi = (By.XPATH, "order-details")
    Button_cancelar = (By.XPATH,'//*[@id="root"]/div/div[5]/div[2]/div[2]/div[1]/div[2]/div')
    asing_driver = (By.CLASS_NAME,"order-number")


