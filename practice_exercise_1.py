from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v135.layer_tree import profile_snapshot
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")
driver.implicitly_wait(15)
# 1. Iniciar sesión
driver.find_element(By.ID, "email").send_keys("rafiki1209@gmail.com")
driver.find_element(By.ID, "password").send_keys("Rlms1209")
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

# Agregar una espera explícita para que se cargue la página
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "header__user")))

# 2. Hacer clic en la foto de perfil
driver.find_element(By.CSS_SELECTOR, ".profile__image").click()

# 3 y 4 Insertar el enlace a la foto en el campo Enlace utilizando la variable avatar_url
avatar_url = "https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/qa-sprint-7/avatarSelenium.png"
driver.find_element(By.ID, "owner-avatar").send_keys(avatar_url)

# 5 Guardar la nueva foto
driver.find_element(By.XPATH, ".//form[@name='edit-avatar']/button[text()='Guardar']").click()

#  6 Agregar una espera explícita hasta que aparezca la nueva foto de perfil
WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element_attribute((By.CSS_SELECTOR, ".profile__image"), 'style', avatar_url))

# Guardar el valor del atributo de estilo para el elemento de foto de perfil en la variable style
style = driver.find_element(By.CSS_SELECTOR, ".profile__image").get_attribute('style')

# 7 Comprobar que style contiene el enlace a la foto de perfil

assert  avatar_url in style

driver.quit()
