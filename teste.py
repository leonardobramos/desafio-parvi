from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Configurando o ChromeDriver automaticamente com o WebDriverManager
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

# Exemplo de uso: Abre uma página web
driver.get("https://www.exemplo.com")

# Agora você pode continuar com suas automações usando o 'driver'

# Quando terminar, não se esqueça de fechar o driver
# driver.quit()
