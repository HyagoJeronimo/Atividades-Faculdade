def exemplo_while_contagem(limite: int) -> list[int]:

    numeros: list[int] = []
    contador = 1

    while contador <= limite:
        # registra o estado atual antes de avançar o contador.
        numeros.append(contador)
        contador += 1

    return numeros

print(exemplo_while_contagem(2))