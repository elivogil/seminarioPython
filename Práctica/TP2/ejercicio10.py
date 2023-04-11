def String_a_List(nombres):
    """ Recibo un string de nombres, le quito los " ", "'" y "\n", y los devuelvo en una lista """
    nombres = nombres.replace("\n", "")
    nombres = nombres.replace(" ", "")
    nombres = nombres.replace("'", "")
    return nombres.split(',')

def armar_zip(nombres,notas_1,notas_2):
    """ A partir de tres listas formo un diccionario, siendo la lista de nombres las claves, 
    y las dos listas de notas los valores guardados en una lista """
    return{i:[j,k] for i,j,k in zip(nombres,notas_1,notas_2)}
    
def sacar_promedios(notas_agrupadas):
    """ Con esta funcion recibo un diccionario, y a partir de los valores devuelvo una lista con el promedio de cada alumno """
    return map(lambda clave:sum(notas_agrupadas[clave])/2,notas_agrupadas)
       
def prom_total(promedios):
    """ Recibo un diccionario y devuelvo el promedio de todos los promedios """
    return (sum(promedios.values())/len(promedios))

def max_prom(promedios):
    """ Esta funcion retorna el mayor promedio que se encuentra en el diccionario """
    return max(promedios,key=promedios.get)

def min_nota(notas_agrupadas):
    """ Esta funcion retorna la menor nota del diccionario """
    return min(notas_agrupadas,key=lambda x:min(notas_agrupadas[x]))   

nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín'  , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 
'Nicolás',  'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''

notas_1 = [81,  60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 
           12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 
           85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
           64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
           95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]


""" Inciso a: armo un diccionario usando la funcion armar_zip """
notas_agrupadas= armar_zip(String_a_List(nombres),notas_1,notas_2)

""" Inciso b: genero un diccionario usando las claves del diccionario "notas_agrupadas", y el promedio de las notas  """
promedios={i:j for i,j in zip(notas_agrupadas,sacar_promedios(notas_agrupadas))}
print('Promedios por alumnos: ',promedios)

""" Inciso c: imprimo el promedio del curso, calculado por la funcion prom_total """
print(f"El promedio total del curso: {prom_total(promedios)}")

""" Inciso d: imprimo el promedio mas alto, calculado por la funcion max_prom """
print(f"Alumno con la nota promedio mas alta: {max_prom(promedios)}")

""" Inciso e: imprimo la nota mas baja, calculado por la funcion min_nota """
print(f"Alumno con la nota mas baja: {min_nota(notas_agrupadas)}")

