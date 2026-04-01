def ex1_contar_pares_while(inicio: int, fim: int) -> int:

    quantidade_pares = 0
    atual = inicio

    while atual <= fim:
        if atual % 2 == 0:
            quantidade_pares += 1
        atual += 1

    return quantidade_pares

print(ex1_contar_pares_while(1, 10))