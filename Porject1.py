'''''
Primeiro Projeto de FP
Duarte Ponce 
ist1107489@tecnico.ulisboa.pt
ist1107489
27/10/2022

'''''


#1

def limpa_texto (texto):

    '''''
    Funcao que recebe uma cadeia de caracteres 
    e devolve essa mesma cadeia sem os caracteres 
    brancos de ASCII

    '''''

    texto = str(texto.strip())
    if '/n' in texto:
        texto = texto.split('/n')
        texto = ' '.join(texto)
    if '/f' in texto:
        texto = texto.split('/f')   
        texto = ' '.join(texto)
    if '/r' in texto:
        texto = texto.split('/r')
        texto = ' '.join(texto)  
    if '/v' in texto:
        texto = texto.split('/v')
        texto = ' '.join(texto)  
    if '/t' in texto:
        texto = texto.split('/t')
        texto = ' '.join(texto) 
    texto = texto.split()
    texto = ' '.join(texto)
    return texto

def corta_texto (t,num):

    '''''
    Funcao que recebe um texto e uma largura de colunas e 
    devolve um tuplo formado por duas cadeias a primeira
    tendo no maximo largura igual a largura de coluna dada

    '''''
    
    t2 = ()
    if len(t) <= num:
        t2 = (t[:len(t)],) + ('',)
    else:
        while t[num] != ' ':
            num = num - 1
        t2 = (t[:num],) + (t[num + 1:],)
    return t2

def insere_espacos(t,num):

    '''''
    Funcao que recebe uma cadeia de caracteres e uma largura de coluna
    e retorna e retorna essa mesma cadeia caso tenho tamanho inferior a num
    com espaços entre as palavras ate ter largura igual a num

    '''''

    t3, ii, i = str(t), 0, 0
    num = num - len(t3)
    t3 = t3.split() 
    if len(t3) >= 2:
        while ii < num:
            for i in range(0,len(t3)-1):
                t3[i] = t3[i] + ' '
                ii += 1
                if ii == num:
                    break
        t = ' '.join(t3)
    else:
        while ii != num:
            t = t + ' '
            ii += 1
    return t

def verificacao(t,num):

    '''''
    funcao de auxilio de verificacoes da funcao justifica_texto

    '''''
    t = t.split()
    for i in range(len(t)):
        if len(t[i]) > num:
            return False
    return True

def justifica_texto(t,num):
    '''''
    Funcao que recebe um texto e uma largura de coluna
    e devolve esse mesmo texto justificado

    '''''
    if type(t) != str or type(num) != int:
        raise ValueError('justifica_texto: argumentos invalidos')
    t = limpa_texto(t) 
    if t == '' or num <= 0 or verificacao(t,num) == False: 
        raise ValueError('justifica_texto: argumentos invalidos')
    t2 = ()
    while len(t) >= num:
        t = corta_texto(t,num)
        ti = insere_espacos(t[0],num)
        t2 = t2 + (ti,)
        t = t[1]
    if len(t) != 0:
        ti = t
        while len(ti) < num:
            ti = ti + ' '
        t2 = t2 + (ti,)       
    return t2


#2


def calcula_quocientes(dic,n):

    '''''
    Funcao que recebe um dicionario constituido pelos partidos e seus votos
    e um numero inteiro que e o numero de deputados a eleger
    e retorna os quocientes pelo metodo de hondt 

    '''''
    r, lst = 1, []
    dic2 = dic.copy()
    for x in dic:
        while r <= n:
            lst = lst + [dic2[x] / r]
            r += 1
        dic2[x] = lst
        lst = []
        r = 1
    return dic2


def atribui_mandatos(dic,n):

    '''''
    Funcao que recebe um dicionario constituido pelos partidos e seus votos
    e um numero inteiro que e o numero de deputados a eleger
    retornando uma lista com a ordem pela qual os partidos 
    elegem deputados

    '''''
    dic2 = dic.copy()
    dic2 = dict(sorted(dic2.items(), key = lambda item : item[1]))
    r, lista = 1, []
    while r <= n:
        k, numl = 0, 1
        testlistkeys = dic2.keys()
        ele = max(dic2.values())
        for i in testlistkeys:
            if dic2[i] == ele:
                k = i
                break
        lista = lista + [k]
        r += 1       
        for i in lista:
            if k == i:
                numl += 1
        dic2[k] = dic[k] / numl
    return lista


def obtem_partidos(dic):

    '''''
    Funcao que recebe um dicionario com os partidos de diferentes regioes
    e retorna uma lista com todos os partidos que estao representados no dicionário

    '''''
    lista, n = [], 0
    for i in dic:
        keys = list(dic[i]['votos'])
        keys.sort()
        lista = lista + keys
    lista.sort()
    while n < len(lista):
        if lista[n] == lista[n-1]:
            lista.remove(lista[n])
        else:
            n += 1
    return lista

def obtem_resultado_eleicoes(dic):

    '''''
    Funcao que recebe um dicionario que contem os dados de eleicoes 
    de regioes diferentes e retorna uma lista constituida por triplos
    com o partido numero de deputados eleitos e numero de votos totais

    '''''
    if type(dic) != dict or dic == {}:
        raise ValueError ('obtem_resultado_eleicoes: argumento invalido')
    for i in dic:
        if (
            'deputados' not in dic[i] or 'votos' not in dic[i] or 
            type(i) != str or type(dic[i]['votos']) != dict or
            dic[i]['votos'] == {}  or len(dic[i]) != 2
        ):
            raise ValueError ('obtem_resultado_eleicoes: argumento invalido')
        for j in dic[i]['votos']:
            if (
                type(dic) != dict or type(dic[i]) != dict or 
                type(dic[i]['deputados']) != int or
                dic[i]['deputados'] == 0 or dic[i].keys() == [] or 
                type(dic[i]['votos']) != dict or dic.keys() == [] or 
                type(j) != str or type(dic[i]['votos'][j]) != int or 
                dic[i]['votos'][j] == 0
            ):       
                raise ValueError ('obtem_resultado_eleicoes: argumento invalido')
            elif dic[i]['votos'][j] < 0  or dic[i]['deputados'] < 0:
                raise ValueError ('obtem_resultado_eleicoes: argumento invalido')
        
    t, dic3, nmtotal = [] , {} , []
    lista = obtem_partidos(dic)
    for i in lista:
        t = t + [(i,)]
    for i in dic:
        nm = atribui_mandatos(dic[i]['votos'],dic[i]['deputados'])
        nmtotal = nmtotal + nm
        nmtotal.sort()
        for j in dic[i]['votos']:
            if j in dic3:
                dic3[j] += dic[i]['votos'][j]
            else:
                dic3[j] = dic[i]['votos'][j]
    dic2 = {}
    for ele in nmtotal:
        if ele in dic2:
            dic2[ele] += 1
        else:
            dic2[ele] = 1
    dic3 = dict(sorted(dic3.items(), key = lambda item : item[1], reverse = True))
    for i in range(len(t)):
        for ii in t[i]:
            if ii in dic2 and ii in dic3:
                t[i] =  (ii , dic2[ii] , dic3[ii])
            else:
                t[i] =  (ii , 0 , dic3[ii])
    for i in range(len(t)):
        for j in range(len(t) - i - 1):
            if t[j][1] < t[j+1][1]:
                t[j],t[j+1] = t[j+1],t[j]
            elif t[j][1] == t[j+1][1]:
                if t[j][2] < t[j+1][2]:
                    t[j],t[j+1] = t[j+1],t[j]
    return t


#3


def produto_interno(u,u1):

    '''''
    Funcao que faz o produto interno 
    entre dois tuplos de igual dimensao

    '''''
    i, pr = 0, 0
    while i != len(u): 
        pr = pr + (u[i] * u1[i])   
        i += 1
    return float(pr)

def verifica_convergencia(u,c,x,e):

    '''''
    Funcao que verifica a convergencia 
    a partir de uma matriz u, vetor solucao e vetor constantes
    e compara com uma precisao retornando ou true ou False

    '''''
    fx, counter, j, i = (), 0, 0, 0
    for i in range(len(u)):
        fx = fx + (produto_interno(u[i],x),)
    for j in range(len(fx)):
        if (fx[j] - c[j]) > 0: 
            if (fx[j] - c[j]) < e:
                counter += 1
        else:
            if -(fx[j] - c[j]) < e:
                counter += 1            
    if counter == len(fx):
        return True
    else: 
        return False

def retira_zeros_diagonal(u,c):

    '''''
    Funcao que a partir de trocas de linhas de 
    ambos os inputs retira os zeros presentes 
    na diagonal

    '''''
    u = list(u)
    c = list(c)
    for i in range(len(u)):
        u[i] = list(u[i])
        if u[i][i] == 0:
            j = 0
            while u[j][i] == 0:
                j += 1
            trocado = u[i]
            u[i] = u[j]
            u[j] = trocado
            trocado = c[i]
            c[i] = c[j]
            c[j] = trocado 
    for i in range(len(u)):
        u[i] = tuple(u[i])
    u = tuple(u)
    c = tuple(c)                  
    return u, c

def eh_diagonal_dominante(u):

    '''''
    Funcao que verifica se a diagonal de uma matriz
    e ou nao diagonalmente dominante

    '''''
    soma = 0
    for i in range(len(u)):
        for j in range(len(u[i])):
            if j != i:
                soma = soma + abs(u[i][j])
        if soma > abs(u[i][i]):
            return False
        soma = 0
    return True

def verifica(u,c):

    '''''
    Funcao auxiliar de verificacoes

    '''''
    for i in range(len(u)):
        for j in range(len(u)):
            if type(u[i]) != tuple or len(c) != len(u[i]) or len(u[i]) < len(u) or type(u[i][j]) != (int or float) or type(c[i]) != (int or int) or u == () or c == () or u[i] == () or len(u[i]) != len(u) :
                return False
    return True

def resolve_sistema(u, c, e):

    '''''
    funcao que aplica o metodo 
    de jacobi e resolve um sistema de equacoes 
    de qualquer tamanho tendo a matriz de ser quadrada

    '''''
    if type(u) != tuple or type(c) != tuple or e < 0 or type(e) != float or verifica(u,c) == False:
        raise ValueError ('resolve_sistema: argumentos invalidos')
    u,c = list(retira_zeros_diagonal(u,c))
    if eh_diagonal_dominante(u) != True:
        raise ValueError ('resolve_sistema: matriz nao diagonal dominante')
    fx, x = () , []
    for i in range(len(u)):
        x = x + [0,]
    while verifica_convergencia(u,c,x,e) == False:
        for j in range(len(u)):
            fx = fx + (produto_interno(u[j],x),)
        for i in range(len(u)):
            t = (c[i] - fx[i])
            x[i] = x[i] + t / u[i][i]
        fx = ()
    return tuple(x)