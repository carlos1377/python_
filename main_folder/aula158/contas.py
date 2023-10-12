from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor: float) -> float:
        ...

    def deposito(self, valor: float) -> float:
        self.saldo += valor
        self.details(f'(Depósito {valor})')
        return self.saldo

    def details(self, msg: str = '') -> None:
        print(f'O seu saldo é {self.saldo:.2f} {msg}')
        print('--')

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencia!r},{self.conta!r}, {self.saldo!r})'
        return f'{class_name}{attrs}'


class ContaPoupanca(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        super().__init__(agencia, conta, saldo)

    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.details(f'(Saque {valor})')
            return self.saldo

        print('não foi possivel sacar o valor desejado')
        self.details(f'(Saque negado {valor})')
        return self.saldo


class ContaCorrente(Conta):
    def __init__(
            self, agencia: int, conta: int, saldo: float = 0,
            limite: float = 0
    ) -> None:
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor
        limit_max = -self.limite

        if valor_pos_saque >= limit_max:
            self.saldo -= valor
            self.details(f'(Saque {valor})')
            return self.saldo

        print('não foi possivel sacar o valor desejado')
        print(f'seu limite é {-self.limite:.2f}')
        self.details(f'(Saque negado {valor})')
        return self.saldo

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r},'\
            f' {self.limite!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    cp1 = ContaPoupanca(111, 222, 100)
    cp1.sacar(1)
    cp1.deposito(2)
    cp1.sacar(1)
    print('##')
    cc1 = ContaCorrente(111, 222, 0, 100)
    cc1.sacar(1)
    cc1.deposito(1)
    cc1.sacar(100)
