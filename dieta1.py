def TMB():
    peso=70
    altura=164
    idade=30    
    return 88.36+(13.4*peso)+(4.8*altura)-(5.7*idade)
print(TMB())

def qtdecalorica():  #quantidade energetica em kcal necessitada 
    return TMB()*1.725 #o numero 1.725 é porque o nivel de atividade do usuario é alto
print(qtdecalorica())