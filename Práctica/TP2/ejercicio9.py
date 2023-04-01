diccio = {
    "AEIOULNRST":1,
    "DG":2,
    "BCMP": 3,
    "FHVWY": 4,
    "K":5,
    "JX":8,
    "QZ":10
}

text = input("ingrese una palabra: ").upper()
resultado =0
claves=list(diccio.keys())
for elem in text:
    i=0
    ok=True
    while ((ok)and(i<len(claves))):
        if(elem in claves[i]):
            llave=claves[i]
            ok=False
        i+=1    
    resultado+=diccio[llave]

print("Hiciste ",resultado," puntos!")