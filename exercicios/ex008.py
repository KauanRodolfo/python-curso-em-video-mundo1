# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input("Digite um valor em metros: "))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print(f"O valor digitado em metros é {m} m. \n{km} km \n{hm} hm \n{dam} dam \n{dm} dm \n{cm} cm \n{mm} mm")
