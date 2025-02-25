﻿"""
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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de Artistas

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtists(catalog)
    loadArtworks(catalog)

def loadArtists(catalog):
    """
    Carga los artistas del archivo. 
    """
    artistsFile = cf.data_dir + 'MoMA/Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artistsFile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)

def loadArtworks(catalog):
    """
    Carga todas las obras de arte del archivo
    """
    artworksFile = cf.data_dir + 'MoMA/Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artworksFile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)

# Funciones de ordenamiento

    
    

# Funciones de consulta sobre el catálogo
def ordenarObrasPorFecha(inicial, final, catalog):
    return model.ordenarObrasPorFecha(inicial, final, catalog)
def organizarObrasEstilo(nombre,catalog):
    if model.organizarObrasEstilo(nombre,catalog)==False:
        return False
    else:
        return model.organizarObrasEstilo(nombre,catalog)

def ordenarArtistasPorFecha(inicial, final, catalog):
    return model.ordenarArtistasPorFecha(inicial, final, catalog)

def darListaNacionalidadesOrdenada(catalog):
    return model.ordenarListaNacionalidades(catalog)

def darArtistasObra(artwork, catalog):
    return model.darArtistasObraNacionalidad(artwork, catalog)

def darObrasCompradas(lista):
    return model.darObrasCompradas(lista)

def darCantidadArtistas(obras):
    return model.darCantidadArtistas(obras)

def darInfoObra(artwork,catalog):
    return model.darInfoObra(artwork,catalog)
def darInfoID(name,catalog):
    return model.crearlistaID(name,catalog)

def darInfoArtista(artist,catalog):
    return model.darInfoArtista(artist,catalog)

def darCostoObras(lista):
    return model.darCostoLista(lista)

def darPesoObras(lista):
    return model.darPesoTotal(lista)

def darObrasDepartamento(departamento, catalog):
    return model.ordenarObrasDepartamento(departamento, catalog)

def darObrasPorVejez(lista):
    return model.ordenarObrasPorVejez(lista)

def darCostoObra(artwork):
    return model.darCostoObra(artwork)

