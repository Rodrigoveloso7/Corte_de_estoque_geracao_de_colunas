from pyomo.environ import *
import numpy as np

comp_itens = [200,400,600,800,100]
demanda = [30,60,45,30,15]
capacidade = 1200
max_iter = 1000
# padroes = [[3,0,0],
# [2,1,0],
# [1,2,0],
# [2,0,1],
# [0,1,1],
# [0,0,2]]
# demanda = [32,17,21]
# padroes = [[1,0,0,3,1],
#            [1,0,2,1,0],
#            [1,1,0,0,0],
#            [0,2,0,1,2],
#            [0,0,1,0,1],]
# demanda = [10,12,15,31,17]

def problema_principal(padroes,demanda):
    #Declaração do modelo
    modelo_principal = ConcreteModel()
    #Definição de variáveis de interesse
    modelo_principal.indices = range(len(padroes))
    modelo_principal.indices_demanda = range(len(demanda))
    modelo_principal.x = Var(modelo_principal.indices,domain=NonNegativeReals)
    # print("Variáveis criadas:", list(modelo_principal.x.keys()))
    # print("modelo principal indices", modelo_principal.indices)

    #Definição da função objetivo
    modelo_principal.f_objetivo = Objective(expr=sum(modelo_principal.x[i] for i in modelo_principal.indices), sense=minimize)
    print(modelo_principal.f_objetivo.expr)

    #Restrições
    modelo_principal.restr = ConstraintList()
    for j in modelo_principal.indices_demanda:
        expr = sum(modelo_principal.x[i]*padroes[j][i] for i in modelo_principal.indices)
        modelo_principal.restr.add(expr >= demanda[j])
        print(f"Restrição {j}: {expr} >= {demanda[j]}")
    modelo_principal.dual = Suffix(direction=Suffix.IMPORT)
    resultado_principal = SolverFactory('cbc', executable='C:\\Cbc-refactor-x86_64-w64-mingw32\\bin\\cbc.exe').solve(modelo_principal,tee=True)
    #
    # print('f_objetivo:',value(modelo_principal.f_objetivo))
    # print(modelo_principal.dual[modelo_principal.restr[1]])
    variaveis_duais = []
    for i in range(1,len(demanda)+1):
        variaveis_duais.append(modelo_principal.dual[modelo_principal.restr[i]])
    # variaveis_de_interesse_principal = []
    # for i in modelo_principal.indices:
    #     print(value(modelo_principal.x[i]))
    #     variaveis_de_interesse_principal.append(value(modelo_principal.x[i]))
    # return variaveis_de_interesse_principal,variaveis_duais

def problema_mochila(padroes,capacidade,variaveis_duais):
    # Declaração do modelo
    modelo_mochila = ConcreteModel()
    # Definição de variáveis de interesse
    modelo_mochila.indices = range(len(padroes))
    modelo_mochila.x = Var(modelo_mochila.indices, within=NonNegativeIntegers)
    # Definição da função objetivo
    modelo_mochila.f_objetivo = Objective(expr=sum(modelo_mochila.x[i]*variaveis_duais[i] for i in modelo_mochila.indices),
                                            sense=maximize)
    modelo_mochila.rest = Constraint(expr=sum(modelo_mochila.x[i]*comp_itens[i] for i in modelo_mochila.indices )<= capacidade)
    resultado_mochila = SolverFactory('cbc', executable='C:\\Cbc-refactor-x86_64-w64-mingw32\\bin\\cbc.exe').solve(
        modelo_mochila)
    novo_padrao = []
    for i in modelo_mochila.indices:
        novo_padrao.append(value(modelo_mochila.x[i]))
    return novo_padrao,variaveis_duais,modelo_mochila.indices




def solucionador(comp_itens,demanda,capacidade,max_iter):
    padroes = np.eye(len(comp_itens)).tolist()  # verificar depois se inicializar
    # com matrizes menor é melhor
    print(padroes)
    for z in range(max_iter):
        solucao_principal = problema_principal(padroes,demanda)
        solucao_mochila = problema_mochila(padroes,capacidade,solucao_principal[1])
        if sum(solucao_mochila[1][i] * solucao_mochila[0][i] for i in solucao_mochila[2]) > 1:
            print(solucao_mochila[0])
            padroes.append(solucao_mochila[0])
        else:
            print('Solução ótima atingida')
            return padroes, solucao_principal[0]

padroes,variaveis_de_interesse = solucionador(comp_itens, demanda, capacidade, max_iter)
print(padroes)
# pp = problema_principal(padroes,demanda)
# print(pp[0])