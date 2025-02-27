# Proyecto de Urban Routes Automatización de Solicitud de Taxi Comfort
___
## INDICE

- Descripción
- Lista de comprobación
- Archivos de proyecto
- Paquetes de python
- Instrucciones para las pruebas

___
## Descripción


- Comprobar pruebas para la funcionalidad y automatización de solicitar un taxi en la plataforma de Urban Routes

## Lista de comprobación

- Realizar  varias pruebas y métodos para comprobación de la funcionalidad de Urban Routes. En el archivo main.py para la solicitud de servicio de taxi en la tarifa Confort y todo el proceso hasta la confirmación y llegada del taxita.

- setup_class(cls): Configurar las opciones del navegador
- def test_set_route(self): Configura y verifica dirección de la ruta.
- def test_click_call_taxi_button(self): Selecciona boton para llamar el taxi
- def test_select_comfort_rate(self): Selecciona y valida la selección de la tarifa Confort.
- def set_select_number_button(self): Selecciona y rellena el número de teléfono.
- def add_number(self): Añade número
- def phone_number(self): 
- def the_next_button(self): 
- def code_number(self): Añade codigo de verificación de telefono
- def payment_method(self): Ejecuta y revisa la configuración de los métodos de pago.
- def write_driver(self): Ingresa y confirma mensaje personalizado.
- def blanket_and_tissues(self):Seleccione y valide la configuración de los requisitos adicionales.
- def request_ice_cream(self): Seleccion de cantidad de helado
- def search_taxi(self): Realiza la busqueda de taxi y se verifica que se haya ejecutado la orden.
- def test_wait_driver_details(self): Verifique la recepción de los detalles del conductor y que el viaje haya sido tomado.

## Lista de comprobación 

- URL de servidor 
- Configurar la dirección 
- Seleccionar personal
- Pedir taxi
- Seleccionar la tarifa Comfort.
- Rellenar el número de teléfono.
- Agregar una tarjeta de crédito. 
- Escribir un mensaje para el conductor
- Pedir una manta y pañuelos.
- Pedir 2 helados.
- Aparece el modal:  buscar un taxi.
- Esperar a que aparezca la información del conductor en el modal 


## Descripción de las tecnologías y técnicas utilizadas

- main.py
- data.py
- .gitignore
- Urban_RoutesPage.py
- SMS.py
- README.md
- Paquetes de Python
- pip
- Pytest
- requests
- TripleTen 

## Instrucciones sobre como ejecutar las pruebas

- Creación del Proyecto para Urban Routes:


1 Clona el repositorio de GitHub en tu máquina local: git clone 

2 Una vez que hayas vinculado tu cuenta de TripleTen con GitHub, se creará un repositorio automáticamente. El nombre del repositorio será qa-project-Urban-Routes-es
Ve a GitHub y clona el nuevo repositorio en tu computadora local, siguiendo estos pasos:
Abre tu terminal preferida. Si estás en Windows, deberás utilizar Git Bash.
Si aún no lo has hecho, crea un directorio para almacenar todos tus proyectos.

3 Clona el repositorio. 

4 Si usas un Sotfware como Pycham ve a los paquetes e instala pip, pythes, requests

5 Estas listos para correr los test desde pycham


## Comandos de ejecución 

- Status
- Branch
- commit -m
- Git
- push
- merge
- stash
- checkout master


___________________
Hecho por: María del Pilar Guerrero 

Cohort 16 pero ahora estoy Cohort 22