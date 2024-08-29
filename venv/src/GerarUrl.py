class GerarUrl:
    def __init__(self, nome_empresa, numero_empresa):
        self.nome_empresa = nome_empresa
        self.numero_empresa = numero_empresa

    def geradorDeUrl(self):
        numero = self.numero_empresa
        texto = f"Boa tarde, seria da {self.nome_empresa}?"
        return f'https://web.whatsapp.com/send?phone={numero}&text={texto}'