from Chrome import Chrome
from time import sleep
from PegarContato import PegarContato
from GerarUrl import GerarUrl
from selenium.webdriver.common.by import By
from EnvioRealizado import EnvioRealizado
from EnvioNaoRealizado import EnvioNaoRealizado


class OpenChrome:
    def __init__ (self):
        driver = Chrome().driver() 
        self.driver = driver
    
    def acessandoSiteWhatsApp(self):
        driver = self.driver
        driver.get("https://web.whatsapp.com/")
        while len(driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[4]")) < 1:
                sleep(0.5)
        self.acessandoContato()

    def acessandoContato(self):
        driver = self.driver

        leitor = PegarContato()
        contatos = leitor.ler_excel()
        for contato in contatos:
            url = GerarUrl(contato.nome, contato.contato)
            urlGenerated = url.geradorDeUrl()
            print(urlGenerated)
            driver.execute_script("window.location.href = '{}'".format(urlGenerated))   
            while len(driver.find_elements(By.ID, "main")) < 1:
                ok_element = "/html/body/div[1]/div/div/span[2]/div/span/div/div/div/div/div/div[2]/div/button"
                if(len(driver.find_elements(By.XPATH, ok_element)) != 0):
                    print("")
                    break
                sleep(0.5)
                
            self.enviarMensagem()
    
    def enviarMensagem(self):
        driver = self.driver

        try:
            btn_enviarElement = "/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button"
            btn_enviar = driver.find_element(By.XPATH, btn_enviarElement)
        except:
            try:
                btn_enviarElement = "#main > footer > div._ak1k._ahmw.copyable-area > div > span:nth-child(2) > div > div._ak1r > div._ak1t._ak1u > button"
                btn_enviar = driver.find_element(By.CSS_SELECTOR, btn_enviarElement)
            except:
                env_nao_realizado = EnvioNaoRealizado()
                env_nao_realizado.preencher_ctt_nao_realizado()
                return print("BTN enviar não localizado")
        btn_enviar.click()
        sleep(5)
        env_realizado = EnvioRealizado()
        env_realizado.preencher_ctt_realizado() 
        

chrome = OpenChrome()
chrome.acessandoSiteWhatsApp()