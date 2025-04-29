# -*- coding: utf-8 -*-

def soma(a,b,c):
    s = a + b + c
    return s

def SOMA(a,b,c):
    s = a + b + c
    return s

y1 = soma(10,20,30)
print(y1)

y2 = soma(30,10,20)
print(y2)

#%% Argumentos com palavras-chave (keywords kw)

def p(a, b, c):
    '''retorna a + b**2 + c**3'''
    return a + b**2 + c**3

print()
y1 = p(10,20,30)
print(y1)

y2 = p(30,10,20)
print(y2)

y3 = p(c=30, a=10, b=20) # mais util para funçoes com muitos parametros
print(y3)

#%% Argumentos posicionais + argumentos com palavras-chaves 

print()
print(p(30,10,c=20)) # argumentos posicionais devem vir antes das palavras chave
#print(p(b=30,a=10,20)) erro

#%% Parametros com valores padroes (default)

def potencia(x, n=2):
    '''retorna x**n'''
    return x**n

print()
print(potencia(2,3))
print(potencia(2))

#%% Forçando o uso de palavras-chave. A partir do (*) temos necessidade de kw

def q(a, *, b=0, c=0):
    '''retorna a + b**2 + c**3'''
    return a + b**2 + c**3

print()
#print(q(10,20,30)) erro
print(q(10,b=20,c=30))
print(q(10,c=30,b=20))
print(q(a=10,b=20,c=30))
print(q(10))

#%% Passando uma lista como argumento

# Exemplo 1:
def listar_elementos(lista):
    '''lista os elementos da lista "list"'''
    for elemento in lista:
        print(elemento)
    
lista1 = ['alpha', 'beta', 'gamma', 'delta']

print()
listar_elementos(lista1)

#%% Exemplo 2:
    
def p(a, b, c):
    '''retorna a + b**2 + c**3'''
    return a + b**2 + c**3


lista = [10,20,30]

print()
print(lista)
print(*lista)

print(p(*lista)) # *lista: operador de desempacotamento

#%% Passando um dicionario como argumento de uma funçao

def p(a, b, c):
    '''retorna a + b**2 + c**3'''
    return a + b**2 + c**3

args = dict(c=30, a=10, b=20)
#args2 = {'a':10, 'b':20, 'c':30} outra forma

print()
print(args)
print(*args)
print(p(**args)) # util para dicionarios

#%% Passando um numero arbitrario de argumentos para uma funcao
# *valores: empacotamento

def media3(a, b, c):
    '''retorna a media de a,b,c'''
    return (a + b + c)/3
    
def media(*valores):
    '''retorna a media de n valores'''
    soma = sum(valores)
    n = len(valores)
    med = soma / n
    return med

print()
print(media3(10,22,25))

print()
print(media(10,20,30,40))

#%% Variaveis locais e globais

v = 123
G = 777
T = 222

def foo():
    global G
    v = 500
    G = 111
    print(f"foo(): {v} e {G} e {T}")

print()
print(f"valor de v, G Antes: {v} e {G}")
foo()
print(f"valor de v, G Depois: {v} e {G}")