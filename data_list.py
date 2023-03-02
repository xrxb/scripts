#guarda en variable files el nombre de todos los elementos que hay
##dentro de la carpeta que le indiques
#comprueba que cada elemento sea un archivo y guarda en una lista
##el SN del equipo filtrado con una comprobación regex
#crea una carpeta con todos los SN de la lista en caso de que no existan
#mueve todos los archivos de la carpeta principal a sus carpetas filtrando
##por el nombre del archivo
#-el archivo '"C:\Windows\A021664A_F.xml'
#-lo moverá a la carpeta 'A021664A_F'

import shutil
import os
import re
 
file_source = r'C:\Windows'
 
files = os.listdir(file_source)
dut_list=[]
#input('x')
for y in files:
    #input(y)
    if os.path.isfile(os.path.join(file_source, y)):
        #print(y)
        new = re.findall(r'[A][0-9]{6}[A].[F][M][0-9]{1}', y)
        new=new[0]
        if new not in dut_list:
            dut_list.append(new)
    
for x in dut_list:
    #dut=input("DUT: ")
    dut=os.path.join(file_source, x)
    if not os.path.exists(dut):
                os.mkdir(dut);
                print(dut+' folder created')

for x in dut_list:
    for g in files: 
        #print(g)
        if x in g:
            new_directory=os.path.join(file_source, x)
            gg=os.path.join(file_source, g)
            if os.path.isfile(gg):
                shutil.move(gg, new_directory)
                #print(g+ ' moved in '+new_directory)
                print(gg+ ' moved in '+new_directory)

for x in dut_list:
    new_directory=os.path.join(file_source, x)
    tfiles = os.listdir(new_directory)
    y=len(tfiles)
    print(f'{x} total files: {y}')

    
#contar los archivos de cada carpeta creada
