# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

Salário = float(input("Digite o valor do salário: R$ ")) 
Aumento = 0.15
Calculo_do_aumento = (Salário * Aumento)
Valor_com_aumento = Salário + Calculo_do_aumento 
print(f"O valor do novo salário do funcionário, com aumento de 15% é de R$ {Valor_com_aumento:.2f}")