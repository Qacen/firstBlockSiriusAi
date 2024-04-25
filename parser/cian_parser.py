from selenium.webdriver.common.by import By
from parser import parser_property
key_good = ['Количество комнат','Общая площадь','Площадь кухни','Этаж','Ремонт','Тип дома','год постройки']
key_good_another = ['Ремонт','Тип дома']
value_change = ['Площадь кухни','Общая площадь']
def parsing(url):
        driver = parser_property.driver_create(url)

        params = {}
        params["Цена"] = driver.find_element(By.XPATH,'//*[@id="frontend-offer-card"]/div/div[2]/div[3]/div/div[1]/div[1]/div[4]/div/div[1]/span').text
        params["Адрес"] = driver.find_element(By.XPATH,'//*[@id="frontend-offer-card"]/div/div[2]/div[2]/section/div/div/div[2]/address/div/div').text.replace("На карте","")

        elems = driver.find_elements(By.CLASS_NAME,"a10a3f92e9--item--Jp5Qv")
        for i in elems:
                key = i.text.split("\n")[0]
                value = i.text.split("\n")[1].strip()
                if (key in key_good):
                        if (key.startswith("Этаж")):
                                params["Этаж"] = value.split("из")[0].strip()
                                params["Этажность"] = value.split("из")[1].strip()
                                continue
                        elif(key in value_change):
                                value = value.split(' ')[0]
                        elif(key == "Количество комнат" & value == "студия"):
                                value = 0
                        params[key] = value
        elems = driver.find_elements(By.CLASS_NAME, "a10a3f92e9--item--qJhdR")
        for i in elems:
                key = i.text.split("\n")[0]
                value = i.text.split("\n")[1]
                if (key in key_good_another):
                        params[key] = value
        driver.quit()
        return params