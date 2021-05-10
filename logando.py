import shopify
import requests
import json
from datetime import date, datetime
from contador import Variantes


class ShopifyApp(Variantes):
    def __init__(self):
        self.chaveapi =
        self.senhaapi =
        self.apiversion = '2020-07'
        self.itens=[]
        self.shop_url = f"https://{self.chaveapi}:{self.senhaapi}@sualoja.myshopify.com/admin/api/{self.apiversion}"
        shopify.ShopifyResource.set_site(self.shop_url)


    def dia_atual(self):
        try:
            dia_hoje = date.today().strftime("%d/%m/%Y")
            return dia_hoje
        except Exception as error:
            print("Erro ao pegar data atual", error)


    def get_collection(self, collection=''):
        try:
            url_collection = f'{self.shop_url}/collections/{collection}/products.json'
            url_resposta = requests.get(url_collection)
            products = json.loads(url_resposta.text)
            products = products['products']
            for percorre in products:
                id_item = percorre['id']
                nome_item = percorre['title']
                self.itens.append(self.contando(self.shop_url, id_item, nome_item))
            return self.itens

        except Exception as error:
            print("Erro ao pegar items", error)

class Comparacao:
    def compara_datas(self, dataatual, dataplanilha):
        try:
            compara1 = datetime.strptime(dataplanilha, '%d/%m/%Y').date()
            compara2 = datetime.strptime(dataatual, '%d/%m/%Y').date()
            dif = compara2 - compara1
            return dif.days
        except Exception as error:
            print("Erro ao comparar datas", error)
