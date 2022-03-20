import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium import webdriver

DELAY = 0.5

urlBase = 'https://fr.tripadvisor.ca/'
f = open("Comment.txt", "w", encoding='utf-8')

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(urlBase)

while True:

    url = input('Entrez l\'url: ')

    if url == 'STOP':
        break

    file = input('Entrez le nom du fichier (avec extension)): ')

    driver.get(url)

    f = open(file, "w", encoding='utf-8')

    while True:

        #Ouverture des sections 'plus'
        while True:
            time.sleep(DELAY)
            try:
                plusButtons = driver.find_element_by_xpath('//*[normalize-space(text())="Plus"]')
                ActionChains(driver).click(plusButtons).perform()
            except NoSuchElementException:
                break

        #Écriture des commentaire
        comments = driver.find_elements_by_xpath('//*[@class="partial_entry"]')
        for i in comments:
            if i.text != "":
                f.write(i.text + '\n\n')

        #Page suivante
        try:
            nextButton = driver.find_element_by_xpath('//*[normalize-space(text())="Suivant"]')
            link = nextButton.get_attribute("href")
            driver.get(link)
        except:
            break

    f.close()

driver.close()