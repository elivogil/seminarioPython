import string
ok=True
i=0
frase=input("Ingresar frase: ")
frase.lower()
letras=string.ascii_lowercase
while(ok)and(i<len(letras)):
    if (frase.count(letras[i])>1):
        ok=False
    i+=1
print("Es heterograma")if ok else print("No es heterograma")

