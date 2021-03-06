import numpy as np

# Funcion que retorna una lista de los numeros positivos en una matriz de 2 dimensiones, el resto de posiciones se hace 0
def positivos(a):
    #Crea una lista vacia para almacenar los resultados
    res=np.zeros(a.shape)
    #Verifica que el tamaño de la matriz si sea 2 dimensiones
    if len(a.shape)==2:
        #Toma el tamaño de la matriz en las filas ya que a.shape regresa una tupla de dos posiciones, se toma la primera que corresponde a las filas
        for i in range(a.shape[0]):
            #Toma el tamaño de la matriz en las columnas
            for j in range(a.shape[1]):
                #Se verifica si el elemento en cada posición es positivo
                if a[i][j]>=0:
                    res[i][j]=a[i][j]
    return res

# Funcion que retorna una matriz de los numeros impares en una de 2 dimensiones, el resto de posiciones se hace 0
def impares(a):
    #Crea una lista vacia para almacenar los resultados
    res=np.zeros(a.shape)
    #Verifica que el tamaño de la matriz si sea 2 dimensiones 
    if len(a.shape)==2:
        #Toma el tamaño de la matriz en las filas ya que a.shape regresa una tupla de dos posiciones, se toma la primera que corresponde a las filas
        for i in range(a.shape[0]):
            #Toma el tamaño de la matriz en las columnas
            for j in range(a.shape[1]):
                #Se verifica si el elemento en cada posición es par mirando si el residuo de la division entre 2 es diferente de 0
                if a[i][j]%2!=0:
                    res[i][j]=a[i][j]
    return res
    
# Funcion que retorna True si en numero ingresado es primo y False si no
def primo(a):
    #Se inicia el iterador en a para descender desde a hasta 0
    i=a
    #Cont representa la cantidad de numeros por los que es divisible a
    cont=0
    while i>0:
        #Si el residuo de la división entre 'a' e 'i' es 0, significa que es divisible y se incrementa cont
        if a%i==0:
            cont+=1
        i-=1
    #Si cont es 2, significa que solo es divisible por 1 y por si mismo, retorna True
    if cont==2:
        return True
    #En caso contrario retorna False
    else:
        return False

# Funcion que retorna una lista de los numeros primos en una matriz de 2 dimensiones
def primos(a):
    #Crea una lista vacia para almacenar los resultados
    res=np.zeros(a.shape)
    #Verifica que el tamaño de la matriz si sea 2 dimensiones
    if len(a.shape)==2:
        #Toma el tamaño de la matriz en las filas ya que a.shape regresa una tupla de dos posiciones, se toma la primera que corresponde a las filas
        for i in range(a.shape[0]):
            #Toma el tamaño de la matriz en las columnas
            for j in range(a.shape[1]):
                #Se verifica si el elemento en cada posicion es primo usando la funcion primo() declarada más arriba
                if primo(a[i][j]):
                    res[i][j]=a[i][j]
    return res

#Funcion para hallar la suma de todos los elementos de una matriz de dos dimensiones
def sumaTot(a):
    total=0
    #Verifica que el tamaño de la matriz si sea 2 dimensiones
    if len(a.shape)==2:
        #Toma el tamaño de la matriz en las filas ya que a.shape regresa una tupla de dos posiciones, se toma la primera que corresponde a las filas
        for i in range(a.shape[0]):
            #Toma el tamaño de la matriz en las columnas
            for j in range(a.shape[1]):
                total+=a[i][j]
    return total