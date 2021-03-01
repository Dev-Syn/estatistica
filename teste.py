import numpy as np

dados = np.loadtxt('dados.txt')

lista = np.array(dados)

lista_ordenada = np.sort(lista)

tam = len(lista_ordenada)


##############################################################
#Calculo da média
soma = 0
i = 0

while i < tam:
    soma += lista_ordenada[i]
    i+=1

media = soma / tam

print("Esse é o array em ordem crescente: \n" , lista_ordenada)
print("A média é: ", round(media))

##############################################################
#calculo da moda.
cont = 0
maior = 0

for i in range(tam):
    cont = 0 #reiniciando o contador caso, haja uma nova ocorrência
    for j in range(tam):
        if (lista_ordenada[i] == lista_ordenada[j]):
            cont += 1
    if (maior < cont) :
        maior = cont
        moda = lista_ordenada[i]

print("A moda é: ", moda, "E se repete: ", maior)
##############################################################
#calculo da mediana.

if tam % 2 == 0:
    #se for par
    j =int(tam / 2)
    # print(j)
    j2 = int(j + 1)
    # print(j2)

    n1 = lista_ordenada[j]
    n2 = lista_ordenada[j2]

    print(n1, n2)
    mediana = (n1 + n2) / 2
    print("Comprimento par.")

else: 
    #se for impar
    con_par = int((tam - 1) / 2)
    mediana = lista_ordenada[con_par + 1]
    print("Comprimento ímpar.")

print("A mediana é: ", mediana)
