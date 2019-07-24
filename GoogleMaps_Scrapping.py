#!/usr/bin/python                                                                                                                                                        #!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
import random
from time import sleep, time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import platform
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import csv
import json
#import cv2 as cv
#import pytesseract
import numpy as np
#from PIL import Image
import pandas as pd
import sys
import re, string
from time import gmtime, strftime

def get_driver():
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap['platform'] = "WINDOWS"
    dcap['version'] = "10"

    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
       ]

    dcap["phantomjs.page.settings.userAgent"] = user_agent_list[random.randrange(1, len(user_agent_list)-1, 1)]
    if platform.system() == 'Linux':
        driver = webdriver.PhantomJS(executable_path="/usr/local/bin/phantomjs", desired_capabilities=dcap)

        #driver = webdriver.PhantomJS(executable_path="/usr/local/bin/phantomjs", desired_capabilities=dcap)
    #driver = webdriver.PhantomJS(executable_path="/usr/local/bin/phantomjs",desired_capabilities=dcap,
        #                             service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1',
        #                                           '--proxy=127.0.0.1:8118', '--proxy-type=http'])
    else:
        # driver = webdriver.PhantomJS(
        #     executable_path="C:\\Users\\rcord_000\\Documents\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe",
        #     desired_capabilities=dcap)
        driver = webdriver.Chrome(

                executable_path="C:\\Users\\rcord_000\\Documents\\chromedriver.exe",
                desired_capabilities=dcap)
            # ,service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1',
            #                                       '--proxy=127.0.0.1:8118', '--proxy-type=http'])

    return driver

def connect_web(driver):
    c = 0
    while True:
        c += 1
        try:
            driver.set_page_load_timeout(40)
            driver.set_window_size(1124, 850)  # set browser size.
            driver.get('https://plus.codes/map')
            # sleep(4)
            print(driver.title)
            if driver.title != "" and "denegado" not in driver.title and "Found" not in driver.title:
                #controller.signal(stem.Signal.NEWNYM)
                sleep(6)
                print("FIN CONTROLLLER **")
                print("entro connect")
                break
            if c > 6:
                print("SUPERO 6 SALIO")
                break
        except TimeoutException as ex:
            print("Exception has been thrown. (TIME) " + str(ex))
        except:
            print('Could not open website, retrying ({})...'.format(c))
        driver.quit()
        sleep(3)
        driver = get_driver()
    return driver

def read_direc(ruta):

    data = pd.read_csv(ruta,encoding='latin-1',header=None)
    data = data.values.tolist()
    direc = []
    for i in data:
        x = i[0]
        x = str(x)
        direc.append(x)

    return direc

def maps(direc,driver):

    llave0 = ['DIR BUSCADA','DIR ENCONTRADA','COORDENADAS']
    llave1 = []
    lista_final = []
    copia = ''
    for i in direc:
        dir1 = ''
        driver.find_element_by_xpath('//*[@id="search-input"]').clear()
        driver.find_element_by_xpath('//*[@id="search-input"]').send_keys(i)
        sleep(1)
        driver.find_element_by_xpath('//*[@id="search-input"]').send_keys(Keys.ENTER)
        sleep(1)
        try:
            driver.find_element_by_xpath('//*[@id="summary"]/div[1]').click()
        except:
            coord = 'Direccion inexacta, no se encuentra la coordenada'
        sleep(1)

        try:
            coord = driver.find_element_by_xpath('//*[@id="placecard-details"]/div[3]/div[1]').text
            dir1 = driver.find_element_by_xpath('//*[@id="placecard-details"]/div[4]/div[1]').text

            if copia == coord:
                error = 'Direccion inexacta, no se encuentra la coordenada'
                llave1 = [i,'',error]
            else:
                llave1 = [i,dir1,coord]

        except:
            t = 1
        # print('Coord. obtenida: ' + coord + ' ||| Dir. buscada: ' + i + ' ||| Dir. Obtenida: ' + dir1)
        copia = coord
        dicF = dict(zip(llave0,llave1))
        lista_final.append((dicF))
        print('fin direccion append')

    return lista_final

def save_file(lista_final):

    csv_columns = ['DIR BUSCADA','DIR ENCONTRADA','COORDENADAS']
    csv_file = 'Geoubicaciones_scrap.csv'

    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in lista_final:
                writer.writerow(data)
    except IOError:
        print("I/O error")


def main():
    ruta = 'no_geo.csv'
    driver = get_driver()
    driver = connect_web(driver)
    direc = read_direc(ruta)
    # direc = ['Los Alpes 127, Surquillo, Peru','Av. 28 de Julio 218','Av Los Choclos 222', 'Bleriot 194, Surquillo, Peru']
    lista_final = maps(direc,driver)
    save_file(lista_final)


if __name__ == '__main__':

    try:
            main()
    except Exception as e:
            print('----------ERROR---------')
            print(e)
            print('Unhandled global error, exiting...')
