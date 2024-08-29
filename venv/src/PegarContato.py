import pandas as pd

class PegarContato:
    def __init__(self):
        self.caminho_arquivo = "C:\WppBot\prospeccao.xlsx"

    def ler_excel(self):
        try:
            df = pd.read_excel(self.caminho_arquivo)
            contatos = []
            for indice, (nome, contato, ctt_realizado) in enumerate(zip(df['NOME'], df['CONTATO'], df['CTT_REALIZADO?']), start=1):
                if pd.isna(ctt_realizado):  # Verifica se o campo CTT_REALIZADO? está vazio
                    contato_obj = Contato(nome, contato, indice)
                    contatos.append(contato_obj)
            return contatos
        except Exception as e:
            print(f"Erro ao ler arquivo Excel: {e}")
            return []

class Contato:
    def __init__(self, nome, contato, numero_linha):
        self.nome = nome
        self.contato = contato
        self.numero_linha = numero_linha


        

