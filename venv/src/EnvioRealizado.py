import pandas as pd

class EnvioRealizado:
    def __init__(self):
        self.caminho_arquivo = r"C:\WppBot\prospeccao.xlsx"
    def preencher_ctt_realizado(self):
        try:
            df = pd.read_excel(self.caminho_arquivo)
            coluna_ctt_realizado = df['CTT_REALIZADO?']
            primeira_linha_vazia = coluna_ctt_realizado.index[coluna_ctt_realizado.isnull()].tolist()[0]
            df.at[primeira_linha_vazia, 'CTT_REALIZADO?'] = 'Sim'
            df.to_excel(self.caminho_arquivo, index=False)
        except Exception as e:
            print(f"Erro ao preencher a célula: {e}")
