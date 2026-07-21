# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

L = float(input("Digite a largura da parede: ")) # Pede para o usuário digitar a largura da parede e armazena na variável L
A = float(input("Digite a altura da parede: ")) # Pede para o usuário digitar a altura da parede e armazena na variável A
área = L * A # Calcula a área da parede multiplicando a largura pela altura e armazena na variável área
Litros = área / 2 # Calcula a quantidade de tinta necessária para pintar a parede, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados e armazena na variável Litros
print(f"Sua parede tem a dimensão de {L} X {A} e sua área é de {área} m².") # Mostra na tela a largura, altura e área da parede digitadas pelo usuário
print(f"Para pintar essa parede, você precisará de {Litros} litros de tinta") # Mostra na tela a largura, altura, área da parede e a quantidade de tinta necessária para pintá-la
