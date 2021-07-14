from bs4 import BeautifulSoup
import requests
import pandas as pd


def get_connection(busca):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "pt-BR,en;q=0.5","Accept-Encoding": "gzip, deflate"}
    url = "http://www.americanas.com.br/busca/" + busca
    return requests.get(url, headers=headers).text

def scrapy_attributes_to_pandas(busca):
    session = get_connection(busca)
    nomes = []
    valores = []
    soup = BeautifulSoup(session, 'lxml')
    attribute = get_attributes(soup)
    d = set_to_array(attribute)
    return pd.DataFrame(data = d)

def add_pandas_to_xlsx(df):
    with pd.ExcelWriter("teste.xlsx") as writer:
        df.to_excel(writer)

def get_attributes(soup):
    nome = soup.find_all('span', class_= 'src__Text-sc-154pg0p-0 src__Name-sc-1k0ejj6-2 kcJuNs')
    valor = soup.find_all('span', class_= 'src__Text-sc-154pg0p-0 src__PromotionalPrice-sc-1k0ejj6-6 cbiYUL')
    return [nome, valor]

def set_to_array(attribute):
    nomes = []
    valores = []
    for i in attribute[0]:
        nomes.append(i.text)
    for i in attribute[1]:
        valores.append(i.text)
    return {"nome": nomes, "valor": valores}