evaluar = """ titulo: Experiences in Developing a Distributed Agent-based
Modeling Toolkit with Python
resumen: Distributed agent-based modeling (ABM) on high-performance
computing resources provides the promise of capturing unprecedented details
of large-scale complex systems. However, the specialized knowledge required
for developing such ABMs creates barriers to wider adoption and utilization.
Here we present our experiences in developing an initial implementation of
Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High
Performance Computing (Repast HPC), to identify the key elements of a useful
distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages
and the Python C-API to create a scalable modeling system that can exploit
the largest HPC resources and emerging computing architectures.
"""

lista=evaluar.split("resumen: ")
titulo=lista[0].split("titulo: ")
resumen=lista[1].split(".")
resumen=resumen[0:len(resumen)-1]
titulo=titulo[1].split()
if(len(titulo)<=10):
    print("El titulo cumple las especificaciones")
else:
    print("El titulo no cumple las especificaciones")
facil=0
acep=0
dif=0
muy_dif=0
for elem in resumen:
    ora=(len(elem.split()))
    if (ora<=12):
        facil+=1
    elif (ora>=13)and(ora<=17):
        acep+=1
    elif (ora>=18)and(ora<=25):
        dif+=1
    else:
        muy_dif+=1
print("Oraciones faciles: ",facil)
print("Oraciones aceptables: ",acep)
print("Oraciones dificiles: ",dif)
print("Oraciones muy dificiles: ",muy_dif)

