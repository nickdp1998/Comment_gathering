import time
import threading

from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import tkinter as tk
from tkinter import *

timer = 0.5

#Initialisation du navigateur
driver = webdriver.Chrome()
driver.maximize_window()

while True:

    query = input('Entrez le nom de la recherche: ')

    if query == 'STOP':
        break

    file = input('Entrez le nom du fichier (avec extension)): ')
    max_reviews = int(input('Entrez le nombre maximal de commentaires : '))

    #Chargement de la page
    driver.get('https://www.google.com/?hl=fr')
    driver.find_element_by_name('q').send_keys(query)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.NAME, 'btnK'))).click()

    #Variable pour une seconde vérification
    test = True

    #Ouverture de la section reviews
    try:
        show_comment = driver.find_element_by_xpath('//*[@jscontroller="qjk5yc"]')
        ActionChains(driver).click(show_comment).perform()
        time.sleep(2 * timer)
    except:
        driver.close()
        break

    # Ouverture du fichier pour l'écriture
    f = open(file, "w", encoding='utf-8')

    #Chargement du nombre de commentaire désiré
    all_comments = driver.find_elements_by_xpath('//*[@jscontroller="fIQYlf"]')
    last_length = len(all_comments)
    while True:
        driver.execute_script('arguments[0].scrollIntoView(true);', all_comments[-1])
        time.sleep(timer)
        all_comments = driver.find_elements_by_xpath('//*[@jscontroller="fIQYlf"]')
        new_length = len(all_comments)
        if last_length == new_length:
            if not test:
                break
            test = False
            continue
        if max_reviews <= new_length:
            break
        test = True
        last_length = new_length

    #Ouverture des commentaire ayant un "plus"
    while True:
        try:
            plus_buttons = driver.find_elements_by_xpath('//*[@class="review-more-link"]')
            for i in plus_buttons:
                ActionChains(driver).click(i).perform()
            break
        except NoSuchElementException:
            break

    #Enregestrement des commentaires
    all_comments = driver.find_elements_by_xpath('//span[@jscontroller="MZnM8e"]')
    all_names = driver.find_elements_by_xpath('//*[@class="TSUbDb"]/a')

    #Écriture des commentaire dans le fichier
    for i in all_comments:
        if i.text != "":
            ind = all_comments.index(i)
            f.write('------------------------------------\n')
            f.write('Nom : \n\n' + all_names[ind].text + '\n\n')
            f.write('Commentaires : \n\n' + i.text + '\n\n')
            f.write('------------------------------------\n')
    f.write('\n')
    f.close()

driver.close()

def extract_all(list, max_review, timer):
    for i in list:
        extract_google_reviews(i.e1.get(), False, i.e2.get(), max_review, timer)
