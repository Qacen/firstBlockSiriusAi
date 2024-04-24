from parser import yandex_parser
from parser import avito_parser
from parser import  cian_parser
def process_url(url):
    params = {}
    if (url.startswith("https://domclick.ru/")):
        print("domclick")
    elif(url.startswith("https://www.avito.ru/")):
        params = avito_parser.parsing(url)
    elif(url.startswith("https://www.cian.ru/")):
        params = cian_parser.parsing(url)
    elif(url.startswith("https://realty.ya.ru/")):
        params = yandex_parser.parsing(url)
    else:
        print("введите корректное url")
    print(params)
    return params