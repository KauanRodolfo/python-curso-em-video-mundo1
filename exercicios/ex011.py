# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

L = float(input("Digite a largura da parede: "))
A = float(input("Digitw a altura da parede: "))
área = L * A
Litros = área / 2
print(f"Sua parede tem a dimensão de {L} X {A} e sua área é de {área} m². \nPara pintar essa parede, você precisará de {Litros} litros de tinta")
