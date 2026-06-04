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

matriz = ler_temperaturas()
print(matriz)