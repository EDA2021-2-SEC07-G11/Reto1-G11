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
    if(tipo == 'ARRAY_LIST'):
        catalog['artists'] = lt.newList('ARRAY_LIST')
        catalog['artworks'] = lt.newList('ARRAY_LIST')
    elif(tipo == 'SINGLE_LINKED'):
        catalog['artists'] = lt.newList('SINGLE_LINKED')
        catalog['artworks'] = lt.newList('SINGLE_LINKED')
    else:
        catalog['artists'] = lt.newList()
        catalog['artworks'] = lt.newList()
    return catalog

# Funciones para agregar informacion al catalogo
def addArtwork(catalog, artwork):
    artistasObra = lt.newList()
    artistasId = artwork['ConstituentID'].replace('[','').replace(']','').split(',')
    n = 0
    while n < len(artistasId):
        artistasId[n] = artistasId[n].lstrip()
        n += 1
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
    total = 0
    for i in lt.iterator(nacionalidades):
        total += i['Cantidad']
    print('El total de obras de nacoinalidades es'+ str(total))
        
                
    return nacionalidades
    
def agregarObras(lista, obras):
    nuevas = 0
    for i in lt.iterator(obras):
        esta = False
        for j in lt.iterator(lista):
            if i['ObjectID'] == j['ObjectID']:
                esta = True
                break
        if( esta == False):
            lt.addLast(lista, i)
            nuevas += 1
    return nuevas
def crearlistaID(name,catalogo):
    for artista in catalogo["artists"]:
        idart=artista["Artista"]["ConstituentID"]
        return idart




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

def darObrasEnRangoFecha(catalog, inicial, final):
    obras = catalog['artworks']
    lista = lt.newList()
    for i in lt.iterator(obras):
        fecha = i['Obra']['DateAcquired']
        if(fecha >= inicial and fecha <= final):
            lt.addLast(lista, i)
    return lista

def darObrasCompradas(lista):
    total = 0
    for i in lt.iterator(lista):
        metodo = i['Obra']['CreditLine']
        if 'purchase' in metodo.lower():
            total += 1
    return total

def darCantidadArtistas(obras):
    total = 0
    artistas = lt.newList()
    for i in lt.iterator(obras):
        artistasObra = i['Artistas']
        for artista in lt.iterator(artistasObra):
            if not(lt.isPresent(artistas, artista)):
                lt.addLast(artistas, artista)
    return lt.size(artistas)
def organizarObrasEstilo(nombre,catalog):
    if nombreobras(nombre,catalog)== False:
        return False
    else:


        listaobras=nombreobras(nombre,catalog)[0]
        idart=nombreobras(nombre,catalog)[1]
        return listamedios(listaobras,idart)

def nombreobras(nombreart,catalog):
    listaart=(catalog["artists"])
    listaobr=(catalog["artworks"])
    encontro=False
    for i in range(0,(lt.size(listaart))):
        elemento=lt.getElement(listaart,i)
        nombre=elemento['Artista']['DisplayName']
        lnombre=nombre.split(",")
        nombre=lnombre[0]
        if nombreart==nombre:
            encontro=True
            idart=elemento["Artista"]["ConstituentID"]
    if encontro==True:
        listaobrart=lt.newList("ARRAY_LIST")        
        for e in range(0,(lt.size(listaobr))):
            elemento=lt.getElement(listaobr,e)
            idartobr=elemento["Obra"]["ConstituentID"]
            if idart in idartobr:
                lt.addLast(listaobrart,elemento)
        return listaobrart,idart
    else:
        return False
def listamedios(listaobras,idart):
    listamedios=[]
    for b in range(0,(lt.size(listaobras))):
        elemento=lt.getElement(listaobras,b)
        medio=elemento["Obra"]["Medium"]
        listamedios.append(medio)
    listaest=[]
    listanum=[]
    for elemento in listamedios:
        if elemento not in listaest:
            listaest.append(elemento)
            cuenta=listamedios.count(elemento)
            listaest.append(cuenta)
            listanum.append(cuenta)
    maximo=max(listanum)
    listadef=[]
    while len(listadef)<5:
        for n in range(0,len(listaest)-1):
            estilo=listaest[n]
            if listaest[n+1]==maximo:
                listap=[]
                listap.append(estilo)
                listap.append(maximo)
                listadef.append(listap)
        maximo+=-1
    mas_u_est=listadef[0][0]

    listmas_u_est=[]
    for b in range(0,(lt.size(listaobras))):
        elemento=lt.getElement(listaobras,b)
        medio=elemento["Obra"]["Medium"]
        if medio==mas_u_est:
            linea=[]
            linea.append(elemento["Obra"]["ObjectID"])
            linea.append(elemento["Obra"]["Title"])
            linea.append(elemento["Obra"]["Medium"])
            linea.append(elemento["Obra"]["Date"])
            linea.append(elemento["Obra"]["Dimensions"])
            linea.append(elemento["Obra"]["DateAcquired"])
            linea.append(elemento["Obra"]["Department"])
            linea.append(elemento["Obra"]["Classification"])
            listmas_u_est.append(linea)
    return idart,len(listanum),len(listamedios),listadef, listmas_u_est
def darInfoObra(artwork, catalog):
    iD = artwork['ObjectID']
    nombre = artwork['Title']
    if len(nombre) > 20:
        contador = 20
        while contador < len(nombre):
            if(nombre[contador-2] == ' '):
                nombre = nombre[:contador-1]+'\n'+nombre[contador-1:]
            else: 
                nombre = nombre[:contador]+'\n'+nombre[contador:]
            contador+=20
    artistas =''
    artistasLista = darArtistasObraNacionalidad(iD, catalog).split('.')

    for i in artistasLista:
        artistas += i+'\n'
   
    medio = artwork['Medium']
    if len(medio) > 20:
        contador = 20
        while contador < len(medio):
            if (medio[contador-2]==' '):
                medio = medio[:contador-1]+'\n'+medio[contador-1:]
            else:
                medio = medio[:contador]+'\n'+medio[contador:]
            contador+=20
    fecha = artwork['Date']
    if (artwork['Dimensions'] != ''):
        dimensiones = artwork['Dimensions']
        if len(dimensiones) > 22:
            contador = 22
            while contador < len(dimensiones):
                if(dimensiones[contador-2]==' '):
                    dimensiones = dimensiones[:contador-1]+'\n'+dimensiones[contador-1:]
                else:
                    dimensiones = dimensiones[:contador]+'\n'+dimensiones[contador:]
                contador+=22
    else:
        dimensiones = 'Unknown'
    departamento = artwork['Department']
    clasificacion = artwork['Classification']
    if(artwork['URL'] != ''):
        Url = artwork['URL']
        if len(Url) >17:
            contador = 17
            while contador < len(Url):
                Url = Url[:contador]+'\n'+Url[contador:]
                contador+=17
    else:
        Url = 'Unknown'

    fechaCompra = artwork['DateAcquired']
    return iD,nombre,artistas,medio,fecha,dimensiones,departamento,clasificacion,Url, fechaCompra







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
    obra1 = artwork1['Obra']['DateAcquired']
    obra2 = artwork2['Obra']['DateAcquired']
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

def ordenarObrasPorFecha(inicial, final, catalog):
    lista = darObrasEnRangoFecha(catalog, inicial, final)
    start_time = time.process_time()
    lista= merge.sort(lista, cmpArtworkByDateAcquired)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, lista

def ordenarListaNacionalidades(catalog):
    nacionalidades = crearListaNacionalidades(catalog)
    return merge.sort(nacionalidades, compararNacionalidades)
