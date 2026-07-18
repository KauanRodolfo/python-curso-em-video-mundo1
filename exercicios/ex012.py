# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

Produto = float(input("Digite o valor do produto: R$ "))
Desconto = 0.05 
Calculo_do_desconto = (Produto * Desconto) / 100
Valor_com_desconto = Produto - Calculo_do_desconto
print(f"O valor do produto com desconto de 5% é de R$ {Valor_com_desconto:.2f}")
