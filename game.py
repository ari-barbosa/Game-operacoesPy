from models.calcular import Calcular

def main() -> None:
    pontos: int = 0  # Iniciando o jogo com 0 pontos.
    jogar(pontos)


def jogar(pontos: int) -> None:  # Função principal

    # Recebendo a dificuldade do jogo
    dificuldade: int = int(input("Informe o nível de dificuldade desejado [1, 2, 3 ou 4]:"))

    calc: Calcular = Calcular(dificuldade)  # Instanciar um objeto informando a dificuldade como parametro

    print("Informe o resultado para a seguinte operação: ")
    calc.mostrar_operacao()  # Mostrar a operação

    resultado: int = int(input()) # Jogador informa o resultado

    # Retornando os pontos para o jogador de acordo com suas respostas.
    if calc.checar_resultado(resultado):  # Checando se o resultado do jogador está correto ou não

        pontos += 1  # Caso a resposta seja verdadeira, acrescentar um ponto
        print(f"Você tem {pontos} pontos.")


    # Verificando se o usuario deseja continuar jogando
    continuar: int = int(input("Deseja continuar no jogo? [1 - Sim, 0- Não]"))

    if continuar:
        jogar(pontos)
    else:
        print(f"Você finalizou com {pontos} pontos.")

if __name__ == '__main__':
    main()