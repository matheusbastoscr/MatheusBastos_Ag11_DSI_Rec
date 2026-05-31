from colorama import Fore, Style, init

# Inicializa o Colorama
init(autoreset=True)

# Lista com os níveis e situações do reservatório
niveis_reservatorio = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

# Função que retorna a cor conforme o nível
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

# Simulação dos níveis do reservatório
for i in range(len(niveis_reservatorio)):
    nivel = i + 1
    cor = definir_cor(nivel)

    print(cor + f"Nível {nivel}: {niveis_reservatorio[i]}")

# Restaura o estilo padrão do terminal
print(Style.RESET_ALL)