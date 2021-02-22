import re
########### Teste de upload de arquivo ###########

documento = open("dados.txt", "r")
### -> Teste bem sucedido. print(documento.read())

listalimpa = []

for dado in documento:
    #Divido as string
    for x in dado.split(','):
    #aqui substituo os caracteres indesejados por nada usando o método sub, do módulo re
        listalimpa.append(int(re.sub('\[|\]|,|''\s*', "", x)))

informacao = sorted(listalimpa)

print(informacao)



