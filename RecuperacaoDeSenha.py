def teste_recuperacao_senha():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/recuperar_senha")
    
    driver.find_element(By.NAME, "email").send_keys("joao@example.com")
    driver.find_element(By.ID, "btn_recuperar").click()
    
    # Verificar se o sistema enviou um e-mail de recuperação
    time.sleep(2)
    mensagem = driver.find_element(By.ID, "mensagem").text
    assert "E-mail de recuperação enviado" in mensagem
    print("Teste de Recuperação de Senha: OK")
    driver.quit()

teste_recuperacao_senha()