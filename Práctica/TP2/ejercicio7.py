import string
texto = """
El salario promedio de un hombre en Argentina es de $60.000, mientras que
el de una mujer es de $45.000. Además, las mujeres tienen menos
posibilidades de acceder a puestos de liderazgo en las empresas.
"""
lista=texto.split()
may=[]
minu=[]
char=[]
for elem in lista:
    if elem[0] in string.ascii_uppercase:
        may.append(elem)
    elif elem[0] in string.ascii_lowercase:
        minu.append(elem)
    else:
        char.append(elem) 

pal=len(lista)
pal_sin=len(may)+len(minu)
print("Cantidad de palabras: ",pal)
print("Cantidad de palabras solo con letras: ",pal_sin)