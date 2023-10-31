from website.usuario import Corretor


def main():
    corretor_1 = Corretor('Luciano')
    corretor_1.anunciar()
    corretor_1.anunciar()
    corretor_1.display_portfolio()


if __name__ == '__main__':
    main()
