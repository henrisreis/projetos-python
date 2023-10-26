from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo=0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    
    @abstractmethod
    def sacar(self, valor): ...

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO {valor})')

    def detalhes(self, msg=''):
        print(f'O seu saldo é {self.saldo:.2f} {msg}')


class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo
        
        print('Não foi possível sacar o valor desejado')
        self.detalhes(f'(SAQUE NEGADO {valor})')

    def __repr__(self):
        return f'{self.__class__.__name__}({self.agencia!r}, {self.conta!r}, {self.saldo!r})'    


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo=0, limite=0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo
        
        print('Não foi possível sacar o valor desejado')
        print(f'Seu limite é {-self.limite:.2f}')
        self.detalhes(f'(SAQUE NEGADO {valor})')

    def __repr__(self):
        return f'{self.__class__.__name__}({self.agencia!r}, {self.conta!r}, {self.saldo!r}, {self.limite!r})'


if __name__ == '__main__':
    cp1 = ContaPoupanca(111, 222, 0)
    cp1.sacar(1)
