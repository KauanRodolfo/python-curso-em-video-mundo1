# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US1.00 = R$ 3,27

n = float(input("Digite quanto dinheiro você tem na carteira: R$ "))
R = 3.27
US = n / R
print(f"Com R$ {n:.2f} você pode comprar US$ {US:.2f}")