CONSTANTE_BONUS = 1000

nome_valido = False
salario_valido = False
percentual_bonus_valido = False

while not nome_valido:
    try:  
        # solicita ao usuário que digite seu nome.
        nome = input("Digite seu nome: ")

        # verifica se o nome está vázio
        if len(nome) == 0:
            raise ValueError("Entrada inválida. Você precisa digitar um nome.") # raise é usada para interromper a execução normal do programa e sinalizar que ocorreu um erro.
        # Verifica se há números no nome
        elif any(char.isdigit() for char in nome): # percorre cada caractere da string (for char in nome), e verifica se é um número (char.isdigit()), se qualquer posição (Any) for numérica retorna True 
            raise ValueError("Entrada inválida. O nome não deve conter números.")
        else:
            print(f"Nome válido: {nome}")
            nome_valido = True

    except ValueError as e:
        print(e)


while not salario_valido:
    try:
        # solicita ao usuário que digite o valor do seu salário, depois converte para decimal (float).
        salario = float(input("Digite seu salário: "))
        if salario < 0:
            raise ValueError("Por favor, digite um valor positivo para o salário.")
        else:
            salario_valido = True
    except ValueError:
        print("Entrada inválida para o salário. Por favor, digite um número.")


while not percentual_bonus_valido:
    try:
        # solicita ao usuário que digite a portcentagem do bônus
        percentagem_bonus = float(input("Digite a porcentagem de seu bônus: "))
        if percentagem_bonus < 0:
            raise ValueError("Por favor, digite um valor positivo para o percentual do bônus.")
        else:
            percentual_bonus_valido = True
    except ValueError:
        print("Entrada inválida para o percentual do bônus. Por favor, digite um número.")

# calcula o valor do bônus
bonus = CONSTANTE_BONUS + (salario * percentagem_bonus)

# imprime a mensagem personalizada com o vlor do bônus
print(f"Olá {nome}, o seu valor bônus foi de R$ {bonus:.2f}")
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus:.2f}.")