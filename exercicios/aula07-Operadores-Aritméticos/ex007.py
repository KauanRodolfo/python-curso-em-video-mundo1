# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input("Digite a primeira nota: ")) # Pede para o usuário digitar a primeira nota e armazena na variável n1
n2 = float(input("Digite a segunda nota: ")) # Pede para o usuário digitar a segunda nota e armazena na variável n2
média = (n1 + n2) / 2 # Calcula a média das duas notas e armazena na variável média
print(f"A média entre as notas {n1} e {n2} é igual a {média:.2f}") # Mostra na tela a média das duas notas digitadas pelo usuário, formatada com duas casas decimais