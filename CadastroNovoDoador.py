from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def teste_cadastro_doador():
    driver = webdriver.Chrome()  # Certifique-se de ter o chromedriver no seu PATH
    driver.get("http://localhost:8000/cadastro")  # URL do seu sistema local
    
    # Preenchimento dos campos do formulário de cadastro
    driver.find_element(By.NAME, "nome").send_keys("João Silva")
    driver.find_element(By.NAME, "cpf").send_keys("12345678901")
    driver.find_element(By.NAME, "data_nascimento").send_keys("01/01/1995")
    driver.find_element(By.NAME, "peso").send_keys("60")
    driver.find_element(By.NAME, "tipo_sanguineo").send_keys("O+")
    driver.find_element(By.NAME, "email").send_keys("joao@example.com")
    driver.find_element(By.NAME, "senha").send_keys("Senha123")
    driver.find_element(By.NAME, "confirma_senha").send_keys("Senha123")
    driver.find_element(By.ID, "btn_cadastrar").click()
    
    # Verificar se o redirecionamento para a página de login ocorreu
    time.sleep(3)
    assert "login" in driver.current_url
    print("Teste de Cadastro: OK")
    driver.quit()

teste_cadastro_doador()