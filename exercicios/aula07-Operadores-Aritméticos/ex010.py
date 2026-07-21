# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US1.00 = R$ 3,27

n = float(input("Digite quanto dinheiro você tem na carteira: R$ ")) # Pede para o usuário digitar quanto dinheiro ele tem na carteira e armazena na variável n
R = 3.27 # Valor do dólar em reais
US = n / R # Calcula quantos dólares a pessoa pode comprar com o dinheiro que ela tem na carteira e armazena na variável US
print(f"Com R$ {n:.2f} você pode comprar US$ {US:.2f}") # Mostra na tela quanto dinheiro a pessoa tem na carteira e quantos dólares ela pode comprar, formatado com duas casas decimais