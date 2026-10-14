def quick_sort(valores):
    # Listas com zero ou um elemento ja estao ordenadas.
    if len(valores) <= 1:
        return valores.copy()

    # Escolhe o elemento do meio como pivo.
    pivo = valores[len(valores) // 2]

    menores = []
    iguais = []
    maiores = []

    # Separa os valores de acordo com o pivo.
    for valor in valores:
        if valor < pivo:
            menores.append(valor)
            continue
        if valor == pivo:
            iguais.append(valor)
            continue
        maiores.append(valor)

    # Ordena as partes menores e maiores recursivamente.
    return quick_sort(menores) + iguais + quick_sort(maiores)


# Testa a funcao com uma lista fora de ordem.
print(quick_sort([7, 3, 9, 1, 5]))