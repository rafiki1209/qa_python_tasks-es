import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")
time.sleep(2)
# Buscar elementos
email = driver.find_element(By.ID,"email")
password = driver.find_element(By.ID,"password")

# Probar el atributo placeholder para cada elemento

assert email.get_attribute('placeholder') == "Correo electrónico"
assert password.get_attribute('placeholder') == "Contraseña"
print ("Pruebas exitosas!")
# Cerrar el navegador
driver.quit()
