# Escreva um programa que leia um valor em metros e o exiba convertido em todas as outras medidas de comprimento: quilômetros, hectômetros, decâmetros, decímetros, centímetros e milímetros.

m = float(input("Digite um valor em metros: ")) # Pede para o usuário digitar um valor em metros e armazena na variável m
km = m / 1000 # Converte o valor em metros para quilômetros e armazena na variável km
hm = m / 100 # Converte o valor em metros para hectômetros e armazena na variável hm
dam = m / 10 # Converte o valor em metros para decâmetros e armazena na variável dam
dm = m * 10 # Converte o valor em metros para decímetros e armazena na variável dm
cm = m * 100 # Converte o valor em metros para centímetros e armazena na variável cm
mm = m * 1000 # Converte o valor em metros para milímetros e armazena na variável mm
print(f"O valor digitado em metros é {m} m. \n{km} km \n{hm} hm \n{dam} dam \n{dm} dm \n{cm} cm \n{mm} mm") # Mostra na tela o valor digitado em metros e as suas conversões para as outras medidas de comprimento
