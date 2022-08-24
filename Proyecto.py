import csv  #modulos para trabajar con archivos .csv
#################LISTAS A UTILIZAR###########################
imports20=[];imports80=[];exports20=[];exports80=[]
exportsF=[];exportsT=[];importsF=[];importsT=[];valueE=[]
valueI=[];countryExports=[];countryImports=[];importsProm=[]
exportsProm=[];transportI=[];transportE=[];Rute=[];red=[]
RuteI=[];redI=[];

##################33CONSTANTES DEL PROGRAMA###################
usuarios = ['emtech','emtech1','Jesus','Carlos']
contraseñas = ['caso1','caso2']
registro ='si'
porcentajeGabnanciaExp=0.8
porcentajeGabnanciaImp=0.8
########FUNCION PARA OBTENER USUARIO Y CONTRASEÑA CORRECTAS####
def login(usuario,contraseña):
    if usuario in usuarios:
      if contraseña in contraseñas[indice]:
          return 1
      else:
          print("\n\tCONTRASEÑA INCORECTA\n")
    elif(usuario not in usuarios):
      print('No existe')
      return 2
    else:
      print('No existe')
      return 2
 
while registro == 'si':
  usuario=input('Ingrese nombre de usuario: ')
  if usuario not in usuarios:
      print('USUARIO INCORRECTO')
  else:
    indice = usuarios.index(usuario)
 
    if indice > (len(contraseñas)-1):
        print('No tiene permiso de adminisrador\n')
    else:
        contraseña = input("Contraseña: ")
   
        if login(usuario,contraseña)==1:
           print('\nBIENVENIDO!! ')
           registro = 'no'
    ##############TRABAJANDO CON ARCHIVO CSV########### 
    ##########ABRIR ARCHIVO Y CREAR OBJETO LECTOR############
           with open('synergy_logistics_database.csv','r') as archivo_csv:
             lector = csv.reader(archivo_csv)
          
######CREANDO LISTAS DE EXPORTACION E IMPORTACION#########        
             for linea in lector:
                 if linea[1] == 'Exports':
                     exportsF.append(linea[2])#ORIGEN DE EXPORTACION
                     exportsT.append(linea[3])#DESTINO DE LA EXPORTACION 
                     valueE.append(int(linea[9]))#VALOR DE LA EXPORTACION
                     transportE.append(linea[7])#TRANSPORTE
                 if linea[1] == 'Imports':
                     importsF.append(linea[2])#ORIGEN DE IMPORTACION 
                     importsT.append(linea[3])#DESTINO DE LA IMPORTACION
                     valueI.append(int(linea[9]))#VALOR DE LA IMPORTACION
                     transportI.append(linea[7])#TRANSPORTE
           #######AGRUPOANDO DATOS DE EXPORTACION E IMPORTACION#######
             exports=list(zip(exportsF, exportsT))#LISTA CON RUTA DE LA EXPORTACION
             exportss=list(zip(exports,valueE))#LISTA CON RUTA Y VALOR DE LA EXPORTACIO
             exportsT=dict(zip(exports, transportE))
             exportss.sort()#ORDENAR DE MAYOR A MENOR
             
             imports=list(zip(importsF, importsT))#LISTA CON RUTA DE LA IMPORTACIO
             importss=list(zip(imports,valueI))#LISTA CON RUTA Y VALOR DE LA IMPORTACIO
             importsT=dict(zip(imports, transportI))
             importss.sort()#ORDENAR DE MAYOR A MENOR
             
             exports,valueE=zip(*exportss)
             imports,valueI=zip(*importss)
        
             w=0
             z=0
    #####AGRUPANDO POR RUTA DE ESPORTACION E IMPORTACION####
             for linea in exports:
                if linea not in countryExports:
                    exportsProm.append(z)
                    z=0
                    countryExports.append(linea)
                    z=valueE[w]
                else:
                    z=int(valueE[w])+int(z)
                    
                w=w+1
             exportsProm.append(z)
             exportsProm.remove(0)
             exports=(list(zip(countryExports, exportsProm)))
             exports.sort(reverse=True, key= lambda x:x[1])
        
        
             x=0
             y=0
             for linea in imports:
                 if linea not in countryImports:
                     countryImports.append(linea)
                     importsProm.append(y)
                     y=0
                     y=valueI[x]
                 else:
                     y=int(valueI[x])+int(y)
                 x=x+1
                 
    
             importsProm.append(y)
             importsProm.remove(0)
             imports=(list(zip(countryImports,importsProm)))
             imports.sort(reverse=True, key=lambda x:x[1])
     ######IMPRIMIENDO LAS 10 MEJORES RUTAS EXP/IMP        
             print('RUTAS CON MAYORES EXPORTACIONES:')
             for list in range(10):
                  print(exports[list])
             print()
             print('RUTA CON MAYORES IMPORTACIONES:')
             
             for list in range(10):
                  print(imports[list])
      #####CALCULANDO EL 80% DE LAS IMPORTACIONES CON SUS RUTAS       
             totalE=(sum(valueE))*porcentajeGabnanciaExp
             totalI=(sum(valueI))*porcentajeGabnanciaImp          
      #######CREANDO LAS LISTAS DE LAS RUTAS QUE GENERAN EL 80% DE LAS GANANCIAS       
             r=0
             for list in exports:
                 if r <= totalE:
                      r=list[1]+r
                      exports80.append(list)
                      red.append(exportsT[list[0]])
                 else: 
                      exports20.append(list)
                      Rute.append(exportsT[list[0]])
             
             s=0
             for list in imports: 
                if s <= totalI:
                  s=list[1]+s
                  imports80.append(list)
                  redI.append(importsT[list[0]])
                else: 
                  imports20.append(list)
                  RuteI.append(importsT[list[0]])
             
#######IMPRESION DE LOS DATOS DE TRANSPORTE              
             sea = red.count("Sea")     
             air = red.count("Air")     
             rail = red.count("Rail")     
             road = red.count("Road")     
             sea20 = Rute.count("Sea")     
             air20 = Rute.count("Air")     
             rail20 = Rute.count("Rail")     
             road20 = Rute.count("Road")     
             
             print('\nTRANSPORTE DEL 80% DE LAS GANANCIAS EXPORTADAS')
             print('Viajes por mar:',sea)
             print('Viajes por aire:',air)
             print('Viajes por tren:',rail)
             print('Viajes por carretera:',road)
 
             print('\nTRANSPORTE DEL 20% DE LAS GANANCIAS EXPORTADAS')
             print('Viajes por mar:',sea20)
             print('Viajes por aire:',air20)
             print('Viajes por tren:',rail20)
             print('Viajes por carretera:',road20)    
             
             seaI = redI.count("Sea")     
             airI = redI.count("Air")     
             railI = redI.count("Rail")     
             roadI = redI.count("Road")     
             sea20I = RuteI.count("Sea")     
             air20I = RuteI.count("Air")     
             rail20I = RuteI.count("Rail")     
             road20I = RuteI.count("Road")     
             print('\nTRANSPORTE DEL 80% DE LAS GANANCIAS IMPORTADAS')
             print('Viajes por mar:',seaI)
             print('Viajes por aire:',airI)
             print('Viajes por tren:',railI)
             print('Viajes por carretera:',roadI)
 
             print('\nTRANSPORTE DEL 20% DE LAS GANANCIAS IMPORTADAS')
             print('Viajes por mar:',sea20I)
             print('Viajes por aire:',air20I)
             print('Viajes por tren:',rail20I)
             print('Viajes por carretera:',road20I)   
   #######CONTRASEA INCORRECTA              
        else:
                print('Incorrecto')
 
                
     