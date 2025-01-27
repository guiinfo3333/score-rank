from selenium.webdriver.common.by import By
from models.scrapy import Scrapy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GetEstatiscEspion(Scrapy):
    def __init__(self):
        super().__init__()

    def searchEstatisticEspion(self):
        self.driver.get(
            "https://ge.globo.com/espiao-estatistico/noticia/2024/11/23/favoritismos-35-dicas-palpites-e-chances-de-vencer-no-brasileirao.ghtml")

        try:
            valor = self.driver.find_element(By.CSS_SELECTOR, f"#slide-content-foreground").click()
            print(valor)

            image_to_download_probabilites = WebDriverWait(self.driver, 5000).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#slide-content-foreground"))
            )

            if image_to_download_probabilites:
                self.driver.execute_script("arguments[0].scrollIntoView();", image_to_download_probabilites[0])
                self.driver.implicitly_wait(2)
            else:
                print("Nenhum elemento encontrado com o seletor fornecido.")

        except Exception as e:
            print(f"Erro ao tentar localizar ou rolar até o elemento: {str(e)}")

