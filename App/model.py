"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from DISClib.DataStructures.arraylist import iterator, newList, size
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as shell
from DISClib.Algorithms.Sorting import insertionsort as insertion
from DISClib.Algorithms.Sorting import mergesort as merge
from DISClib.Algorithms.Sorting import quicksort as quick
assert cf
import time

"""
Se define la estructura de un catálogo
"""

# Construccion de modelos
def newCatalog(tipo):
    """
    Inicializa el catálogo. Crea una lista vacia para guardar
    todos los artistas, adicionalmente, crea una lista vacia para las obras de arte,
    Retorna el catalogo inicializado.
    """
    catalog = {'artists': None,
               'artworks': None}
    catalog['artists'] = lt.newList(tipo)
    catalog['artworks'] = lt.newList(tipo)

    return catalog

# Funciones para agregar informacion al catalogo
def addArtwork(catalog, artwork):
    artistasObra = lt.newList()
    artistasId = artwork['ConstituentID'].replace(']', '').replace('[', '').split(',')
    for i in lt.iterator(catalog['artists']):
        artista = i['Artista']
        if artista['ConstituentID'] in artistasId:
            lt.addLast(i['Obras'], artwork)
            lt.addLast(artistasObra, artista['DisplayName'])
    lt.addLast(catalog["artworks"],{'Obra': artwork, 'Artistas': artistasObra})

def addArtist(catalog, artist):
    # Se adiciona el libro a la lista de libros
    obras = lt.newList()
    lt.addLast(catalog["artists"],{'Artista': artist, 'Obras': obras})

# Funciones para creacion de datos
def crearListaNacionalidades(catalog):
    lista = catalog['artists']
    nacionalidades = lt.newList()
    soporte = lt.newList()
    for i in lt.iterator(lista):
        obras = i['Obras']
        artista = i['Artista']
        nacionalidad = artista['Nationality']
        if not(lt.isPresent(soporte, nacionalidad)):
            lt.addLast(soporte, nacionalidad)
            lt.addLast(nacionalidades, {'Nombre': nacionalidad, 'Obras':obras, 'Cantidad': lt.size(obras)})
        else:
            for j in lt.iterator(nacionalidades):
                if(j['Nombre'] == nacionalidad):
                    j['Cantidad'] += agregarObras(j['Obras'], obras)
        
                
    return nacionalidades
    
def agregarObras(lista, obras):
    nuevas = 0
    for i in lt.iterator(obras):
        esta = False
        for j in lt.iterator(lista):
            if i['Title'] == j['Title']:
                esta = True
            if esta == True:
                break
        if( esta == False):
            lt.addLast(lista, i)
            nuevas += 1
    return nuevas




# Funciones de consulta
def darArtistasObraNacionalidad(idartwork, catalog):
    artwork = None
    for i in lt.iterator(catalog['artworks']):
        if(i['Obra']['ObjectID'] == idartwork) :
            artwork = i
            break
    respuesta = ''
    if(artwork != None):
     for i in lt.iterator(artwork['Artistas']):
            respuesta += i+'. '
    return respuesta






# Funciones utilizadas para comparar elementos dentro de una lista
def compareartworks(title1, artworks):
    if (title1.lower() in artworks['Title'].lower()):
        return 0
    return -1

def cmpArtworkByDateAcquired(artwork1, artwork2):
    """
    Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de artwork2
    Args:
    artwork1: informacion de la primera obra que incluye su valor 'DateAcquired'
    artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired'
    """
    obra1 = artwork1['DateAcquired']
    obra2 = artwork2['DateAcquired']
    if obra1 < obra2:
        return True
    else:
        return False

def compararNacionalidades(nt1, nt2):
    cantidad1 = nt1['Cantidad']
    cantidad2 = nt2['Cantidad']
    if(cantidad1 > cantidad2):
        return True
    else:
        return False
    
# Funciones de ordenamiento

def ordenarObrasPorFecha(ordenamiento, tamano, catalog):
    obras = catalog['artworks']
    soporte = lt.newList()
    for i in lt.iterator(obras):
        lt.addLast(soporte, i['Obra'])
    lista = lt.subList(soporte, 0, tamano)
    start_time = time.process_time()
    if(ordenamiento == 'insertion'):
        listaOrdenada = insertion.sort(lista, cmpArtworkByDateAcquired)
    elif (ordenamiento == 'shell'):
        listaOrdenada = shell.sort(lista, cmpArtworkByDateAcquired)
    elif (ordenamiento == 'quick'):
        listaOrdenada = quick.sort(lista, cmpArtworkByDateAcquired)
    elif (ordenamiento == 'merge'):
        listaOrdenada = merge.sort(lista, cmpArtworkByDateAcquired)
    else:
        return None
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, listaOrdenada

def ordenarListaNacionalidades(catalog):
    nacionalidades = crearListaNacionalidades(catalog)
    return merge.sort(nacionalidades, compararNacionalidades)
