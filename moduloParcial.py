import numpy as np
import sys

# Funcion que retorna una lista de los numeros positivos en una matriz de 2 dimensiones
def positivos(a):
    res=[]
    if len(a.shape)==2:
        for i in range(a.shape[0]):
            for j in range(a.shape[0]):
                if a[i][j]>=0:
                    res.append(a[i][j])
    return res

# Funcion que retorna una lista de los numeros negativos en una matriz de 2 dimensiones
def negativos(a):
    res=[]
    if len(a.shape)==2:
        for i in range(a.shape[0]):
            for j in range(a.shape[0]):
                if a[i][j]<0:
                    res.append(a[i][j])
    return res
    
# Funcion que retorna una lista de los numeros pares en una matriz de 2 dimensiones 
def pares(a):
    res=[]
    if len(a.shape)==2:
        for i in range(a.shape[0]):
            for j in range(a.shape[0]):
                if a[i][j]%2==0:
                    res.append(a[i][j])
    return res

# Funcion que retorna una lista de los numeros impares en una matriz de 2 dimensiones  
def impares(a):
    res=[]
    if len(a.shape)==2:
        for i in range(a.shape[0]):
            for j in range(a.shape[0]):
                if a[i][j]%2!=0:
                    res.append(a[i][j])
    return res
    
# Funcion que retorna True si en numero ingresado es primo y False si no
def primo(a):
    i=a
    cont=0
    while i>0:
        if a%i==0:
            cont+=1
        i-=1
    if cont==2:
        return True
    else:
        return False

# Funcion que retorna una lista de los numeros primos en una matriz de 2 dimensiones
def primos(a):
    res=[]
    if len(a.shape)==2:
        for i in range(a.shape[0]):
            for j in range(a.shape[0]):
                if primo(a[i][j]):
                    res.append(a[i][j])
    return res