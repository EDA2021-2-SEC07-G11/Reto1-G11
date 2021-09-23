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
def newCatalog():
    """
    Inicializa el catálogo. Crea una lista vacia para guardar
    todos los artistas, adicionalmente, crea una lista vacia para las obras de arte,
    Retorna el catalogo inicializado.
    """
    catalog = {'artists': None,
               'artworks': None}
    catalog['artists'] = lt.newList('ARRAY_LIST')
    catalog['artworks'] = lt.newList('ARRAY_LIST')
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

def darArtistasEnRangoFecha(catalog, inicial, final):
    artistas = catalog['artists']
    lista = lt.newList()
    for i in lt.iterator(artistas):
        fecha = i['Artista']['BeginDate']
        if(fecha >= inicial and fecha <= final):
            lt.addLast(lista, i['Artista'])
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
        if len(Url) >16:
            contador = 16
            while contador < len(Url):
                Url = Url[:contador]+'\n'+Url[contador:]
                contador+=16
    else:
        Url = 'Unknown'

    fechaCompra = artwork['DateAcquired']
    return iD,nombre,artistas,medio,fecha,dimensiones,departamento,clasificacion,Url, fechaCompra


def darInfoArtista(artist, catalog):

    iD = artist['ConstituentID']

    nombre = artist['DisplayName']

    fecha = artist['BeginDate']

    nacionalidad = artist['Nationality']

    if nacionalidad == '':
        nacionalidad = 'Unknown'

    genero = artist['Gender']

    if genero == '':
        genero = 'Unknown'

    bio = artist['ArtistBio']
    
    wiki = artist['Wiki QID']

    if wiki == '':
        wiki = 'Unknown'

    ulan = artist['ULAN']

    if ulan == '':
        ulan = 'Unknown'

    return iD,nombre,fecha,nacionalidad,genero,bio,wiki,ulan

def darObrasDepartamento(departamento, catalog):
    obras = catalog['artworks']
    lista = lt.newList()
    for i in lt.iterator(obras):
        obra = i['Obra']
        depObra = obra['Department']
        if depObra == departamento:
            lt.addLast(lista, i)
    return lista

def darPesoTotal(lista):
    peso = 0
    for i in lt.iterator(lista):
        obra = i['Obra']
        if(obra['Weight (kg)'] != ''):
            peso += float(obra['Weight (kg)'])
    return peso

def darCostoObra(artwork):
    costo = 0
    if artwork['Weight (kg)'] != '':
        peso = float(artwork['Weight (kg)'])
    else:
        peso = 0
    tamano = 0
    alto = artwork['Height (cm)']
    largo = artwork['Length (cm)']
    ancho = artwork['Width (cm)']
    if alto != '':
        alto = float(alto)/100
        tamano = alto
        if largo != '':
            largo = float(largo)/100
            tamano *= largo
            if(ancho != ''):
                ancho = float(ancho)/100
                tamano *= ancho
        else:
            if(ancho != ''):
                ancho = float(ancho)/100
                tamano *= ancho
    elif largo != '':
        largo = float(largo)/100
        tamano = largo
        if ancho != '':
            ancho = float(ancho)/100
            tamano *= ancho
    elif ancho != '':
        ancho = float(ancho)/100
        tamano = ancho
    
    if(peso>0 or tamano > 0):
        if (peso * 72 >= tamano*72):
            costo = peso * 72
        else:
            costo = tamano *72
    else:
        costo = 48
    return costo

def darCostoLista(lista):
    costo = 0
    for i in lt.iterator(lista):
        obra = i['Obra']
        costo += darCostoObra(obra)
    return costo




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
    fecha1 = artwork1['Obra']['DateAcquired']
    fecha2 = artwork2['Obra']['DateAcquired']
    if fecha1 < fecha2:
        return True
    else:
        return False

def cmpArtistByDate(artist1, artist2):
    """
    Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de artwork2
    Args:
    artwork1: informacion de la primera obra que incluye su valor 'DateAcquired'
    artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired'
    """
    fecha1 = artist1['BeginDate']
    fecha2 = artist2['BeginDate']
    if fecha1 < fecha2:
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

def compararObrasPorCosto(artwork1, artwork2):
    artwork1 = artwork1['Obra']
    costo1 = darCostoObra(artwork1)
    artwork2 = artwork2['Obra']
    costo2 =darCostoObra(artwork2)
    if(costo1 > costo2):
        return True
    else:
        return False

def compararObrasPorVejez(artwork1, artwork2):
    artwork1 = artwork1['Obra']
    fecha1 = artwork1['Date']
    artwork2 = artwork2['Obra']
    fecha2 = artwork2['Date']
    if (fecha1 == ''):
        return False
    elif fecha2 == '':
        return True
    else:
        if(fecha1 < fecha2):
            return True
        else:
            return False
    
# Funciones de ordenamiento

def ordenarObrasPorFecha(inicial, final, catalog):
    lista = darObrasEnRangoFecha(catalog, inicial, final)
    lista= merge.sort(lista, cmpArtworkByDateAcquired)
    return lista

def ordenarListaNacionalidades(catalog):
    nacionalidades = crearListaNacionalidades(catalog)
    return merge.sort(nacionalidades, compararNacionalidades)

def ordenarArtistasPorFecha(inicial, final, catalog):
    lista = darArtistasEnRangoFecha(catalog, inicial, final)
    lista= merge.sort(lista, cmpArtistByDate)
    return lista

def ordenarObrasDepartamento(departamento, catalog):
    lista = darObrasDepartamento(departamento, catalog)
    lista = merge.sort(lista, compararObrasPorCosto)
    return lista

def ordenarObrasPorVejez(lista):
    lista = merge.sort(lista, compararObrasPorVejez)
    return lista
    

