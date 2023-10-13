import pessoas
import contas


class Banco:
    def __init__(
            self,
            agencias: list[int] | None = None,
            contas: list[contas.Conta] | None = None,
            clientes: list[pessoas.Pessoa] | None = None) -> None:
        self.agencias = agencias or []
        self.contas = contas or []
        self.clientes = clientes or []

    def _check_agencia(self, conta) -> bool:
        if conta.agencia in self.agencias:
            print('agencia True')
            return True
        print('agencia False')
        return False

    def _check_cliente(self, cliente) -> bool:
        if cliente in self.clientes:
            print('cliente True')
            return True
        print('cliente False')
        return False

    def _check_conta(self, conta) -> bool:
        if conta in self.contas:
            print('conta True')
            return True
        print('conta False')
        return False

    def check_conta_has_cliente(self, cliente, conta):
        if conta is cliente.conta:
            print('conta_cliente True')
            return True
        print('conta_cliente False')
        return False

    def autenticar(self, cliente: pessoas.Pessoa, conta: contas.Conta) -> bool:
        return self._check_agencia(conta) and \
            self._check_cliente(cliente) and self._check_conta(conta) and \
            self.check_conta_has_cliente(cliente, conta)

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.contas!r}, {self.clientes!r}'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    c1 = pessoas.Cliente('carlos', 18)
    cc1 = contas.ContaCorrente(111, 222, 3, 100)
    c1.conta = cc1
    c2 = pessoas.Cliente('carlos', 18)
    cp1 = contas.ContaPoupanca(112, 223, 10)
    c2.conta = cp1
    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp1])
    banco.agencias.extend([111, 112])
    print(banco)

    print(banco.autenticar(c1, cp1))
    print('###########')
    print(banco.autenticar(c1, cc1))

    if banco.autenticar(c1, cc1):
        cc1.deposito(80)
        print(c1.conta)
        cc1.sacar(200)
