import random # Importa a biblioteca para gerar números aleatórios (usada pelo computador)

# Cria o tabuleiro do jogador (10x10) preenchido com espaços vazios " "
tabuleiro_jogador = [[" " for _ in range(10)] for _ in range(10)]

# Cria o tabuleiro do computador (10x10) preenchido com espaços vazios " "
tabuleiro_computador = [[" " for _ in range(10)] for _ in range(10)]

# Lista com as letras que representam as linhas do tabuleiro
coordenadas_linha = ["A","B","C","D","E","F","G","H","I","J"]

# Lista com as siglas de cada tipo de navio
embarcacoes = ["P","T","C","S","D"]

#Utilizamos estas letras para abreviar o nome das embarcações
nome_embarcacoes = ["Porta aviões","Navio tanque","Contratorpedeiro","Submarino","Destroier"]

# Inicializa a pontuação do jogador humano em zero
pontos_jogador = 0

# Inicializa a pontuação do computador em zero
pontos_computador = 0

# Lista com os pontos que cada navio dá quando é atingido
pontos_embarcação = [5,4,3,2,1]

# Define quem começa jogando (neste caso, o primeiro turno chama o Jogador humano)
jogadas = "Computador"

def desenho_tabuleiro():
    #função que desenha o tabuleiro de ambos jogadores
    print("            Tabuleiro jogador                                  Tabuleiro computador")
    print("    1   2   3   4   5   6   7   8   9   10                1   2   3   4   5   6   7   8   9   10")
    # variável utilizada para preecher a liha detro dos laços de liha  e coluuan do tabuleiro
    strlinha =""
    for linha in range(10): # Passa por cada uma das 10 linhas do jogo
        # liha que coloca a coordenada da linha entra A e J para iniciar o print
        strlinha = coordenadas_linha[linha]+" | "

        for coluna in range(10): # Adiciona as 10 colunas do tabuleiro do jogador
            strlinha = strlinha + tabuleiro_jogador[linha][coluna]+" | "

        # Adiciona o espaço do meio e a letra da linha para o tabuleiro do computador
        strlinha = strlinha + "          " + coordenadas_linha[linha]+" | "

        for col_jogador in range(10): # Adiciona as 10 colunas do computador
            letra_pos_comp = " "
            # testa se a poicao do tab computador é um tiro, caso contrario mostra em branco na tela
            if tabuleiro_computador[linha][col_jogador] == "X":
               letra_pos_comp = "X"
            strlinha = strlinha + letra_pos_comp+" | "
        print(strlinha) # Imprime a linha completa na tela com os dois tabuleiros montados

    # Imprime o placar de pontos atualizado abaixo dos tabuleiros
    print("            Pontos jogador: " + str(pontos_jogador) + "                                  Pontos computador: " + str(pontos_computador))

def tab_computador():
    #funcao que define as jogadas aleatorias do computador
    for n_embarcacoes in range(5): # Passa por cada um dos 5 navios
        while True: # Repete até achar uma posição livre
            lin = random.randint(0, 9) # Sorteia uma linha de 0 a 9
            col = random.randint(0, 9) # Sorteia uma coluna de 0 a 9
            # testa se a posição randomica gerada já mão foi utilizada
            if not valida_pos_oculpada_computador(lin,col):
               tabuleiro_computador[lin][col] = embarcacoes[n_embarcacoes] # Coloca a letra do navio na matriz
               break # Sai do 'while True' e vai para o próximo navio

def validacao_lin(linha: str):
    #essa funcao define se o usuario digitar uma letra que esta errada
    if not linha: # Se o jogador apertar 'Enter' sem digitar nada, dá erro
        return False
    if len(linha) > 1: # Se o jogador digitar mais de uma letra (ex: 'AA'), dá erro
        return False
    letra = linha[0].upper() # Pega a primeira letra e transforma em maiúscula
    letras_validas = "ABCDEFGHIJ" # String com os caracteres permitidos

    # Verifica se a letra está na lista de válidas
    if letra in letras_validas:
        return True # Retorna verdadeiro se a letra estiver certa
    else:
        return False # Retorna falso se a letra não existir no tabuleiro

def validacao_col(coluna: str):
    #essa funcao define se o usuario digitar um numero que esta errado
    if coluna.isdigit(): # Verifica se o que foi digitado é realmente um número
        numero = int(coluna) # Converte o texto para número inteiro
        # 2. Verifica se o número está no intervalo de 1 a 10
        if 1 <= numero <= 10:
            return True # Retorna verdadeiro se estiver entre 1 e 10
    return False # Retorna falso se for um texto ou um número fora do limite

def letra_para_indice(letra_digitada: str):
    # Converte para maiúsculo (ex: "c" vira "C")
    letra = letra_digitada.upper()

    # Encontra a posição da letra na lista
    indice = coordenadas_linha.index(letra)
    return indice # Retorna o número do índice encontrado (ex: 'A' vira 0, 'B' vira 1...)

def valida_pos_oculpada_jogador(linha: int, coluna: int):
    # Verifica se a posição do tabuleiro do jogador já tem um navio
    if tabuleiro_jogador[linha][coluna] != " ":
        return True # Retorna verdadeiro (está ocupada)
    else:
        return False # Retorna falso (está vazia/livre)

def valida_pos_oculpada_computador(linha: int, coluna: int):
    # Verifica se a posição do tabuleiro do computador já tem um navio
    if tabuleiro_computador[linha][coluna] != " ":
        return True # Retorna verdadeiro (está ocupada)
    else:
        return False # Retorna falso (está vazia/livre)

def tab_jogador():
    # Loop que passa por cada um dos 5 navios para o jogador posicionar
    for n_embarcacoes in range(5):
        print("Onde você gostaria de posicionar os seu " + nome_embarcacoes[n_embarcacoes] + "?")
        while True: # Loop para garantir que a posição escolhida seja válida e livre
            while True: # Loop para validar a digitação da linha
                lin = input("Digite a linha utilizando (A até J como referência): ")
                if validacao_lin(lin):
                    break # Linha correta, sai do loop de validação
                else:
                    print("Digite apenas valores entre A e J!")
            while True: # Loop para validar a digitação da coluna
                col = input("Digite a coluna (1 até 10 como referência): ")
                if validacao_col(col):
                    break # Coluna correta, sai do loop de validação
                else:
                    print("Digite apenas valores entre 1 e 10!")

            # Verifica se o lugar escolhido já não está guardando outro navio do jogador
            if valida_pos_oculpada_jogador(letra_para_indice(lin),int(col)-1):
                print("Posição já ocupada, digite outra por favor!")
            else:
                break # Posição está totalmente livre, sai do loop principal de escolha

        # Grava a letra da embarcação na posição correta da matriz do jogador
        tabuleiro_jogador[letra_para_indice(lin)][int(col) - 1] = embarcacoes[n_embarcacoes]
        desenho_tabuleiro() # Desenha o tabuleiro atualizado para mostrar onde o navio ficou

def tiro_jogador(pontos_jogador_atual):
    pos_tiro = " "
    print("Digite as cordenadas para seu tiro:")
    while True: # Loop para receber e validar a linha onde o jogador quer atirar
        lin = input("Digite a linha utilizando (A até J como referência): ")
        if validacao_lin(lin):
           break
        else:
            print("Digite apenas valores entre A e J!")
    while True: # Loop para receber e validar a coluna onde o jogador quer atirar
        col = input("Digite a coluna (1 até 10 como referência): ")
        if validacao_col(col):
            break
        else:
            print("Digite apenas valores entre 1 e 10!")

    # Verifica se o tiro atingiu um navio escondido no tabuleiro do computador
    if valida_pos_oculpada_computador(letra_para_indice(lin),int(col)-1):
        pos_tiro = tabuleiro_computador[letra_para_indice(lin)][int(col)-1]

        if pos_tiro != "X": # Se não for um local que já foi atingido antes
            print(nome_embarcacoes[embarcacoes.index(pos_tiro)] + " Atigindo!")
            # Soma os pontos do navio atingido aos pontos atuais do jogador humano
            pontos_jogador_atual = pontos_jogador_atual + pontos_embarcação[embarcacoes.index(pos_tiro)]
        else:
            print("Você já atirou nessa posição!")
    else:
        print("Tiro na água!") # Caso a posição estivesse vazia (" ")

    # Marca a matriz do computador com "X" para registrar que houve um tiro ali
    tabuleiro_computador[letra_para_indice(lin)][int(col)-1] = "X"
    return pontos_jogador_atual # Devolve o novo valor dos pontos do jogador para fora da função

def tiro_computador(pontos_computador_atual):
    lin = random.randint(0, 9) # Computador sorteia a linha do tiro de 0 a 9
    col = random.randint(0, 9) # Computador sorteia a coluna do tiro de 0 a 9

    # Mostra na tela a coordenada que o computador escolheu atacar
    print("Computador atirou na posição: " + coordenadas_linha[lin] + "-" + str(col+1))

    # Verifica se o computador acertou algum navio no tabuleiro do jogador humano
    if valida_pos_oculpada_jogador(lin,col):
        pos_tiro = tabuleiro_jogador[lin][col]

        if pos_tiro != "X": # Se o computador não repetiu um tiro certeiro anterior
            print(nome_embarcacoes[embarcacoes.index(pos_tiro)] + " Atigindo!")
            # Soma os pontos do navio destruído à pontuação global do computador
            pontos_computador_atual = pontos_computador_atual + pontos_embarcação[embarcacoes.index(pos_tiro)]
        else:
            print("Computador já atirou nessa posição!")
    else:
        print("Tiro na água!") # Se o computador acertou um espaço em branco

    # Marca a matriz do jogador com "X" para desenhar o estrago na tela
    tabuleiro_jogador[lin][col] = "X"
    return pontos_computador_atual # Devolve os pontos atualizados do computador para o jogo

tab_computador()
tab_jogador()
desenho_tabuleiro()

while pontos_jogador < 15 and pontos_computador < 15:
    if jogadas == "Computador":
        pontos_jogador = tiro_jogador(pontos_jogador)
        jogadas = "Jogador"
    else:
        pontos_computador = tiro_computador(pontos_computador)
        jogadas = "Computador"
    desenho_tabuleiro()


print("\n===== FIM DE JOGO =====")
print(f"Pontos do Jogador: {pontos_jogador}")
print(f"Pontos do Computador: {pontos_computador}")

if pontos_jogador >= 15:
    print("Parabéns! Você venceu!")
else:
    print("O computador venceu!")