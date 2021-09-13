"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar Cronológicamente los Artistas")
    print("3- Listar Cronológicamente las Adquisiciones")
    print("4- Clasificar Obras de un Artista por Técnica")
    print("5- Clasificar Obras por la Nacionalidad de sus Creadores")
    print("6- Transportar Obras de un Departamento")
    print("7- Proponer una nueva exposición del museo")
    print("0- Salir")

def printMenuTipos():
    print("Seleccione el tipo de lista")
    print("1- ARRAY_LIST")
    print("2- LINKED_LIST")

def printMenuOrdenamientos():
    print("Seleccione el tipo de ordenamiento")
    print("1- Insertion Sort")
    print("2- Shell Sort")
    print("3- Merge Sort")
    print("4- Quick Sort")

catalog = None

def initCatalog(tipo):
    """
    Inicializa el catalogo
    """
    return controller.initCatalog(tipo)
    
def loadData(catalog):
    """
    Carga los datos en la estructura de datos
    """
    controller.loadData(catalog)

def printartwork(artwork):
    print('Titulo: ' + artwork['Title'] )

def printartworkFecha(artwork):
    print('Titulo: ' + artwork['Title'] + '. Fecha de adquisición: '+ artwork['DateAcquired'] )

def printartist(artist):
    print('Nombre: ' + artist['DisplayName'] )

def imprimir_ultimostresworks(lista):
    print("Estas son las ultimas tres obras: ")
    contador=0
    puesto=lt.size(lista)
    while contador<3:
        printartwork(lt.getElement(lista,puesto))
        puesto+=-1
        contador+=1

def imprimir_ultimostresworksFecha(lista):
    print("Estas son las últimas tres obras: ")
    contador=0
    puesto=lt.size(lista) - 2
    while contador<3:
        printartworkFecha(lt.getElement(lista,puesto))
        puesto+=1
        contador+=1

def imprimir_primerostresworksFecha(lista):
    print("Estas son las primeras tres obras: ")
    contador=0
    puesto=1
    while contador<3:
        printartworkFecha(lt.getElement(lista,puesto))
        puesto+=1
        contador+=1

def imprimir_ultimostresartist(lista):
    print("Estas son los ultimos tres artistas: ")
    contador=0
    puesto=lt.size(lista)
    while contador<3:
        printartist(lt.getElement(lista,puesto))
        puesto+=-1
        contador+=1

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        tipo = ''
        printMenuTipos()
        opciones = input('Seleccione una opción para continuar\n')
        if int(opciones[0]) == 1:
            tipo = 'ARRAY_LIST'
        elif int(opciones[0] == 2):
            tipo = 'LINKED_LIST'
        print("Cargando información de los archivos ....")
        catalog = initCatalog(tipo)
        loadData(catalog)
        print('Obras Cargadas: ' + str(lt.size(catalog['artworks'])))
        lista=catalog["artworks"]
        imprimir_ultimostresworks(lista)
        print('Artistas cargados: ' + str(lt.size(catalog['artists'])))
        lista=catalog["artists"]
        imprimir_ultimostresartist(lista)
    elif int(inputs[0]) == 2:
        pass
    elif int(inputs[0]) == 3:
        lista = catalog['artworks']
        muestra = input('Seleccione el tamaño de la muestra\n')
        if(muestra.isnumeric()):
            muestra = int(muestra)
            total = lt.size(lista)
            if(muestra > total or muestra <= 0):
                print('Tamaño inválido')
            else:
                ordenamiento = ''
                printMenuOrdenamientos()
                opciones = input('Seleccione una opción para continuar\n')
                if int(opciones[0]) == 1:
                    result = controller.ordenarObrasPorFecha('insertion', muestra, catalog)
                    print("Para la muestra de", muestra, " elementos, el tiempo (mseg) es: ", str(result[0]))
                    imprimir_primerostresworksFecha(result[1])
                    imprimir_ultimostresworksFecha(result[1])

                elif int(opciones[0]) == 2:
                    result = controller.ordenarObrasPorFecha('shell', muestra, catalog)
                    print("Para la muestra de", muestra, " elementos, el tiempo (mseg) es: ", str(result[0]))
                elif int(opciones[0]) == 3:
                    result = controller.ordenarObrasPorFecha('merge', muestra, catalog)
                    print("Para la muestra de", muestra, " elementos, el tiempo (mseg) es: ", str(result[0]))
                elif int(opciones[0]) == 4:
                    result = controller.ordenarObrasPorFecha('quick', muestra, catalog)
                    print("Para la muestra de", muestra, " elementos, el tiempo (mseg) es: ", str(result[0]))
                else:
                    print('Seleccione una opción válida')
        else:
            print('Tamaño inválido')

    elif int(inputs[0]) == 4:
        pass


    elif int(inputs[0]) == 5:
        pass

    elif int(inputs[0]) == 6:
        pass

    elif int(inputs[0]) == 7:
        pass

    else:
        sys.exit(0)
sys.exit(0)
