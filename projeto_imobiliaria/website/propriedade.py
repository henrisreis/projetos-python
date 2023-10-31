class Apartamento:
    def __init__(self, titulo, endereco, preco, condominio, iptu, area, quartos, banheiros, vagas):
        self.titulo = titulo
        self.endereco = endereco
        self.preco = preco
        self.condominio = condominio
        self.iptu = iptu
        self.area = area
        self.quartos = quartos
        self.banheiros = banheiros
        self.vagas = vagas

    def display(self):
        print()
        print('DETALHES DA PROPRIEDADE')
        print('=' * 15)
        print(self.titulo)
        print(f'Endereço da propriedade: {self.endereco}')
        print(f'Preço: R${self.preco}')
        print(f'Condomínio: R${self.condominio}')
        print(f'IPTU: R${self.iptu}')
        print(f'Área: {self.area}m²')
        print(f'Quartos: {self.quartos}')
        print(f'Banheiros: {self.banheiros}')
        print(f'Vagas: {self.vagas}')
        print('=' * 15)
        print()

    @staticmethod
    def prompt_init():
        return dict(titulo=input('Insira o título do seu anúncio: '),
                    endereco=input('Qual é o endereço da propriedade? '),
                    preco=input('Qual é o preço (R$)? '),
                    condominio=input('Qual é o valor do condomínio (R$)? '),
                    iptu=input('Qual é o valor do IPTU (R$)? '),
                    area=input('Qual é a área da propriedade (m²)? '),
                    quartos=input('Quantos quartos tem? '),
                    banheiros=input('Quantos banheiros possui? '),
                    vagas=input('Quantas vagas de garagem? '))


if __name__ == '__main__':
    init = Apartamento.prompt_init()
    apartamento_1 = Apartamento(**init)
