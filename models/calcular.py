from random import randint


class Calcular:
    def __init__(self: object, dificuldade: int) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1: int = self._gerar_valor
        self.__valor2: int = self._gerar_valor
        self.__operacao: int = randint(1, 3)  # 1 = somar, 2 = diminuir, 3 = multiplicar
        self.__resultado: int = self._gerar_resultado

    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade

    @property
    def valor1(self: object) -> int:
        return self.__valor1

    @property
    def valor2(self: object) -> int:
        return self.__valor2

    @property
    def operacao(self: object) -> int:
        return self.__operacao

    @property
    def resultado(self: object) -> int:
        return self.__resultado

    def __str__(self: object) -> str:
        # Criando a variavel de operação, op = operacao.
        op: str = ""

        # Se a variavel for igual a 1 entao é soma.
        if self.operacao == 1:
            op = "Somar"

        # Se a variavel for igual a 2 entao é diminuir.
        elif self.operacao == 2:
            op = "Diminuir"

        # Se a variavel for igual a 1 entao é Multiplicar.
        elif self.operacao == 3:
            op = "Multiplicar"

        # Se a variavel for igual a 3 entao é invalido.
        else:
            op = "Operação desconhecida"
        return f"Valor 1: {self.valor1} \nValor 2: {self.valor2}\nDificuldade: {self.dificuldade}\nOperação: {op}"

    @property
    def _gerar_valor(self: object) -> int:

        # Dificuldade super fácil, irá gerar um valor aleatorio de 0 a 10.
        if self.dificuldade == 1:
            return randint(0, 10)

        # Dificuldade fácil, irá gerar um valor aleatorio de 0 a 100.

        elif self.dificuldade == 2:
            return randint(0, 100)

        # Dificuldade média, irá gerar um valor aleatorio de 0 a 1.000.

        elif self.dificuldade == 3:
            return randint(0, 1000)

        # Dificuldade dificil, irá gerar um valor aleatorio de 0 a 10.000.
        elif self.dificuldade == 4:
            return randint(0, 10000)

        # Dificuldade hard, irá gerar um valor aleatorio de 0 a 100.000.
        else:
            return randint(0, 100000)

    @property
    def _gerar_resultado(self: object) -> int:

        if self.operacao == 1:  # Somar
            return self.valor1 + self.valor2  # Somando os valores.

        elif self.operacao == 2:  # Diminuir
            return self.valor1 - self.valor2  # Subtraindo os valores

        else:  # Multiplicando
            return self.valor1 * self.valor2  # Multiplicando os valores

    @property
    # Informa o simbolo de cada operação
    def _op_simbolo(self: object) -> str:

        if self.operacao == 1:  # Soma
            return '+'

        elif self.operacao == 2:  # Subtração
            return '-'

        else:
            return '*'  # Multiplicação

    def checar_resultado(self: object, resposta: int) -> bool:
        certo: bool = False  # Iniciando a verificação como falso.

        if self.resultado == resposta:  # Verifica se o resultado é igual a resposta do jogador

            print("Resposta Correta!")
            certo = True  # Altera a verificação como correta.

        else:
            print("Resposta Incorreta!")

        # Imprimindo a operação na tela e o resultado correto.
        print(f"{self.valor1} {self._op_simbolo} {self.valor2} = {self.resultado}")
        return certo

    # Essa função será chamada no Game.
    def mostrar_operacao(self: object) -> None:
        print(f"{self.valor1} {self._op_simbolo} {self.valor2} = ?")
