import numpy as np

dados = np.loadtxt('dados.txt')

lista = np.array(dados)

lista_ordenada = np.sort(lista)

soma = 0
i = 0
tam = len(lista_ordenada)

while i < tam:
    soma += lista_ordenada[i]
    i+=1

media = soma / tam

print("Esse é o array em ordem crescente: \n" , lista_ordenada)
print("A média é: ", round(media))

##############################################################

cont_r = 0
i = 0

while i < tam:
    if i == lista_ordenada[i]:
        repete = lista_ordenada[i]
        cont_r += 1
    i += 1

############################################################

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
