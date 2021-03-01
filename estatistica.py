import numpy as np

dados = np.loadtxt('dados.txt')

lista = np.array(dados)

nl = lista.astype(int)

lista_ordenada = np.sort(nl)

#lista_teste = [1,3,4,5,6,7,6,5,6,7,6,7]

tam = len(lista_ordenada)

def media(lista):
    soma = 0
    i = 0

    while i < tam:
        soma += lista[i]
        i += 1
    
    return soma / tam

def mediana(lista):

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

        return mediana

    else: 
        #se for impar
        con_par = int((tam - 1) / 2)
        mediana = lista_ordenada[con_par + 1]
        print("Comprimento ímpar.")
        
        return mediana


def moda(lista):
    tam = len(lista)
    cont = 0
    maior = 0

    for i in range(tam):
        cont = 0 #reiniciando o contador caso, haja uma nova ocorrência
        for j in range(tam):
            if (lista[i] == lista[j]):
                cont += 1
        if (maior < cont) :
            maior = cont
            moda = lista[i]

    return moda, maior



#### Finalização


print("Dados ordenados: \n", lista_ordenada)

media = media(lista_ordenada)
print("A média arredondada é: ", round(media))

mediana = mediana(lista_ordenada)
print("Nesse caso a mediana é: ", mediana)

moda, maior = moda(lista_ordenada)
print("A moda é: ", moda, "E se repitiu: ", maior, "vezes.")
