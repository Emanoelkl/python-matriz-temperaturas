# Mapa de Temperaturas da Semana

Objetivo: praticar matriz (lista de listas), laços, condicionais e funções, gerando um pequeno relatório.

Enunciado

Crie um programa em Python que leia as temperaturas (em °C) registradas ao longo de 5 dias (Seg a Sex) em 4 horários (Manhã, Tarde, Noite, Madrugada).

Você deve armazenar os dados em uma matriz 5x4, onde:

    linhas = dias
    colunas = horários

Depois, o programa deve:

    Mostrar a matriz formatada (tabela simples)
    Calcular e mostrar:

    a média de cada dia
    a média de cada horário
    a maior temperatura registrada e em qual dia/horário ocorreu
    a menor temperatura registrada e em qual dia/horário ocorreu

    Permitir uma consulta:

    o usuário informa dia e horário e o programa mostra a temperatura correspondente
    validar entradas (dia/horário inválidos devem pedir novamente)

Requisitos obrigatórios

    Usar matriz (lista de listas)
    Usar funções (mínimo 4), por exemplo:
        ler_temperaturas()
        mostrar_tabela(matriz)
        medias(matriz)
        maior_menor(matriz)
        consultar(matriz)
    Usar for para percorrer linhas/colunas
    Ter validação simples com if/else
