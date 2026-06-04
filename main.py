dias = ["segunda", "terça", "quarta", "quinta", "sexta"]
horarios = ["manhã", "tarde", "noite", "madrugada"]

def ler_temperaturas():
    matriz = []
    print("Insira as temperaturas (em °C) registradas durante a semana.")
    for dia in range(len(dias)):
        linha = []
        for hora in range(len(horarios)):
                while True:
                    try:
                        linha.append(float(input(f"{dias[dia]} de {horarios[hora]}: ")))
                        break
                    except:
                        print("Erro: Insira um numero! tente novamente.")
        matriz.append(linha)
    return matriz

def mostrar_tabela(matriz):
    print(f"           manhã   tarde   noite   madrugada")
    for dia in range(len(matriz)):
        print(f"{dias[dia]:>7}", end=" ")
        for hora in range(len(matriz[dia])):
            print(f"{matriz[dia][hora]:>7}", end=" ")
        print()

def medias(matriz):
    print("\nMedia de temperaturas de cada dia:")
    for dia in range(len(matriz)):
        soma = 0
        print(f"{dias[dia]}:", end=" ")
        for hora in range(len(matriz[dia])):
            soma += matriz[dia][hora]
        print(f"{soma/4}°C")
    print("\nMedia de temperaturas de cada horario:")
    for hora in range(len(matriz[0])):
        soma = 0
        print(f"{horarios[hora]}:", end=" ")
        for dia in range(len(matriz)):
            soma += matriz[dia][hora]
        print(f"{soma/5}°C")

def maior_menor(matriz):
    menor = [matriz[0][0],0,0]
    maior = [matriz[0][0],0,0]
    for dia in range(len(matriz)):
        for hora in range(len(matriz[0])):
            if menor[0] > matriz[dia][hora]:
                menor = [matriz[dia][hora], dia, hora]
            elif maior[0] < matriz[dia][hora]:
                maior = [matriz[dia][hora], dia, hora]
    print("\nMaior temperatura registrada:")
    print(f"{dias[maior[1]]} de {horarios[maior[2]]}: {maior[0]}°C")
    print("\nMenor temperatura registrada:")
    print(f"{dias[menor[1]]} de {horarios[menor[2]]}: {menor[0]}°C")

def consultar(matriz):
    print("\nConsulte uma temperatura:")
    while True:
        dia = input("Informe o dia (como escrito na tabela): ")
        if dia in dias:
            break
        else:
            print("Resposta invalida! tente novamente.")
    while True:
        hora = input("Informe o horario (como escrito na tabela): ")
        if hora in horarios:
            break
        else:
            print("Resposta invalida! tente novamente.")
    print(f"Temperatura na {dia} de {hora} foi {matriz[dias.index(dia)][horarios.index(hora)]}°C")

#matriz = ler_temperaturas()
matriz_teste = [[1.0, 2.0, 3.0, 4.0], [5.0, 6.0, 7.0, 8.0], [9.0, 10.0, 11.0, 12.0], [13.0, 14.0, 15.0, 16.0], [17.0, 18.0, 19.0, 20.0]]
mostrar_tabela(matriz_teste)
medias(matriz_teste)
maior_menor(matriz_teste)
consultar(matriz_teste)