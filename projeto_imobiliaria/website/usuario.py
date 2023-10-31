from website.propriedade import Apartamento


class Corretor():
    def __init__(self, nome):
        self.nome = nome
        self.portfolio = []

    def display_portfolio(self):
        print(f'Portfólio do corretor {self.nome}')
        for apartamento in self.portfolio:
            apartamento.display()

    def anunciar(self):
        init_args = Apartamento.prompt_init()
        self.portfolio.append(Apartamento(**init_args))
