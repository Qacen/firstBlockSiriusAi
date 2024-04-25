from selenium.webdriver.common.by import By
from parser import parser_property
key_good = ['Количество комнат','Общая площадь','Площадь кухни','Этаж','Ремонт','Тип дома','Этажей в доме','Жилая площадь']
value_change = ['Площадь кухни','Общая площадь']
def parsing(url):
        driver = parser_property.driver_create(url)

        params = {}
        params["Цена"] = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[1]/div/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div[1]/div/span/span/span[1]').text
        params["Адрес"] = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[1]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/span').text
        params["Район"] = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[1]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div/span/span/span[2]').text

        elems = driver.find_elements(By.CLASS_NAME,"params-paramsList__item-_2Y2O")
        for i in elems:
                key = i.text.split(':')[0]
                value = i.text.split(':')[1].strip()
                if (key in key_good):
                        #print(key)
                        if (key.startswith("Этаж")):
                                value = value.split("из")[0].strip()
                        elif(key in value_change):
                                value = value.split(' ')[0]
                        elif(key == "Количество комнат" & value == "студия"):
                                value = 0
                        params[key] = value

        driver.quit()
        return params

