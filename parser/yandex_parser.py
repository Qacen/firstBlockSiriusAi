from selenium.webdriver.common.by import By
from parser import parser_property
import time
key_good = ['общая','жилая','кухня','Этаж','год постройки']
key_correct = {'общая':'Общая площадь','жилая':'Жилая площадь','кухня':'Площадь кухни','год постройки':'Год постройки'}
value_change = ['Площадь кухни','Общая площадь']
def parsing(url):
        driver = parser_property.driver_create(url)
        params = {}
        params["Цена"] = driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/div/div[5]/div/div[1]/div[2]/div[1]/span').text
        params["Адрес"] = driver.find_element(By.XPATH,'//*[@id="location"]/div[1]/section/div[1]').text
        count_rooms = driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/div/div[5]/div/div[1]/div[2]/div[1]/h1').text
        if (count_rooms.split('-')[1]=="студия"):
                params["Количество комнат"] = 0
        else:
                params["Количество комнат"] = count_rooms.split('-')[0].strip()
        elems = driver.find_elements(By.CLASS_NAME,"OfferCardHighlight__container--2gZn2")
        for i in elems:
                key = i.text.split("\n")[1]
                value = i.text.split("\n")[0]
                if (value.split(' ')[1] == "этаж"):
                        params["Этаж"] = value.split(' ')[0]
                        params["Этажность"] = key.split(' ')[1]
                elif (key in key_good):
                        params[key_correct[key]] = value
        driver.quit()
        return params
