def TMB():
    peso=70
    altura=164
    idade=30    
    return 88.36+(13.4*peso)+(4.8*altura)-(5.7*idade)
print(TMB() )#Nível basal do metabolismo

def qtdecalorica():  #quantidade energetica em kcal necessitada 
    return TMB()*1.725 #o numero que multiplica o tmb é 1.725 porque o nivel de atividade do usuario é alto
print(qtdecalorica()) #só para saber qual a necessidade energetica, que é de 2833.416kcal
dict_usuario = dict()
lista_consumido = []         
datas = []          
arquivo_usuario = open("usuario.csv","r")
leitura_usuario = arquivo_usuario.readlines()
print(leitura_usuario)
for e in range(3,len(leitura_usuario)):
    linha_alimento = leitura_usuario[e].split(',')
    lista_consumido.append(linha_alimento)

for b in lista_consumido:
    if b[0] not in datas:
        datas.append(b[0])
        
for a in datas:
    dict_usuario[a] = []
    for c in lista_consumido:
        if a == c[0]:      
            dict_usuario[a].append([c[1],c[2]])

print(dict_usuario)

arquivo_alimentos = open('alimentos.csv','r')
leitura_alimentos = arquivo_alimentos.readlines()
dict_alimentos = dict()
for e in leitura_alimentos[:]:
    linha_alimentos = e.split(',')
    dict_alimentos[linha_alimentos[0]] = linha_alimentos[1], linha_alimentos[2], linha_alimentos[3], linha_alimentos[4], linha_alimentos[5]
print(dict_alimentos)

