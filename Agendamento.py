def teste_agendamento_doacao():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/agendamento")
    
    driver.find_element(By.NAME, "local").send_keys("Hemocentro A")
    driver.find_element(By.NAME, "data").send_keys("2024-12-01")
    driver.find_element(By.NAME, "horario").send_keys("10:00")
    driver.find_element(By.ID, "btn_agendar").click()
    
    # Verificar se o agendamento foi confirmado
    time.sleep(2)
    mensagem = driver.find_element(By.ID, "mensagem").text
    assert "Agendamento confirmado" in mensagem
    print("Teste de Agendamento: OK")
    driver.quit()

teste_agendamento_doacao()