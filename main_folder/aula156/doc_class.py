class Foo:
    """esse e uma doc de class"""

    def soma(self, x: int | float, y: int | float) -> int | float:
        """Soma x e y
        Este módulo contém funções e exemplos de documentação de funções.
        A função soma você já conhece bastante.
        :param x: Número 1
        :type x: int or float
        :param y: Número 2
        :type y: int or float
        :return: A soma entre x e y
        :rtype: int or float
        """
        return x + y

    def bar(self) -> int:
        """
        ele faz:

        :raises NotImplementedError: se o metodo nao for definido

        """
        raise NotImplementedError('teste')
