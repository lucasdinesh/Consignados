import requests
import json
import openpyxl
import os

class Variantes:
    def contando(self, url, id, nome):
        try:
            url_produtos = f"{url}/products/{id}/variants.json"
            resposta = requests.get(url_produtos)
            data = json.loads(resposta.text)
            variants = data['variants']
            estoque = 0
            for campo in variants:
                estoque = estoque + campo['inventory_quantity']
                preco = campo['price']

            items = {'id': id, 'nome': nome, 'estoque': estoque, 'preco': preco}
            return items
        except Exception as error:
            print("Erro ao executar codigo: ", error)


class Informacoes:
    def get_id(self, caminho):
        try:
            planilha_existente = openpyxl.load_workbook(filename=caminho)
            planilha1 = planilha_existente['Estoque']
            return planilha1['A80'].value

        except Exception as error :
            print("Erro ao executar codigo: ",error)

    def get_nomearquivo(self, caminho):
        try:
            return os.path.splitext(os.path.basename(caminho))[0]

        except Exception as error:
            print("Erro ao executar codigo: ", error)

