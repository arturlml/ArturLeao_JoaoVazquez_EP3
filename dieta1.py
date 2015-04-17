def TMB():
    peso = 70
    altura = 164
    idade = 30    
    return 88.36+(13.4*peso)+(4.8*altura)-(5.7*idade)

print(TMB())  #Nível basal do metabolismo

def qtdecalorica():  #quantidade energetica em kcal necessitada 
    return TMB()*1.725  #o numero que multiplica o tmb é 1.725 porque o nivel de atividade do usuario é alto
print(qtdecalorica())  #só para saber qual a necessidade energetica, que é de 2833.416kcal
        

''' Criando um dicionário com as informaões do que o usuário comeu '''

dict_usuario = dict()
lista_consumido = []
datas = []

arquivo_usuario = open("usuario.csv","r")
leitura_usuario = arquivo_usuario.readlines()

for y in range(3,len(leitura_usuario)):  #comeca do 3 porque as informações que importam só começam depois da terceira linha
    linha_usuario = leitura_usuario[y].split(',')  #cria uma lista separada por vírgula para cada linha do excel
    lista_consumido.append(linha_usuario)  #adiciona à lista_consumido as linhas como listas

for b in lista_consumido:   #adiciona as datas que o usuario quiser caso hajam mais dias de dieta
    if b[0] not in datas:
        datas.append(b[0]) #adiciona a lista de datas as datas presentes nas listas com as informações
        
for a in datas:
    dict_usuario[a] = []
    for c in lista_consumido:
        if a == c[0]:                               
            dict_usuario[a].append([c[1],c[2]])  #se a chave do dic for igual ao primeiro termo da lista_consumido adicionar os dois proximos elementos da lista_consumida ao dicionário 

print(dict_usuario)

''' Criar um dicionário com as informações de todos os alimentos fornecidos '''

arquivo_alimentos = open('alimentos.csv','r')
leitura_alimentos = arquivo_alimentos.readlines()
dict_alimentos = dict()
for e in leitura_alimentos[:]:
    linha_alimentos = e.split(',')
    dict_alimentos[linha_alimentos[0]] = linha_alimentos[1], linha_alimentos[2], linha_alimentos[3], linha_alimentos[4], linha_alimentos[5]
print(dict_alimentos)

