import numpy as np

dados = np.loadtxt('dados.txt')

lista = np.array(dados)

lista_ordenada = np.sort(lista)

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


#### Finalização

media = media(lista_ordenada)

mediana = mediana(lista_ordenada)


print("Dados ordenados: \n", lista_ordenada)
print("A média arredondada é: ", round(media))
print("Nesse caso a mediana é: ", mediana)