# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

Salário = float(input("Digite o valor do salário: R$ ")) # Pede para o usuário digitar o valor do salário e armazena na variável Salário
Aumento = 0.15 # Define o aumento como 15%
Calculo_do_aumento = (Salário * Aumento) # Calcula o valor do aumento
Valor_com_aumento = Salário + Calculo_do_aumento  # Calcula o valor do salário com aumento
print(f"O valor do novo salário do funcionário, com aumento de 15% é de R$ {Valor_com_aumento:.2f}") # Mostra na tela o valor do novo salário do funcionário, com aumento de 15%, formatado com duas casas decimais