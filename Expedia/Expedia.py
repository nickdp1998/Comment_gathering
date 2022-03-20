import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium import webdriver

urlBase = 'https://www.expedia.com/'

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(urlBase)

searchBar = driver.find_element_by_xpath('//*[contains(@aria-label, "Going to")]')
ActionChains(driver).click(searchBar).perform()

searchEntry = driver.find_element_by_xpath('//*[contains(@placeholder, "Where are you going")]').send_keys("Test\n")

searchButton = driver.find_element_by_xpath('//*[contains(@data-testid, "submit-button")]')
ActionChains(driver).click(searchButton).perform()


print('Compléter la vérification')

while True:
    url = input('Entrez l\'url: ')

    if url == 'STOP':
        break

    file = input('Entrez le nom du fichier (avec extension)): ')

    driver.get(url)

    f = open(file, "w", encoding='utf-8')

    SCROLL_PAUSE_TIME = 0.5

    allCommentButton = driver.find_element_by_xpath('//*[contains(@data-stid, "reviews-link")]').click()


    while True:
        try:
            time.sleep(4*SCROLL_PAUSE_TIME)
            moreComment = driver.find_element_by_xpath('//*[text()[contains(., "More reviews")]]')

            last_height = moreComment.location
            ActionChains(driver).click(moreComment).perform()

            new_height = moreComment.location

            if last_height == new_height:
                break

        except NoSuchElementException:
            break;

    comment = driver.find_elements_by_xpath('//*[@itemprop="description"]')

    for i in comment:
        if i.text != "":
            f.write(i.text + '\n\n')

    f.write('\n')

    f.close()