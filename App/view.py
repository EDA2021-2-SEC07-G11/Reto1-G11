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

catalog = None

def initCatalog():
    """
    Inicializa el catalogo
    """
    return controller.initCatalog()
    
def loadData(catalog):
    """
    Carga los datos en la estructura de datos
    """
    controller.loadData(catalog)

def printartwork(artwork):
    print('Titulo: ' + artwork['Title'] )

def printartist(artist):
    print('Nombre: ' + artist['DisplayName'] )

def imprimir_ultimostresworks(lista):
    print("Estos son las ultimas tres obras: ")
    contador=0
    puesto=lt.size(lista)
    while contador<3:
        printartwork(lt.getElement(lista,puesto))
        puesto+=-1
        contador+=1

def imprimir_ultimostresartist(lista):
    print("Estos son los ultimos tres artistas: ")
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
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print('Obras Cargadas: ' + str(lt.size(catalog['artworks'])))
        lista=catalog["artworks"]
        imprimir_ultimostresworks(lista)
        print('Autores cargados: ' + str(lt.size(catalog['artists'])))
        lista=catalog["artists"]
        imprimir_ultimostresartist(lista)
    elif int(inputs[0]) == 2:
        pass

    elif int(inputs[0]) == 3:
        pass

    elif int(inputs[0]) == 4:
        pass


    elif int(inputs[0]) == 5:
        print('Cargando Información...')
        lista = controller.darObrasNacionalidad(catalog)
        for n in range (1,lt.size(lista)):
            nacionalidad = lt.getElement(lista, n)
            print('Nacionalidad número '+ str(n)+': '+nacionalidad['Nombre']+'. Tiene '+str(nacionalidad['NumeroObras'])+' obras asociadas')
        nacionalidad = lt.firstElement(lista)
        print('La Nacionalidad con más obras es: '+nacionalidad['Nombre']+'. Las obras cuyo artista tiene esta nacionalidad son: ')
        for n in range(1, lt.size(nacionalidad['Obras'])):
            obra = lt.getElement(nacionalidad['Obras'], n)
            artistasObra = controller.darArtistasObra(obra, catalog)
            print('Tiene: '+str(lt.size(artistasObra))+' Artistas')
            print('Obra número '+str(n)+': ')
            print('Título: '+ obra['Title'])
            artistas = ''
            if(lt.size(artistasObra)>1):
             for m in range (1, lt.size(artistasObra)):
                    artistas = artistas + ' ' + str(lt.getElement(artistasObra, m)['DisplayName'])
            else:
                artistas = artistas + ' ' + str(lt.getElement(artistasObra, 1)['DisplayName'])
            print('Artistas: '+artistas)
            print('Fecha de la Obra: '+obra['Date'])
            print('Medio: '+obra['Medium'])
            if(obra['Dimensions'] != ''):
                print('Dimensiones: '+ obra['Dimensions'])
            elif (obra['Duration (sec.)'] != ''):
                print('Duración: '+ obra['Duration (sec.)'])
            else:
                print('Dimensiones Desconocidas')

    elif int(inputs[0]) == 6:
        pass

    elif int(inputs[0]) == 7:
        pass

    else:
        sys.exit(0)
sys.exit(0)
