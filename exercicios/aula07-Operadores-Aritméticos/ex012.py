# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

Produto = float(input("Digite o valor do produto: R$ ")) # Pede para o usuário digitar o valor do produto e armazena na variável Produto
Desconto = 0.05 # Define o desconto como 5%
Calculo_do_desconto = (Produto * Desconto) # Calcula o valor do desconto
Valor_com_desconto = Produto - Calculo_do_desconto # Calcula o valor do produto com desconto
print(f"O valor do produto com desconto de 5% é de R$ {Valor_com_desconto:.2f}") # Mostra na tela o valor do produto com desconto, formatado com duas casas decimais
