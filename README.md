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

Executar:

    python main.py

Exemplo de entrada:

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    segunda
    manhã

Exemplo de saída:

    Insira as temperaturas (em °C) registradas durante a semana.
    segunda de manhã: 1
    segunda de tarde: 2
    segunda de noite: 3
    segunda de madrugada: 4
    terça de manhã: 5
    terça de tarde: 6
    terça de noite: 7
    terça de madrugada: 8
    quarta de manhã: 9
    quarta de tarde: 10
    quarta de noite: 11
    quarta de madrugada: 12
    quinta de manhã: 13
    quinta de tarde: 14
    quinta de noite: 15
    quinta de madrugada: 16
    sexta de manhã: 17
    sexta de tarde: 18
    sexta de noite: 19
    sexta de madrugada: 20

                manhã     tarde     noite    madrugada
    segunda     1.0°C     2.0°C     3.0°C     4.0°C
    terça     5.0°C     6.0°C     7.0°C     8.0°C
    quarta     9.0°C    10.0°C    11.0°C    12.0°C
    quinta    13.0°C    14.0°C    15.0°C    16.0°C
    sexta    17.0°C    18.0°C    19.0°C    20.0°C

    Media de temperaturas de cada dia:
    segunda: 2.5°C
    terça: 6.5°C
    quarta: 10.5°C
    quinta: 14.5°C
    sexta: 18.5°C

    Media de temperaturas de cada horario:
    manhã: 9.0°C
    tarde: 10.0°C
    noite: 11.0°C
    madrugada: 12.0°C

    Maior temperatura registrada:
    sexta de madrugada: 20.0°C

    Menor temperatura registrada:
    segunda de manhã: 1.0°C

    Consulte uma temperatura:
    Informe o dia (como escrito na tabela): segunda
    Informe o horario (como escrito na tabela): manhã
    Temperatura na segunda de manhã foi 1.0°C
