from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Já formatado para o caminho em Windows. Caso seu dispositivo seja Linux ou MacOS, verifique como deverá ser feita a instalação do caminho
# Necessário ter o ChromeDriver, que permite você usar as opções do chrome de forma avançada
# Será necessário você verificar sua versão do Chrome(botão dos três pontos->Acerca/Sobre Google Chrome -> Versão: ex:Versão 125.0.6422.77 (Compilação oficial) (64 bits))
# Após isso busque por chromedriver download se sua versão for compátivel com a do exemplo cole e de enter no link a seguir: https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.76/win64/chromedriver-win64.zip
# Depois crie uma pasta no seu Disco de Armazenamento(C:, D:, E:, ...) e extraia o arquivo lá


# Caminho para o ChromeDriver
driver_path = 'C:\\ChromeDriver\\chromedriver-win64\\chromedriver.exe'  # Certifique-se de que este caminho está correto

# Opções para abrir o Chrome em modo anônimo
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

# URL do site de votação
url = 'URL_SITE'


# Função VOTAR:
def votar(voto_num):

    # Inicia o navegador em modo anônimo
    driver = webdriver.Chrome(service=webdriver.chrome.service.Service(driver_path), options=chrome_options)

    try:
        # Acesse o site
        driver.get(url)

        # Aguarde carregar (ajuste conforme necessário)
        time.sleep(2)

        # Adicione logs para depuração
        print(f"Página carregada para o voto {voto_num}")

        # Localize e clique na opção "EM SUA OPÇÃO"
        labol_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//td[contains(@class, "estilo_celdas_opciones") and contains(text(), "SEU ELEMENTO DE VOTO E BUSCA ")]/preceding-sibling::td/input[@type="radio"]'))
        )
        print(f"Elemento encontrado, clicando na opção ELEMENTO_VOTO para o voto {voto_num}")
        labol_option.click()

        # Localize o botão de enviar
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@type="submit" and @value="Enviar"]'))
        )
        print(f"Botão de enviar encontrado, clicando para submeter o voto {voto_num}")

        # Clique no botão de enviar usando JavaScript para evitar elementos sobrepostos(ANÚNCIOS na maioria dos casos).
        driver.execute_script("arguments[0].click();", submit_button)

        # Aguarde a confirmação ou próximo passo (ajuste conforme necessário)
        time.sleep(1)
        print(f"Voto {voto_num} submetido com sucesso")

    except Exception as e:
        print(f"Erro ao votar no voto {voto_num}: {e}")

    finally:

        # Feche o navegador
        driver.quit()

# Repetir o processo


num_repeticoes = 1000 # Defina o número de repetições desejado

for i in range(1, num_repeticoes + 1):
    votar(i)
    time.sleep(0.5)  # Aguarde um pouco antes de iniciar a próxima iteração



