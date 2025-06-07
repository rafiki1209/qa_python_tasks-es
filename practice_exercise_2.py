from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Iniciar sesión
driver.find_element(By.ID, "email").send_keys("rafiki1209@gmail.com")
driver.find_element(By.ID, "password").send_keys("Rlms1209")
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

# Agregar una espera explícita para que se cargue la página
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "header__user")))

# Guardar el título de la tarjeta más reciente
title_before = 

# Hacer clic en el botón que publica una nueva tarjeta
driver.find_element(...)...

# Generar el nuevo nombre del lugar e ingresarlo en el campo Nombre
new_title = ...
driver.find_element(...)...

# Insertar el enlace a la imagen en el campo Enlace
driver.find_element(...)...

# Guardar los datos
driver.find_element(...)...

# Esperar a que aparezca el botón Eliminar
WebDriverWait(...).until(...)

# Comprobar que la tarjeta tiene el título correcto
title_after = ...
assert ...

# Guardar la cantidad de tarjetas antes de eliminar
cards_before = len(...)

# Eliminar la tarjeta
driver.find_element(...)...

# Esperar a que el título de la tarjeta más reciente sea igual a title_before
WebDriverWait(...).until(...)

# Comprobar que ahora hay una tarjeta menos
cards_after = len(...)
assert ...

driver.quit()
