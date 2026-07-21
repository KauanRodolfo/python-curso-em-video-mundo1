#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

n = input("Digite algo: ") ### Função que lê o que o usuário digitar e armazena na variável n

print(f"O tipo primitivo desse valor é {type(n)}") ### Função que mostra o tipo da variável

print(f"Só tem espaços? {n.isspace()}") ### Função que verifica se a variável é composta apenas por espaços

print(f"É um número? {n.isnumeric()}") ### Função que verifica se a variável é composta apenas por números

print(f"É alfabético? {n.isalpha()}") ### Função que verifica se a variável é composta apenas por letras

print(f"É alfanúmerico? {n.isalnum()}") ### Função que verifica se a variável é composta apenas por letras e números

print(f"Está em maiúsculas? {n.isupper()}") ### Função que verifica se a variável está em maiúsculas

print(f"Está em minúsculas? {n.islower()}") ### Função que verifica se a variável está em minúsculas

print(f"Está capitalizada? {n.istitle()}") ### Função que verifica se a variável está capitalizada (primeira letra maiúscula e as demais minúsculas)
