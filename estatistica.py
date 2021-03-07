import numpy as np

dados = np.loadtxt('dados_impar.txt')

lista = np.array(dados) # convertemos o conteúdo da variável em um array do tipo tratado pela biblioteca.

nl = lista.astype(int) 

lista_ordenada = np.sort(nl) #criando uma variável que recebe o conteúdo do vetor ordenado de forma crescente.

#lista_teste = [1,3,4,5,6,7,6,5,6,7,6,7]

tam = len(lista_ordenada) 


#Calculo de quadrantes.
q1 = lista_ordenada[round((tam * 0.25)-1)] # Essa linha eu usei a lógica de porcentagem pra definir o primeiro quadrante.
q3 = lista_ordenada[round(tam*0.75)] # mesma coisa para o 3º


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

        #print(n1, n2)
        mediana = (n1 + n2) / 2
        print("Comprimento par.")

        return mediana

    else: 
        #se for impar
        con_par = int((tam - 1) / 2)
        mediana = lista_ordenada[con_par + 1]
        print("Comprimento ímpar.")
        
        return mediana

''' Essa função  recebe a lista como argumento, e aqui ela compara se for impar ou par, como a eli disse. e no caso ela tem 2 returns, um para caso for par, e outro para caso for impar. '''


def moda(lista):
    #tam = len(lista)
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

############################### Finalização

print("Dados ordenados: \n", lista_ordenada)

print("O primeiro quartil é delimitado por: ", q1, ".")

mediana = mediana(lista_ordenada)
print("Nesse caso a mediana é: ", mediana, "(Segundo Quartil.)")

print("O valor que delimita o terceiro quartil é: ", q3, ".")

moda, maior = moda(lista_ordenada)
print("A moda entre os dados é: ", moda, "E se repitiu: ", maior, "vezes.")

media = media(lista_ordenada)
print("A média arredondada dos dados é: ", round(media), ".")


'''O vetor ordenado, O valor do primeiro quartil, A mediana (que é o valor do segundo quartil), O valor do terceiro quartil, a moda ocorrente no vetor, e a média dos dados no vetor'''