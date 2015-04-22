def TMB():
    peso = 70
    altura = 164
    idade = 30    
    return 88.36+(13.4*peso)+(4.8*altura)-(5.7*idade)

#print(TMB())  #Nível basal do metabolismo

def qtdecalorica():  #quantidade energetica em kcal necessitada 
    return TMB()*1.725  #o numero que multiplica o tmb é 1.725 porque o nivel de atividade do usuario é alto
print(qtdecalorica())  #só para saber qual a necessidade energetica, que é de 2833.416kcal
 
def IMC():
    return (1.3*70)/(1.64**2.5)
print(IMC()) #deu 26.4 e portanto a pessoa esta com sobrepeso
       

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


''' Criar um dicionário com as informações de todos os alimentos fornecidos '''

arquivo_alimentos = open('alimentos.csv','r')
leitura_alimentos = arquivo_alimentos.readlines()
dict_alimentos = dict()
for e in leitura_alimentos[:]:
    linha_alimentos = e.split(',')
    dict_alimentos[linha_alimentos[0]] = linha_alimentos[1], linha_alimentos[2], linha_alimentos[3], linha_alimentos[4], linha_alimentos[5]
dict_alimentos['IOGURTE'][3]

'''06/04/15'''
'''INFORMACOES DO IOGURTE INGERIDO '''

proteina_iogurte = (float(dict_usuario['06/04/15'][0][1]) * float(dict_alimentos['IOGURTE'][2]))/100
#print(proteina_iogurte) #calculando proteina presente na qtde ingerida pelo usuario no iogurte

carbo_iogurte = (float(dict_usuario['06/04/15'][0][1]) * float(dict_alimentos['IOGURTE'][3]))/100
#print(carbo_iogurte)  #calculando carbo presente na qtde ingerida pelo usuario no iogurte

calorias_iogurte = (float(dict_usuario['06/04/15'][0][1]) * float(dict_alimentos['IOGURTE'][1]))/100
#print(calorias_iogurte)

gordura_iogurte = (float(dict_usuario['06/04/15'][0][1]) * float(dict_alimentos['IOGURTE'][4]))/100
#print(gordura_iogurte)

'''INFORMACOES DO SUCO DE LARANJA E CENOURA INGERIDO''' 
proteina_suco = (float(dict_usuario['06/04/15'][3][1]) * float(dict_alimentos['SUCO DE LARANJA E CENOURA'][2]))/100
#print(proteina_suco)

carbo_suco = (float(dict_usuario['06/04/15'][3][1]) * float(dict_alimentos['SUCO DE LARANJA E CENOURA'][3]))/100
#print(carbo_suco)

calorias_suco = (float(dict_usuario['06/04/15'][3][1]) * float(dict_alimentos['SUCO DE LARANJA E CENOURA'][1]))/100
#print(calorias_suco)

gordura_suco = (float(dict_usuario['06/04/15'][3][1]) * float(dict_alimentos['SUCO DE LARANJA E CENOURA'][4]))/100
#print(gordura_suco)

'''INFORMACOES DO MAMAO PAPAYA'''

proteina_mamao = (float(dict_usuario['06/04/15'][1][1]) * float(dict_alimentos['MAMAO PAPAYA'][2]))/100
#print(proteina_mamao)

carbo_mamao = (float(dict_usuario['06/04/15'][1][1]) * float(dict_alimentos['MAMAO PAPAYA'][3]))/100
#print(carbo_mamao)

calorias_mamao = (float(dict_usuario['06/04/15'][1][1]) * float(dict_alimentos['MAMAO PAPAYA'][1]))/100
#print(calorias_mamao)

gordura_mamao = (float(dict_usuario['06/04/15'][1][1]) * float(dict_alimentos['MAMAO PAPAYA'][4]))/100
#print(gordura_mamao)

'''INFORMACOES DO BISCOITO AMANTEIGADO'''

proteina_biscoito = (float(dict_usuario['06/04/15'][2][1]) * float(dict_alimentos['BISCOITO AMANTEIGADO'][2]))/100
#print(proteina_biscoito)

carbo_biscoito = (float(dict_usuario['06/04/15'][2][1]) * float(dict_alimentos['BISCOITO AMANTEIGADO'][3]))/100
#print(carbo_biscoito)

calorias_biscoito = (float(dict_usuario['06/04/15'][2][1]) * float(dict_alimentos['BISCOITO AMANTEIGADO'][1]))/100
#print(calorias_biscoito)

gordura_biscoito = (float(dict_usuario['06/04/15'][2][1]) * float(dict_alimentos['BISCOITO AMANTEIGADO'][4]))/100
#print(gordura_biscoito)


'''07/04/15'''
'''CREME DE AMENDOIM'''

proteina_creme = (float(dict_usuario['07/04/15'][1][1]) * float(dict_alimentos['CREME DE AMENDOIM'][2]))/100
#print(proteina_creme)

carbo_creme = (float(dict_usuario['07/04/15'][1][1]) * float(dict_alimentos['CREME DE AMENDOIM'][3]))/100
#print(carbo_creme)

calorias_creme = (float(dict_usuario['07/04/15'][1][1]) * float(dict_alimentos['CREME DE AMENDOIM'][1]))/100
#print(calorias_creme)

gordura_creme = (float(dict_usuario['07/04/15'][1][1]) * float(dict_alimentos['CREME DE AMENDOIM'][4]))/100
#print(gordura_creme)

'''MACARRAO AO ALHO E OLEO'''

proteina_macarrao = (float(dict_usuario['07/04/15'][0][1]) * float(dict_alimentos['MACARRAO AO ALHO E OLEO'][2]))/100
#print(proteina_macarrao)

carbo_macarrao = (float(dict_usuario['07/04/15'][0][1]) * float(dict_alimentos['MACARRAO AO ALHO E OLEO'][3]))/100
#print(carbo_macarrao)

calorias_macarrao = (float(dict_usuario['07/04/15'][0][1]) * float(dict_alimentos['MACARRAO AO ALHO E OLEO'][1]))/100
#print(calorias_macarrao)

gordura_macarrao = (float(dict_usuario['07/04/15'][0][1]) * float(dict_alimentos['MACARRAO AO ALHO E OLEO'][4]))/100
#print(gordura_macarrao)

'''NHOQUE'''

proteina_nhoque = (float(dict_usuario['07/04/15'][2][1]) * float(dict_alimentos['NHOQUE'][2]))/100
#print(proteina_nhoque)

carbo_nhoque = (float(dict_usuario['07/04/15'][2][1]) * float(dict_alimentos['NHOQUE'][3]))/100
#print(carbo_nhoque)

calorias_nhoque = (float(dict_usuario['07/04/15'][2][1]) * float(dict_alimentos['NHOQUE'][1]))/100
#print(calorias_nhoque)

gordura_nhoque = (float(dict_usuario['07/04/15'][2][1]) * float(dict_alimentos['NHOQUE'][4]))/100
#print(gordura_nhoque)

'''MILK-SHAKE DE CHOCOLATE'''

proteina_milk = (float(dict_usuario['07/04/15'][3][1]) * float(dict_alimentos['MILK-SHAKE DE CHOCOLATE'][2]))/100
#print(proteina_milk)

carbo_milk = (float(dict_usuario['07/04/15'][3][1]) * float(dict_alimentos['MILK-SHAKE DE CHOCOLATE'][3]))/100
#print(carbo_milk)

calorias_milk = (float(dict_usuario['07/04/15'][3][1]) * float(dict_alimentos['MILK-SHAKE DE CHOCOLATE'][1]))/100
#print(calorias_milk)

gordura_milk = (float(dict_usuario['07/04/15'][3][1]) * float(dict_alimentos['MILK-SHAKE DE CHOCOLATE'][4]))/100
#print(gordura_milk)

proteina_total6 = proteina_iogurte + proteina_suco + proteina_mamao + proteina_biscoito  #calcula o total de proteina ingerida no dia 6
#print(proteina_total6)

carbo_total6 = carbo_iogurte + carbo_suco + carbo_mamao + carbo_biscoito
#print(carbo_total6)

calorias_total6 = calorias_iogurte + calorias_suco + calorias_mamao + calorias_biscoito
print(calorias_total6)

gordura_total6 = gordura_iogurte + gordura_suco + gordura_mamao + gordura_biscoito
#print(gordura_total6)


