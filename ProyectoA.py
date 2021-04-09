import random
import time
import math
import sys
import operator

sys.setrecursionlimit(100000000)
from datetime import datetime
now = datetime.now()
print(now)

#MERGE SORT INVERSO  
def Merge(A,I,D):
    indIzq=0
    indDer=0
    for i in range (len(A)):
        if (indDer >= len(D)) or ( indIzq<len(I) and I[indIzq]>D[indDer] ):
            A[i]=I[indIzq]
            indIzq=indIzq+1
        else:
            A[i]=D[indDer]
            indDer=indDer+1

def MergeSort(A):
    if len(A)>1:
        mitad=len(A)//2
        ArrIzq=A[:mitad]
        ArrDer=A[mitad:]
        MergeSort(ArrIzq)
        MergeSort(ArrDer)
        Merge(A,ArrIzq,ArrDer)
#MERGE SORT INVERSO

#QUICK SORT INVERSO
def quickSortInverso(A):
    def quickSort(A,low,high):
            if low<high:
                    pivote=particion(A,low,high)
                    quickSort(A,low,pivote-1)
                    quickSort(A,pivote+1,high)
            
    def particion(A,low,high):
            i=low-1
            pivote=A[high]
            for j in range(low,high):
                    if (A[j]>=pivote):
                            i=i+1
                            swap(A,j,i)
            swap(A,i+1,high)
            return i+1

    def swap(A,j,i):
            temp=A[j]
            A[j]=A[i]
            A[i]=temp
            
    quickSort(A,0,len(A)-1)
#QUICK SORT INVERSO

#INSERTION SORT INVERSO
def insertionSortInverso(A):
    for i in range(1,len(A)):
        valor=A[i]
        j=i-1
        while (j>=0 and A[j]<valor):
            A[j+1]=A[j]
            j=j-1
        A[j+1]=valor
#INSERTION SORT INVERSO

#RADIX SORT INVERSO

def RadixSort(A):
    X=[0]*len(A)
    base=10
    k=max(A) #si esto es 100
    numDig=int(math.log10(k)+1) #esto es 3
    for i in range (numDig):
        X=CountingSort(A,i,base)
        A=X
    return X

def CountingSort(A,pos,base): 
    k=base-1
    n=len(A)
    B=[0]*n
    C=[0]*(k+1)
    for i in range(n): 
        digito=ObtenerDigito(A[i],pos,base)
        C[digito]=C[digito]+1
    C[base-1]=C[base-1]-1
    #print(C[base-1])
    for i in range( len(C)-1,0,-1 ):
        C[i-1]=C[i-1]+C[i]
    #print(C)
    for i in range (len(A)-1,-1,-1):
        digito=ObtenerDigito(A[i],pos,base)
        B[C[digito]]=A[i]
        C[digito]=C[digito]-1
        
    return B    

def ObtenerDigito(num,pos,base):
    digito=(num//10**pos)%10
    return digito
#RADIX SORT INVERSO

def todoElPrograma(A):
    ArregloParaInsertion = A
    ArregloParaRadix = A
    ArregloParaMerge = A
    ArregloParaQuick = A
    
    t1=time.time()
    insertionSortInverso(ArregloParaInsertion)
    t2=time.time()
    tiempoInsertion = t2-t1
    t3=time.time()
    print("Arreglo con Insertion Sort:",ArregloParaInsertion)
    x = RadixSort(ArregloParaRadix)
    t4=time.time()
    tiempoRadix = t4-t3
    print("Arreglo con Radix Sort:",x)
    t5=time.time()
    MergeSort(ArregloParaMerge)
    t6=time.time()
    print("Arreglo con Merge Sort:",ArregloParaMerge)
    tiempoMerge = t6-t5
    t7=time.time()
    quickSortInverso(ArregloParaQuick)
    t8=time.time()
    print("Arreglo con Quick Sort:",ArregloParaQuick)
    tiempoQuick = t8-t7
    diccionarioAlgoritmos = {'Quicksort':tiempoQuick, 'MergeSort':tiempoMerge, 'RadixSort':tiempoRadix, 'InsertionSort':tiempoInsertion}
    print("DICCIONARIO: ", diccionarioAlgoritmos)
    #print("RXS tardo ", diccionarioAlgoritmos['RadixSort']  )
    with open('resultados.eda2','w') as resultados:
        resultados.write(str(now)+"\n")
        tam = str(len(A))
        resultados.write("Tamaño de la colección: "+tam+"\n")       
        #Se itera sobre cada KEY                          #Pero KEY será VALUE
        elemDict = sorted(diccionarioAlgoritmos.items(), key=operator.itemgetter(1), reverse=False)
        for name in enumerate(elemDict):
            print(name[1][0], ' ha tardado ', diccionarioAlgoritmos[ name[1][0] ])
            resultados.write( str(name[1][0])+ ' ha tardado '+ str(diccionarioAlgoritmos[name[1][0]])+"[s]\n")
    



arr = []
t = True
try: #Primer try verifica que exista el archivo
    with open("C:/Users/52552/Desktop/Proyecto A/input.eda2", "r") as archivo:
        archivo.readline()   
        print("Se encontró el archivo")
                
except:
    print("El archivo no existe. La lista se generará aleatoriamente")

    while(t==True): #Para evitar excepciones como elingreso de un caracter o cadena
        try:
            n = int( input("Escribe el número de elementos del arreglo") )
            t = False
        except:
            print("Ingresa bien el numero")
    Arreglo=random.sample(range(0,n*n),n) #rango [0, n^2]
    todoElPrograma(Arreglo)
    sys.exit()

try: #El segundo verifica que esté en el formato correcto
    with open("C:/Users/52552/Desktop/Proyecto A/input.eda2", "r") as archivo:
        lista = [int(linea) for linea in archivo] #Esta linea generaría la excepción en caso de que el archivo no esté en el formato correcto   
        arr = lista
        todoElPrograma(arr)
        print(arr)

except:
    print("Formato de archivo incorrecto.")
    sys.exit(0)