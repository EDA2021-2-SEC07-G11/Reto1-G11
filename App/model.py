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
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo
"""

# Construccion de modelos
def newCatalog():
    """
    Inicializa el catálogo. Crea una lista vacia para guardar
    todos los artistas, adicionalmente, crea una lista vacia para las obras de arte,
    Retorna el catalogo inicializado.
    """
    catalog = {'artists': None,
               'artworks': None}

    catalog['artists'] = lt.newList()
    catalog['artworks'] = lt.newList()

    return catalog

# Funciones para agregar informacion al catalogo
def addArtwork(catalog, artwork):
    lt.addLast(catalog["artworks"],artwork)
    # Se adiciona el libro a la lista de libros

def addArtist(catalog, artist):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog["artists"],artist)


# Funciones para creacion de datos
def darObrasdeArtista(idArtista, catalog):
    obras = catalog['artworks']
    obrasArtista = lt.newList()
    for n in range (1, lt.size(obras)):
        obra = lt.getElement(obras, n)
        artistasObra = obra['ConstituentID']
        if idArtista in artistasObra:
            lt.addLast(obrasArtista, obra)
    return obrasArtista

# Funciones de consulta

def darListaNacionalidades(catalog):
    artistas = catalog["artists"]
    nacionalidades = lt.newList(key='Nombre')
    numeroArtistas = lt.size(artistas)
    for cont in range (1, numeroArtistas):
        obras = lt.newList()
        artista = lt.getElement(artistas, cont)
        nacionalidadArtista = artista['Nationality']
        numeroNacionalidades = lt.size(nacionalidades)
        esta = False
        if(numeroNacionalidades>0):
            for cont in range (1,numeroNacionalidades):
                elemento = lt.getElement(nacionalidades, cont)
                if(elemento['Nombre']==nacionalidadArtista):
                    esta = True
        if (esta == False):
            nuevaNacionalidad = {'Nombre':nacionalidadArtista, 'NumeroObras': 0 , 'Obras': obras}
            lt.addLast(nacionalidades, nuevaNacionalidad)
    return nacionalidades

def darObrasNacionalidades(catalog):
    artistas = catalog['artists']
    obras = catalog['artworks']
    nacionalidades = darListaNacionalidades(catalog)
    for n in range (1, lt.size(artistas)):
        artista = lt.getElement(artistas, n)
        obrasArtista = darObrasdeArtista(artista['ConstituentID'], catalog)
        posNacionalidad = 0
        for n in range (1, lt.size(nacionalidades)):
            nacionalidad = lt.getElement(nacionalidades, n)
            if nacionalidad['Nombre'] == artista['Nationality']:
                posNacionalidad = n
        nacionalidad = lt.getElement(nacionalidades, posNacionalidad)
        for n in range(1,lt.size(obrasArtista)):
            obra = lt.getElement(obrasArtista, n)
            lt.addLast(nacionalidad['Obras'], obra)
            nacionalidad['NumeroObras'] += 1
    return nacionalidades


# Funciones utilizadas para comparar elementos dentro de una lista
def compareartworks(title1, artworks):
    if (title1.lower() in artworks['Title'].lower()):
        return 0
    return -1


# Funciones de ordenamiento


