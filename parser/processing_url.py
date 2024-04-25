from parser import yandex_parser
from parser import avito_parser
from parser import  cian_parser
def process_url(url):
    params = {}
    try:
        if (url.startswith("https://domclick.ru/")):
            print("domclick")
        elif(url.startswith("https://www.avito.ru/moskva/kvartiry/")):
            params = avito_parser.parsing(url)
        elif(url.startswith("https://www.cian.ru/sale/flat/")):
            params = cian_parser.parsing(url)
        elif(url.startswith("https://realty.ya.ru/offer/")):
            params = yandex_parser.parsing(url)
        else:
            print("введите корректное url")
        print(params)
    except Exception as ex:
        print(ex.with_traceback())
    return params