from logic.logic import leer_json_a_lista,leer_json_a_dicionario, agregar_datos_a_lista, guardar_lista_en_json
import json

#Ejercicios de Listas y Tuplas
#-----------------------------
#Ejercicio 1
#Escribir un programa que almacene las asignaturas de un
#curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
#en una lista y la muestre por pantalla.
def desingTypeOneExOne():
    
    print("    Este es un programa para añadir y guardar cursos \n")
    while True:
        try:
            while True:
                ruta = "databases/dataTypeOneExOne.json"
                lista_datos = leer_json_a_lista(ruta)
                print(f"""    El listado actual es el siguiente:
    {lista_datos}""")

                cursoNombre = str(input("    Ingrese el Cursos que desee añadir a la lista: "))
                
                lista_datos = agregar_datos_a_lista(lista_datos,cursoNombre)
                
                guardar_lista_en_json(ruta,lista_datos) 
                
                print(f"    la lista actual ahora es {lista_datos}")

                print("    Desea agregar otro elemento?: ")
                respuesta = input ("    1) si 2)no ")
                if respuesta == "1" or respuesta == "si":
                    pass
                else:
                    return print("Ok")
        except:
            pass

#Ejercicio 2

#scribir un programa que almacene las asignaturas de un curso
#(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
#en una lista y la muestre por pantalla el mensaje `Yo estudio <asignatura>`,
#donde `<asignatura>` es cada una de las asignaturas de la lista.
# 

def desingTypeOneExTwo():
    print("    Este es un programa para añadir , guardar cursos e imprimirlos en consola \n")
    while True:
        try:
            while True:
                ruta = "databases/dataTypeOneExTwo.json"
                lista_datos = leer_json_a_lista(ruta)
                print(f"""    El listado actual es el siguiente:
    {lista_datos}""")

                cursoNombre = str(input("    Ingresar los cursos que yo estudio: "))
                
                lista_datos = agregar_datos_a_lista(lista_datos,cursoNombre)
                
                guardar_lista_en_json(ruta,lista_datos) 
                
                print(f"    Yo estudio:", ",".join(map(str,lista_datos)))

                print("    Desea agregar otro elemento?: ")
                respuesta = input ("    1) si 2)no ")
                if respuesta == "1" or respuesta == "si":
                    pass
                else:
                    return print("Ok")
        except:
            pass


#-----------------------------
# Ejercicio 3

#Escribir un programa que almacene las asignaturas de un curso 
#(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
#en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y
#después las muestre por pantalla con el mensaje `En <asignatura> has sacado <nota>` donde
#`<asignatura>` es cada una des las asignaturas de la lista y `<nota>`
#cada una de las correspondientes notas introducidas por el usuario.


def desingTypeOneExThree():

    ruta = "databases/dataTypeOneExThree.json"
    
    mattersAndNotes = leer_json_a_dicionario(ruta)
    

    if mattersAndNotes :
        allMatters = []
        
    else :
        allMatters = []
        mattersAndNotes={}
    
    print("    This is a program to match the subjects with the note")
    while True: 
        try:
            matters = str(input("    Enter the subjects: "))
            allMatters.append(matters)
                     
            awnser = int(input(f"    Do you need to add more? 1)yes 2)no (1-2)" ))

            
            if awnser != 1:
                dictlen = len(allMatters)
                
                for i in range(0,dictlen):
                    noteMatter = input(f"    Enter the note for {allMatters[i]}: ")
                    mattersAndNotes.update({allMatters[i]:noteMatter})

                    
                    
                guardar_lista_en_json(ruta, mattersAndNotes)

                for key, value in mattersAndNotes.items():
                    print(f"    For the subjects {key} you have: {value}")
                print("")
                break
            
            else:
                pass
                
        except ValueError:
            pass
            

    


 #last line if code



## Ejercicio 4

#Escribir un programa que pregunte al usuario los números ganadores 
#de la lotería primitiva, los almacene en una lista y los muestre por 
#pantalla ordenados de menor a mayor.

def desingTypeOneExFour():
    
        ruta = "databases/dataTypeOneExFour.json"
        lista = leer_json_a_lista(ruta)
            
        try:
            while True:    
                nuevosDatos = int(input("    Enter the numbers for primivite lottery: "))
                
                lista.append(nuevosDatos)
                
                awnser = int(input(f"    Do you want to enter a new number? 1)yes 2)no: "))
                
                
                if awnser == 2:
                
                    lista.sort()
                    print(f"    This is the winning numbers for primitive lottery \n    {lista}")
                    
                    
                    guardar_lista_en_json(ruta, lista)
                    break
                
                else :
                    
                    pass
        except:
            pass


## Ejercicio 5

#Escribir un programa que almacene en una lista los números del 1 
#al 10 y los muestre por pantalla en orden inverso separados por comas.      


def desingTypeOneExFive():
    
    ruta = "databases/dataTypeOneExFive.json"
    lista = leer_json_a_lista(ruta)
            
    try:
        while True:    
            nuevosDatos = int(input("    Enter the numbers between 1 - 10: "))
            
            if nuevosDatos < 1 or nuevosDatos > 10:
                raise ValueError
                        
            lista.append(nuevosDatos)
            
            awnser = int(input(f"    Do you want to enter a new number? 1)yes 2)no: "))
            
            
            if awnser == 2:
            
                lista.sort(reverse=True)
                print(f"    This is the list for the numbers in descendend order ", ",".join(map(str,lista) ) )
                
                
                guardar_lista_en_json(ruta, lista)
                break
            
            else :
                pass
    except ValueError:
        print("    Enter the correct number")
        pass



# Ejercicio 6

#Escribir un programa que almacene 
#las asignaturas de un curso (por ejemplo 
#Matemáticas, Física, Química, Historia y Lengua) en una lista,
#pregunte al usuario la nota que ha sacado en cada asignatura y elimine de
#la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla 
#las asignaturas que el usuario tiene que repetir.

def desingTypeOneExSix():
    print("\nDISCLAIMER: For this especific type of exercise we accept true only notes above 50 pts\n")
    ruta = "databases/dataTypeOneExSix.json"
        
    mattersAndNotes = leer_json_a_dicionario(ruta)
    
    if mattersAndNotes :
        allMatters = []
        
    else :
        allMatters = []
        mattersAndNotes={}

    print("    This is a program to match the subjects with the note")
    while True: 
        try:
            matters = str(input("    Enter the subjects: "))
            allMatters.append(matters)
                        
            awnser = int(input(f"    Do you need to add more? 1)yes 2)no (1-2)" ))

            
            if awnser != 1:
                dictlen = len(allMatters)
                
                for i in range(0,dictlen):
                    
                    noteMatter = int(input(f"    Enter the note for {allMatters[i]}: "))

                    if noteMatter < 50: 
                        mattersAndNotes.update({allMatters[i]:noteMatter})
                    else:
                        pass

                    
                    
                guardar_lista_en_json(ruta, mattersAndNotes)

                for key, value in mattersAndNotes.items():
                    print(f"    You need to repeat this subject {key} ")
                print("")
                break
            
            else:
                pass
                
        except ValueError:
            pass


## Ejercicio 7

#Escribir un programa que almacene el abecedario en una lista,
#elimine de la lista las letras que ocupen posiciones múltiplos de 3,
#  y muestre por pantalla la lista resultante.


def desingTypeOneExSeven():

    ruta = "databases/dataTypeOneExSeven.json"
    print("    This is a program that show you all letters of the alphabet that number position is multiple of three ")
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    nweAlphabet = []
    
    
    a = int(len(alphabet)) 
        
    for i in range (0,a):
        if i % 3 == 0:
            print(f"    { alphabet[i] }")
            nweAlphabet.append(alphabet[i])

        
    guardar_lista_en_json(ruta,nweAlphabet)

## Ejercicio 8

#Escribir un programa que pida al usuario una
# palabra y muestre por pantalla si es un palíndromo.

def desingTypeOneExEight():
    ruta = "databases/dataTypeOneExEight.json"
    print("    This is a program to know if a word is palindrome or not")
    word = str(input("    Enter the word: "))
    firstWord = []
    firstWord.append(word)
    secondWord = [chain[::-1] for chain in firstWord]
    
    if firstWord == secondWord:
        print(f"    The word {word} is palindrome ")
        lista = leer_json_a_lista(ruta)
        lista.append(word)
        guardar_lista_en_json(ruta,lista)
        
    else:
        print(f"    The word {word} is not a palindrome ")
    
    
## Ejercicio 9

#Escribir un programa que pida al usuario 
# una palabra y muestre por pantalla el número
# de veces que contiene cada vocal.

def desingTypeOneExNine():
    
    ruta = "databases/dataTypeOneExNine.json"
    
    chain = str(input("    Enter the word")).lower()
    
    vocals = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for caracter in chain:
        if caracter in vocals:
            vocals[caracter] += 1
            
            lista = leer_json_a_dicionario(ruta)
            lista.update(vocals)
        
    vocals.update({ 'Word':str(chain)})
    lista.update({ 'Word':str(chain)})
    guardar_lista_en_json(ruta,lista)
            
            
            
            
    print(f"""    The word {chain} have this amount of vocals 
    {vocals}""")
    
    
# Ejercicio 10

#Escribir un programa que almacene
#en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8,
#y muestre por pantalla el menor y el mayor de los precios.
    
def desingTypeOneExTen():
    print("    This is a program for sort a list of numbers")
    
    ruta = "databases/dataTypeOneExTen.json"
    lista = leer_json_a_lista(ruta)
    print(f"    Numbers before {lista}")
    lista.sort()
    print("")
    print(f"    Numbers after {lista}")
    
    
#-----------------------------------------------------    
#-----------------------------------------------------
# Ejercicios de Diccionarios

## Ejercicio 1

#Escribir un programa que guarde en una variable el diccionario 
# `{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}`, pregunte al usuario 
# por una divisa y muestre su símbolo o un mensaje de aviso si la 
# divisa no está en el diccionario.

def desingTypeTwoExOne():
    ruta = "databases/dataTypeTwoExOne.json"
    currency = str(input("    Enter the currency that you want to Know its symbol: ")).lower()
    diccionario = leer_json_a_dicionario(ruta)
    print(f"""    {diccionario.get(currency,"This currency dont exist in this data base")}""")
    
def desingTypeTwoExTwo():
    pass
    
    
    
    


    





#last line of code