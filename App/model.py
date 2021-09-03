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
def darObrasdeArtista(idArtista, obras):
    obrasArtista = lt.newList()
    for obra in obras:
        artistasObra = obra['ConstituentID']
        if idArtista in artistasObra:
            lt.addLast(obrasArtista, obra)
    return obrasArtista

# Funciones de consulta

def darListaNacionalidades(artistas):
    nacionalidades = lt.newList()
    for artista in artistas:
        obras = lt.newList()
        if(artista['Nacionalidad'] not in nacionalidades['Nombre']):
            elemento = {'Nombre': '', 'CantidadObras': 0, 'Obras': None}
            lt.addLast(nacionalidades, {artista['Nacionalidad'],0, obras})
    return nacionalidades

def darObrasNacionalidades(artistas, obras):
    nacionalidades = darListaNacionalidades(artistas)
    for artista in artistas:
        obrasArtista = darObrasdeArtista(artista['ConstituentID'], obras)
        posNacionalidad = lt.isPresent(nacionalidades, artista['Nationality'])
        nacionalidad = lt.getElement(nacionalidades, posNacionalidad)
        for obra in obrasArtista:
            lt.addLast(nacionalidad['Obras'], obra)
            nacionalidad['CantidadObras'] += 1
    return nacionalidades


# Funciones utilizadas para comparar elementos dentro de una lista
def compareartworks(title1, artworks):
    if (title1.lower() in artworks['Title'].lower()):
        return 0
    return -1

# Funciones de ordenamiento


