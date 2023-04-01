import string
jupyter_info = """ JupyterLab is a web-based interactive development
environment for Jupyter notebooks,
code, and data. JupyterLab is flexible: configure and arrange the user
interface to support a wide range
of workflows in data science, scientific computing, and machine learning.
JupyterLab is extensible and
modular: write plugins that add new components and integrate with existing
ones.
"""
words=jupyter_info.lower().split()
char=input("Ingresar letra").lower()
if(len(char)==1)and(char in string.ascii_letters):
    [print(pal)for pal in words if(pal.startswith(char))]
else: 
    print("No se ingreso una letra")