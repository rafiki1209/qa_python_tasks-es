import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Buscar el campo Correo electrónico y rellenarlo
wait.until(expected_conditions.presence_of_element_located((By.ID, "email"))).send_keys("rafiki1209@gmail.com")

# Buscar el campo Contraseña y rellenarlo
wait.until(expected_conditions.presence_of_element_located((By.ID, "password"))).send_keys("Rlms1209")

# Buscar el botón Iniciar sesión y hacer clic en él
wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".auth-form__button"))).click()

# Agregar una espera explícita para que se cargue la página
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".header__user")))

# Buscar el botón, recuperar su texto y comprobar que el valor del texto es 'Cerrar sesión'
logout_text = wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "header__logout"))).text

assert logout_text.strip() == 'Cerrar sesión', f"Se esperaba 'Cerrar sesión', pero se obtuvo '{logout_text}'"

driver.quit()


