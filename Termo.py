def teste_upload_documento():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/upload_documento")
    
    driver.find_element(By.NAME, "arquivo").send_keys("/path/to/hemograma.pdf")
    driver.find_element(By.ID, "btn_upload").click()
    
    # Verificar se o upload foi realizado com sucesso
    time.sleep(2)
    mensagem = driver.find_element(By.ID, "mensagem").text
    assert "Upload realizado com sucesso" in mensagem
    print("Teste de Upload de Documento: OK")
    driver.quit()

teste_upload_documento()