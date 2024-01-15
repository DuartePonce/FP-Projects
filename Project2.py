'''''
Projeto 2 de FP
Duarte Ponce ist1107489
data
ist1107489@gmail.com
'''''

'''''

TAD Gerador

'''''  


# Construtores

def cria_gerador(b, s):
    '''''
    cria o gerador 
    '''''
    if(
        type(b) != int or type(s) != int or b not in (32, 64) or s <= 0 or
        (b == 32 and s > 2**32-1) or (b == 64 and s > 2**64-1)
    ):
        raise ValueError('cria_gerador: argumentos invalidos')
    return [b, s]         

def cria_copia_gerador(g):
    '''''
    Faz uma copia do gerador
    '''''
    return g

# Seletores

def obtem_estado(g):
    '''''
    retorna o estado do gerador 
    '''''
    return g[1]

# Modificadores

def define_estado(g,s):
    '''''
    Define um novo estado para o gerador
    '''''
    g[1] = s
    return s

def atualiza_estado(g):
    '''''
    função que atualiza o estado do gerador com um seed nova
    '''''
    s = g[1]
    if g[0] == 32:
        s ^= (s << 13) & 0xFFFFFFFF
        s ^= (s >> 17) & 0xFFFFFFFF
        s ^= (s << 5) & 0xFFFFFFFF
    elif g[0] == 64:
        s ^= (s << 13) & 0xFFFFFFFFFFFFFFFF
        s ^= (s >> 7) & 0xFFFFFFFFFFFFFFFF
        s ^= (s << 17) & 0xFFFFFFFFFFFFFFFF
    g[1] = s
    return s

# Reconhecedor 

def eh_gerador(arg):
    '''''
    Identifica se é ou nao um gerador
    '''''
    if (
        type(arg) != list or len(arg) != 2 or type(arg[0]) != int or
        arg[0] not in (32, 64) or type(arg[1]) != int or 
        arg[1] <= 0 or (arg[0] == 32 and arg[1] > 2**32-1) or 
        (arg[0] == 64 and arg[1] > 2**64-1)
    ):
        return False
    return True

# Testes

def geradores_iguais(g1, g2):
    '''''
    Avalia se dois geradores sao iguais ou nao
    '''''
    if (eh_gerador(g1) and eh_gerador(g2)) == True and g1 == g2:
        return True
    return False

# Transformador

def gerador_para_str(g):
    '''''
    gera uma string com as informacoes sobre o gerador
    '''''
    return str(f'xorshift{g[0]}(s={g[1]})')

# Funcoes de alto nivel

def gera_numero_aleatorio(g, n):
    '''''
    gera um numero aleatorio ate n
    '''''
    s = atualiza_estado(g)
    return (1 + s % n)

def gera_carater_aleatorio(g, c):
    '''''
    ger um caracter aleatorio ate c
    '''''
    l = (ord(c) - ord('A') + 1) #O +1 aparece para tornar o intervalo fechado em 'A'
    s = atualiza_estado(g)
    return chr((s % l) + ord('A'))


'''''

TAD Coordenada

'''''


#construtor

def cria_coordenada(col, lin):
    '''''
    Cria uma coordenada (coluna, linha)
    '''''
    if ( 
        type(col) != str or type(lin) != int or
        len(col) != 1 or ord(col) < ord('A') or 
        ord(col) > ord('Z') or lin < 1 or lin > 99
    ):
        raise ValueError ('cria_coordenada: argumentos invalidos')
    return (col, lin)

#Seletores

def obtem_coluna(c):
    '''''
    Obtem a coluna da coordenada
    '''''
    return c[0]
def obtem_linha(c):
    '''''
    Obtem a linha da coordenada
    '''''
    return c[1]

#Reconhecedor

def eh_coordenada(arg):
    '''''
    verifica se o argumento é uma coordenada
    '''''
    if (
        type(arg) != tuple or len(arg) != 2 or
        len(arg[0]) != 1 or 
        type(arg[0]) != str or type(arg[1]) != int
        or ord('A') > ord(arg[0]) or ord('Z') < ord(arg[0])
        or 1 > arg[1] or 99 < arg[1]
    ):  
        return False
    return True


#Testes

def coordenadas_iguais(c1, c2):
    '''''
    Verifica se as coordenadas sao iguais
    '''''
    if c1[0] == c2[0] and c1[1] == c2[1]:
        return True
    return False

#Transformador

def coordenada_para_str(c):
    '''''
    transforma a coordenada numa string 
    '''''
    if c[1] < 10:
        return str(c[0]) + '0' + str(c[1])
    return str(c[0]) + str(c[1])

def str_para_coordenada(s):
    '''''
    transforma uma string numa coordenada
    '''''

    return (s[0], int(s[1:]))

#Funções de alto nivel


def obtem_coordenadas_vizinhas(c):
    '''''
    Obtem as coordenadas vizinhas a coordenada inserida
    '''''
    col = obtem_coluna(c)
    lin = obtem_linha(c)
    if col == 'A' and lin != 1:
        return [cria_coordenada(col, lin - 1), cria_coordenada(chr(ord(col) + 1), lin - 1),
        cria_coordenada(chr(ord(col) + 1), lin), cria_coordenada(chr(ord(col) + 1), lin + 1), 
        cria_coordenada(col, lin + 1)]

    elif lin == 1 and col != 'A':
        return [cria_coordenada(chr(ord(col) + 1), lin), cria_coordenada(chr(ord(col) + 1), lin + 1), 
        cria_coordenada(col, lin + 1), cria_coordenada(chr(ord(col) - 1), lin + 1), cria_coordenada(chr(ord(col) - 1), lin)]

    elif lin == 1 and col == 'A':
        return [cria_coordenada(chr(ord(col) + 1), lin), cria_coordenada(chr(ord(col) + 1), lin + 1), 
        cria_coordenada(col, lin + 1)]

    elif col == 'Z' and lin == 99 and lin != 1 and col != 'A':
        return [cria_coordenada(chr(ord(col) - 1), lin - 1), cria_coordenada(col, lin - 1), 
        cria_coordenada(chr(ord(col) - 1), lin)]

    elif lin != 99 and col != 'A' and col == 'Z' and lin != 1:
        return [cria_coordenada(chr(ord(col) - 1), lin - 1), cria_coordenada(col, lin - 1), 
        cria_coordenada(col, lin + 1), cria_coordenada(chr(ord(col) - 1), lin + 1), cria_coordenada(chr(ord(col) - 1), lin)]

    elif lin == 99 and col != 'A' and col != 'Z' and lin != 1:
        return [cria_coordenada(chr(ord(col) - 1), lin - 1), cria_coordenada(col, lin - 1), 
        cria_coordenada(chr(ord(col) + 1), lin - 1), cria_coordenada(chr(ord(col) + 1), lin), cria_coordenada(chr(ord(col) - 1), lin)]

    elif lin == 99 and col == 'A' and col != 'Z' and lin != 1:
        return [cria_coordenada(col, lin - 1), cria_coordenada(chr(ord(col) + 1), lin - 1), 
        cria_coordenada(chr(ord(col) + 1), lin)]
    
    elif col == 'Z' and lin == 1 and col != 'A' and lin != 99:
        return [(col, lin + 1), cria_coordenada(chr(ord(col) - 1), lin + 1), 
        cria_coordenada(chr(ord(col) - 1), lin)]

    else:
        return [cria_coordenada(chr(ord(col) - 1), lin - 1), cria_coordenada(col, lin - 1), cria_coordenada(chr(ord(col) + 1), lin - 1), 
        cria_coordenada(chr(ord(col) + 1), lin), cria_coordenada(chr(ord(col) + 1), lin + 1), cria_coordenada(col, lin + 1), 
        cria_coordenada(chr(ord(col) - 1), lin + 1), cria_coordenada(chr(ord(col) - 1), lin)]

    

def obtem_coordenada_aleatoria(c, g):
    '''''
    obtem uma coordenada aleatoria
    '''''
    maxcol = obtem_coluna(c)
    maxlin = obtem_linha(c)
    col = gera_carater_aleatorio(g, maxcol)
    lin = gera_numero_aleatorio(g, maxlin)
    return cria_coordenada(col, lin)

#Funcoes extras

def obtem_coordenadas_vizinhas_aux(c, m):
    '''''
    Obtem as coordenadas vizinhas a coordenada inserida
    '''''
    col = obtem_coluna(c)
    lin = obtem_linha(c)
    col_max = obtem_ultima_coluna(m)
    lin_max = obtem_ultima_linha(m)

    if lin != 1 and col == 'A' and col != col_max and lin != lin_max:
        return [(col, lin - 1), (chr(ord(col) + 1), lin - 1), (chr(ord(col) + 1), lin), (chr(ord(col) + 1), lin + 1), (chr(ord(col)), lin + 1)]

    elif lin == 1 and col != 'A' and col != col_max and lin != lin_max:
        return [(chr(ord(col) + 1), lin), (chr(ord(col) + 1), lin + 1), (col, lin + 1), (chr(ord(col) - 1), lin + 1), (chr(ord(col) - 1), lin)]

    elif lin == 1 and col == 'A' and col != col_max and lin != lin_max:
        return [(chr(ord(col) + 1), lin), (chr(ord(col) + 1), lin + 1), (col, lin + 1,)]
    
    elif col == col_max and lin == lin_max and lin != 1 and col != 'A':
        return [(chr(ord(col) - 1), lin - 1), (col, lin - 1), (chr(ord(col) - 1), lin)]

    elif lin != lin_max and col != 'A' and col == col_max and lin != 1:
        return [(chr(ord(col) - 1), lin - 1), (col, lin - 1), (col, lin + 1), (chr(ord(col) - 1), lin + 1), (chr(ord(col) - 1), lin)]

    elif lin == lin_max and col != 'A' and col != col_max and lin != 1:
        return [(chr(ord(col) - 1), lin - 1), (col, lin - 1), (chr(ord(col) + 1), lin - 1), (chr(ord(col) + 1), lin), (chr(ord(col) - 1), lin)]

    elif lin == lin_max and col == 'A' and col != col_max and lin != 1:
        return [(col, lin - 1), (chr(ord(col) + 1), lin - 1), (chr(ord(col) + 1), lin)]
    
    elif col == col_max and lin == 1 and col != 'A' and lin != lin_max:
        return [(col, lin + 1), (chr(ord(col) - 1), lin + 1), (chr(ord(col) - 1), lin)]

    else:
        return [(chr(ord(col) - 1), lin - 1), (col, lin - 1), (chr(ord(col) + 1), lin - 1), 
        (chr(ord(col) + 1), lin), (chr(ord(col) + 1),  lin + 1), (col, lin + 1), 
        (chr(ord(col) - 1), lin + 1), (chr(ord(col) - 1), lin)]

'''''
TAD Parcela
'''''

#Construtores
'''''
Funções construtoras da parcela 

'''''
def cria_parcela():
    return ['tapada', 0]

def cria_copia_parcela(p):
    return [p[0], p[1]]

#Modificadores
'''''
Funçoes que recebem uma parcela e a modificao destrutivamente
'''''
def limpa_parcela(p):
    p[0] = 'limpa'
    return p

def marca_parcela(p):
    p[0] = 'marcada'
    return p

def desmarca_parcela(p):
    p[0] = 'tapada'
    return p

def esconde_mina(p):
    p[1] = 1
    return p

#Reconhecedor
'''''
funcoes que ao receberem uma parcela verificao se é uma parcela, o seu estado e a exitencia de mina
'''''
def eh_parcela(arg):
    if type(arg) != list or len(arg) != 2 or arg[0] not in ('limpa', 'marcada', 'tapada') or arg[1] not in (0, 1):
        return False
    return True

def eh_parcela_tapada(p):
    if p[0] == 'tapada':
        return True
    return False

def eh_parcela_marcada(p):
    if p[0] == 'marcada':
        return True
    return False

def eh_parcela_limpa(p):
    if p[0] == 'limpa':
        return True
    return False

def eh_parcela_minada(p):
    if p[1] == 1:
        return True
    return False

#Testes
'''''
Funçao que testa se duas parcelas sao iguais
'''''
def parcelas_iguais(p1, p2):
    if eh_parcela(p1) != True or eh_parcela(p2) != True or p1[0] != p2[0] or p1[1] != p2[1]:
        return False
    return True

#Transformadores
'''''
Funcao que transforma a parcela que recebe numa string do seu tipo
'''''
def parcela_para_str(p):
    if p[0] == 'limpa' and p[1] == 1:
        return  'X'
    elif p[0] == 'limpa':
        return '?'
    elif p[0] == 'marcada':
        return  '@'
    elif p[0] == 'tapada':
        return '#'


#Funcoes de alto nivel
'''''
Funcao que recebe uma parcela e marca-a caso esteja desmarcada e desmarca caso esteja marcada
'''''
def alterna_bandeira(p):
    if eh_parcela_marcada(p):
        desmarca_parcela(p)
        return True
    elif eh_parcela_tapada(p):
        marca_parcela(p)
        return True
    return False



'''''
TAD Campo
'''''

#Construtores
'''''
Funcao que recebe um caracter e um inteiro e cria um campo com limite na coordenada criada por esse caracter e inteiro
'''''

def cria_campo(c, l):
    if (
        type(c) != str or len(tuple(c)) != 1 or ord(c) < ord('A') or ord(c) > ord('Z') or
        type(l) != int or l < 1 or l > 99
    ):
        raise ValueError ('cria_campo: argumentos invalidos')
    campo = {}
    for i in range(ord(c) - ord('A') + 1):
        for j in range(1,l + 1):
            campo[(chr(i + ord('A')), j)] = ['tapada', 0]
    return campo

def cria_copia_campo(m):
    '''''
    funcao que cria uma copia de um campo
    '''''
    c = obtem_ultima_coluna(m)
    l = obtem_ultima_linha(m)
    m2 = cria_campo(c, l)
    return m2

#Seletores
'''''
Funcoes que recebem um campo  e identificam a sua ultima linha e ultima coluna
'''''
def obtem_ultima_coluna(m):
    # key = list(m.keys())
    key = []
    for x in m.keys():
        key.append(x)
    return key[-1][0]

def obtem_ultima_linha(m):
    key = list(m.keys())
    return key[-1][1]

'''''
funcao que identifica dentro de um campo a parcela respetiva a coordenada de entrada
'''''
def obtem_parcela(m, c):
    return m[c]

'''''
Funcao que recebe um campo e um estado e retorna todas as coordenadas cujas parcelas
tem esse estado
'''''
def obtem_coordenadas(m, s):
    c = obtem_ultima_coluna(m)
    l = obtem_ultima_linha(m)
    tuplo = ()
    for j in range(1,l + 1):
        for i in range(1,(ord(c) - ord('A') + 2)):
            col, lin = chr(64 + i), j
            if s == 'limpas':
                if m[(col, lin)] == ['limpa', 0]:
                    tuplo += ((col, lin),)
            if s == 'tapadas':
                if m[(col, lin)] == ['tapada', 0]:
                    tuplo += ((col, lin),)
            if s == 'marcadas':
                if m[(col, lin)] == ['marcada', 0]:
                    tuplo += ((col, lin),)
            if s == 'minadas':
                if  m[(col, lin)] == ['marcada', 1] or m[(col, lin)] == ['tapada', 1] or m[(col, lin)] == ['limpa', 1]:
                    tuplo += ((col, lin),)

    return tuplo

'''''
Funcao que recebe um campo e coordenada e retorna o numero de minas vizinhas a essa coordenada
'''''
def obtem_numero_minas_vizinhas(m, c):
    viz = 0
    coor_m = obtem_coordenadas_vizinhas_aux(c, m)
    for i in coor_m:
            if eh_parcela_minada(obtem_parcela(m, i)) == True:
                viz += 1
    return viz

#Reconhecedores
'''''
Funcao que verifica se o argumento e umk campo
'''''
def eh_campo(arg):
    if type(arg) != dict or arg == {}:
        return False
    for i in arg:
        if (
            eh_coordenada(i) == False
            or eh_parcela(arg[i]) == False
        ):
            return False
    return True
'''''
Funcao que veerifica se uma coordenada faz parte do campo que recebe
'''''
def eh_coordenada_do_campo(m, c):
    k = list(m.keys())
    if c not in k:
        return False
    else:
        return True

#Testes
'''''
funcao que avalia se dois campos sao iguais
'''''
def campos_iguais(m1, m2):
    if m1 == m2:
        return True
    return False

#Transformadores
'''''
funcao que transforma um campo(dicionario) numa string com a sua representacao interna
'''''
def campo_para_str(m):
    col_campo = obtem_ultima_coluna(m)
    campo, coor = '', list(sorted(m.items(), key = lambda item : item[0][1]))
    col, bar, par, linhas, n, l = '   ', '\n  +', '', '', 0, 1


    for i in range(len(coor)):
        if coor[i][1][0] != 'limpa' or (coor[i][1][0] == 'limpa' and coor[i][1][1] == 1):
            par += f'{parcela_para_str(coor[i][1])}'
        else:
            minas = obtem_numero_minas_vizinhas(m, coor[i][0])
            if minas == 0:
                par += ' '
            else:
                par += str(minas)

        n += 1

        if n == (ord(col_campo) - ord('A') + 1):
            if l < 10:
                linhas += ('\n0' + str(l) + '|' + par + '|')
            else:
                linhas += ('\n' + str(l) + '|' + par + '|')
            n = 0
            l += 1
            par = ''


    for j in range(ord(col_campo) - ord('A') + 1):
        col += chr(j+ ord('A'))
        bar += '-'
    bar += '+'
    campo += col + bar + linhas + bar


    return campo

#Funcoes de alto nivel
'''''
Funcao que coloca as minas aleatoriamente no campo
'''''
def coloca_minas(m, c, g, n):
    col_campo, lin_campo = obtem_ultima_coluna(m), obtem_ultima_linha(m)
    lista = []
    coor = cria_coordenada(col_campo, lin_campo)
    coor_viz = obtem_coordenadas_vizinhas(c)
    coor_viz += (c,)
    while len(lista) < n:
        coor_random = obtem_coordenada_aleatoria(coor, g)
        if coor_random not in coor_viz and coor_random not in lista and eh_parcela_minada(obtem_parcela(m, coor_random)) == False:
            lista += [coor_random]

    for i in lista:
        esconde_mina(obtem_parcela(m, i))

    return m

'''''
funcao que dada uma coordenada limpa-a e a todas a sua volta
'''''
def limpa_campo(m, c):
    if eh_parcela_limpa(obtem_parcela(m, c)):
        return m 
    limpa_parcela(obtem_parcela(m, c))
    if obtem_numero_minas_vizinhas(m, c) == 0:
        for i in obtem_coordenadas_vizinhas_aux(c, m):
            if eh_parcela_tapada(obtem_parcela(m, i)):
                limpa_campo(m, i)
    return m


#Funcoes adicionais
'''''
funcao que avalia se o jogo foi ou nao perdido returnando false se perdido e True se ganho

'''''
def jogo_ganho(m):
    for i in m:
        if not eh_parcela_limpa(obtem_parcela(m, i)) and not eh_parcela_minada(obtem_parcela(m, i)):
            return False
    return True

#Funcao turno jogador

'''''
Funcao que efetua as interacoes necessarias para efetuar um turno do jogo das minas
'''''
def turno_jogador(m):
    lista = []
    for i in m:
        lista += [i]

    acao = str(input('Escolha uma ação, [L]impar ou [M]arcar:'))

    while acao not in  ('L','M'):
        acao = str(input('Escolha uma ação, [L]impar ou [M]arcar:'))
    coor = str(input('Escolha uma coordenada:'))
    coor = str_para_coordenada(coor)

    while coor not in lista:
        coor = str_para_coordenada(str(input('Escolha uma coordenada:')))

    if acao == 'L' and eh_parcela_minada(obtem_parcela(m,coor)) == True:
        limpa_parcela(obtem_parcela(m, coor))
        return False
    elif acao == 'L' and eh_parcela_minada(obtem_parcela(m,coor)) == False:
        limpa_campo(m, coor)
        return True 
    elif acao == 'M':
        alterna_bandeira(obtem_parcela(m, coor))
        return True


#Função auxiliar
'''''
Funcao semelhante ao turno_jogador contudo somente efetua o primeiro turno 
dado que esse é ligeiramente diferente
'''''
def primeiro_turno_jogador(m, g, n):
    lista = []
    for i in m:
        lista += [i]

    coor = str(input('Escolha uma coordenada:'))
    coor = str_para_coordenada(coor)

    m = coloca_minas(m, coor, g, n)

    while coor not in lista:
        coor = str_para_coordenada(str(input('Escolha uma coordenada:')))

    if eh_parcela_minada(obtem_parcela(m,coor)) == True:
        return False
    elif eh_parcela_minada(obtem_parcela(m,coor)) == False:
        limpa_campo(m, coor)
        return True 

'''''
pequena funcao auxiliar que avalia o tamanho do campo para
um verificacao na funcao mais a frente
'''''
def tamanho_campo(c, l):
    m = cria_campo(c, l)
    n = len(obtem_coordenadas(m, 'tapadas'))
    return n

'''''
Funcao que combina todos os tads e suas funcoes de alto nivel 
e permite jogar o jogo 
'''''
def minas(c, l, n, d, s):
    if(
        type(c) != str or len(tuple(c)) != 1 or ord(c) < ord('A') or ord(c) > ord('Z') or
        type(l) != int or l < 1 or l > 99 or
        type(d) != int or type(s) != int or d not in (32, 64) or s <= 0 or
        (d == 32 and s > 2**32-1) or (d == 64 and s > 2**64-1) or   
        type(n) != int  or n <= 0 or n > tamanho_campo(c, l)-9     
    ): 
        raise ValueError('minas: argumentos invalidos')

    g = cria_gerador(d, s)
    m = cria_campo(c,l)
    print('   ', f'[Bandeiras {numero_bandeiras(m)}/{n}]')
    print(campo_para_str(m))
    primeiro_turno_jogador(m,g ,n)
    jogo_ganho(m)

    while jogo_ganho(m) == False:
        print('   ', f'[Bandeiras {numero_bandeiras(m)}/{n}]')
        print(campo_para_str(m))
        d = turno_jogador(m)
    
        
        if d == False:
            print(campo_para_str(m))
            print('BOOOOOOOM!!!')
            return False

    print('VITORIA!!!')       
    return True

'''''
pequena funcao auxiliar que conta o numero de parcelas 
marcadas no campo
'''''
def numero_bandeiras(m):
    n = 0
    for i in m:
        if eh_parcela_marcada(obtem_parcela(m, i)) == True:
            n += 1
    return n
