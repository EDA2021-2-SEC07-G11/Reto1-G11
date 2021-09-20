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
default_limit = 1000
sys.setrecursionlimit(default_limit*10)
from tabulate import tabulate


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
    print("2- SINGLE_LINKED")

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
    print('Titulo: ' + artwork['Obra']['Title'] )

def printartworkFecha(artwork):
    print('Titulo: ' + artwork['Obra']['Title'] + '. Fecha de adquisición: '+ artwork['Obra']['DateAcquired'] )

def printarworkInfo(artwork):
    print()

def printartist(artist):
    print('Nombre: ' + artist['Artista']['DisplayName'] )


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
        elif int(opciones[0]) == 2:
            tipo = 'SINGLE_LINKED'
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
        fechaInicial = input('Seleccione la fecha inicial en formato AAAA-MM-DD\n')
        formato = fechaInicial.split('-')
        if (len(formato) != 3 or len(formato[0]) != 4 or len(formato[1]) != 2 or len(formato[2]) != 2):
            print('Ha ingresado una fecha inicial inválida')
        else:
            fechaFinal = input('Seleccione la fecha final en formato AAAA-MM-DD\n')
            formato = fechaFinal.split('-')
            if(len(formato) != 3 or len(formato[0]) != 4 or len(formato[1]) != 2 or len(formato[2]) != 2 or fechaInicial > fechaFinal):
                print('Ha ingresado una fecha inicial inválida')
            else:
                lista = controller.ordenarObrasPorFecha(fechaInicial, fechaFinal, catalog)[1]
                total = lt.size(lista)
                print('El MOMA adquirió '+str(total)+ ' piezas únicas entre ' + fechaInicial + ' y '+fechaFinal)
                compradas = controller.darObrasCompradas(lista)
                artistas = controller.darCantidadArtistas(lista)
                print('Con '+str(artistas) +' artistas diferentes y compró '+str(compradas) +' de ellas')
                obras = []
                contador = 0
                puesto = 1
                while contador<3:
                    info = controller.darInfoObra(lt.getElement(lista, puesto)['Obra'], catalog)
                    info = [info[0],info[1],info[2],info[3],info[4],info[5],info[8],info[9]]
                    obras.append(info)
                    puesto+=1
                    contador+=1
                contador = 0
                puesto = lt.size(lista)-2
                while contador<3:
                    info = controller.darInfoObra(lt.getElement(lista, puesto)['Obra'], catalog)
                    info = [info[0],info[1],info[2],info[3],info[5],info[4],info[9],info[8]]
                    obras.append(info)
                    puesto+=1
                    contador+=1
                print('Las primeras y últimas 3 obras en el rango son...')
                print(tabulate(obras, headers=['ObjectID', 'Title', 'ArtistsNames','Medium','Dimensions','Date','DateAcquired','URL'], tablefmt='fancy_grid'))


        

    elif int(inputs[0]) == 4:
        pass

    elif int(inputs[0]) == 5:
        print('Clasificando los países por el número de obras asociadas...')
        lista = controller.darListaNacionalidadesOrdenada(catalog)
        contador = 0
        print('El TOP 10 de países en el MOMA son:')
        datos =[]
        for i in lt.iterator(lista):
            contador += 1
            datos.append([i['Nombre'],i['Cantidad']])
            if(contador == 10):
                break
        print(tabulate(datos, headers=['Nationality', 'Artworks'], tablefmt='fancy_grid'))
        primeraNacionalidad = lt.firstElement(lista)
        obrasPrimeraNacionalidad = primeraNacionalidad['Obras']
        obras = []
        contador = 0
        puesto = 1
        while contador<3:
            info = controller.darInfoObra(lt.getElement(obrasPrimeraNacionalidad, puesto), catalog)
            info = [info[0],info[1],info[2],info[3],info[4],info[5],info[6],info[7],info[8]]
            obras.append(info)
            puesto+=1
            contador+=1
        contador = 0
        puesto = lt.size(obrasPrimeraNacionalidad)-2
        while contador<3:
            info = controller.darInfoObra(lt.getElement(obrasPrimeraNacionalidad, puesto), catalog)
            info = [info[0],info[1],info[2],info[3],info[4],info[5],info[6],info[7],info[8]]
            obras.append(info)
            puesto+=1
            contador+=1
        print('La nacionalidad con mayor cantidad de obras en el museo es '+primeraNacionalidad['Nombre']+', que tiene '+str(primeraNacionalidad['Cantidad'])+' obras asociadas')
        print('La primeras y las últimas tres obras de la nacionalidad '+primeraNacionalidad['Nombre']+' son:')
        print(tabulate(obras, headers=['ObjectID', 'Title', 'ArtistsNames','Medium','Date','Dimensions','Department','Classification','URL'], tablefmt='fancy_grid'))



    elif int(inputs[0]) == 6:
        pass

    elif int(inputs[0]) == 7:
        pass

    else:
        sys.exit(0)
sys.exit(0)
