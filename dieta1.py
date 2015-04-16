def TMB():
    peso=70
    altura=164
    idade=30    
    return 88.36+(13.4*peso)+(4.8*altura)-(5.7*idade)
print(TMB())

def qtdecalorica():  #quantidade energetica em kcal necessitada 
    return TMB()*1.725 #o numero que multiplica o tmb é 1.725 porque o nivel de atividade do usuario é alto
print(qtdecalorica()) #só para saber qual a necessidade energetica, que é de 2833.416kcal

arquivo_usuario = open("usuario.csv","r")
leitura_usuario = arquivo_usuario.readlines()
#print(leitura_usuario)
lista=[]
lista2=[]
for i in leitura_usuario[3:]:
    linha_usuario = i.split(',')
    if i == 3:
        lista1 = lista.append(linha_usuario[1:])
    print(lista1)
    else:
        break    
    


arquivo_alimentos = open('alimentos.csv','r')
leitura_alimentos = arquivo_alimentos.readlines()
dict_alimentos = dict()
for e in leitura_alimentos[1:]:
    linha_alimentos = e.split(',')
    dict_alimentos[linha_alimentos[0]] = linha_alimentos[1], linha_alimentos[2], linha_alimentos[3], linha_alimentos[4], linha_alimentos[5]
#print(dict_alimentos)
