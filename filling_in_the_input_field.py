import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")
time.sleep(2)
# Buscar el campo Correo electrónico y rellenarlo
driver.find_element(By.ID,"email").send_keys("rafiki1209@gmail.com")

# Buscar el campo Contraseña y rellenarlo
driver.find_element(By.ID,"password").send_keys("Rlms1209")
time.sleep(2)
# Buscar el botón Iniciar sesión y hacer clic en él
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

# Agregar una espera explícita para que se cargue la página
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "header__user")))


# Comprobar que la URL actual es 'https://around-v1.nm.tripleten-services.com/signin?lng=es'
assert driver.current_url == 'https://around-v1.nm.tripleten-services.com/'


driver.quit()
