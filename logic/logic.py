#razonamiento logico

import json

def leer_json_a_lista(ruta):
    """
    Lee un archivo JSON desde una ruta específica y lo convierte en una lista.
    
    Parámetros:
        ruta (str): Ruta del archivo JSON.

    Retorna:
        list: Lista de lista cargados desde el archivo JSON.
    """
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            lista = json.load(archivo)
            if not isinstance(lista, list):
                raise ValueError("El archivo JSON no contiene una lista.")
                
            
            return lista
    except FileNotFoundError:
        print("El archivo no existe.")
        return []
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON.")
        return []

def agregar_datos_a_lista(lista, nuevos_datos):
    """
    Agrega nuevos datos a una lista existente.

    Parámetros:
        lista (list): Lista existente a la que se agregarán lista.
        nuevos_datos (any): Datos que se agregarán a la lista.

    Retorna:
        list: Lista actualizada.
    """
    if isinstance(lista, list):
        lista.append(nuevos_datos)
    else:
        print("El objeto proporcionado no es una lista.")
    return lista

def guardar_lista_en_json(ruta, lista):
    """
    Guarda una lista en un archivo JSON en la ruta especificada.

    Parámetros:
        ruta (str): Ruta donde se guardará el archivo JSON.
        lista (list): Lista a guardar en formato JSON.
    """
    try:
        with open(ruta, 'w', encoding='utf-8') as archivo:
            json.dump(lista, archivo, indent=4, ensure_ascii=False)
            print(f"    Archivo guardado exitosamente en: {ruta}")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")
