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


from DISClib.DataStructures.arraylist import newList, size
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
    lt.addLast(catalog["artworks"],artwork)
    # Se adiciona el libro a la lista de libros

def addArtist(catalog, artist):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog["artists"],artist)


# Funciones para creacion de datos


# Funciones de consulta

def darArtistasObra(obra, catalog):
    artistas = catalog['artists']
    lista = lt.newList()
    artistasObra = obra['ConstituentID']
    for n in range(1, lt.size(artistas)):
        artista = lt.getElement(artistas, n)
        if artista['ConstituentID'] in artistasObra:
            lt.addFirst(lista, artista)
    return lista





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


    
# Funciones de ordenamiento

def ordenarObrasPorFecha(ordenamiento, tamano, catalog):
    obras = catalog['artworks'] 
    lista = lt.subList(obras, 0, tamano)
    lista = lista.copy()
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


