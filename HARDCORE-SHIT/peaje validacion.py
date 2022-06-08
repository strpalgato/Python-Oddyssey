from os import system # Al escribir esto limpiamos la terminal
system("cls")         # cada vez que ejecutamos el programa.

#Primero que todo; defino algunas variables.

contV=1 #Contador de while principal en base a la cantidad de vehiculos ingresados.
mTotalEdadC=0 #Suma de las edades de los hombres que poseen camioneta.
mContAUTOS=0 #Total de automoviles que son manejados por hombres.
mContCAMIONETAS=0 #Total de camionetas que son manejadas por hombres. (Se requiere para sacar el promedio)
fContCamionetas2005=0 #Contador de motomamis 2005.
totalMotos=0 #total motos 1999-2001.
totaldinero=0 #total de dinero ganado en el peaje.
totaldin2=0 #total de dinero ganado solo por automoviles con dueños menores de 34 años.
edadmayor=0 #persona con mas edad.
lista=[] #registra las edades de las personas.
sexMayor="" #rescata el sexo de la persona con mayor edad.
vehMayor="" #rescata el tipo de veh de la persona con mayor edad.
edadBackup="" #rescata una copia de la "edad mayor" más reciente. (Osea que; si la edad de un conductor posterior supera a la del anterior, se sobrescribe) (Si no supera la edad anterior, se mantiene)

#En lo personal, me gusta utilizar el while(True) cuando se me da la oportunidad, ya que este no depende de contadores.
#Basicamente este tipo de while; termina cuando se cumple una condicion mediante el uso del "break".
#En cambio un while con contador; termina cuando se cumple "x" cantidad de vueltas/rondas designadas mediante una variable. Por ejemplo: (round<="10")  ##Eso significa 10 rounds, por lo tanto el while termina en el round numero "10".

#A continuacion, la >introduccion< al codigo.

while(True): #Se realiza una validacion de digitos, ya que es ilogico trabajar numeros negativos, decimales y caracteres.
    try: #El "try"; como su nombre lo dice; intenta obtener el mejor resultado posible. Osea que; le pedirá los datos necesarios al usuario infinitamente; hasta que este se vea obligado a introducirlos de la manera en que se le pide. (DE LA MANERA CORRECTA)
        cantVeh=int(input("Introduzca la cantidad de vehiculos con los que desea trabajar: "))
        if(cantVeh>0): #Si la cantidad de vehiculos es MAYOR que 0...
            break      #Se utiliza el break ligado a la condicional para finiquitar este while y pasar al siguiente. Si no se utiliza el break, el while se loopeara infinitamente y solamente en este sector.
        elif(cantVeh<0): #Si la cantidad de vehiculos NO es mayor que 0...
            print("Error, el digito ingresado debe ser positivo") #Esta condicional sirve para cuando se introduce un numero negativo.
        else: #Por descarte, esta condicional corresponde a "=0", por lo tanto: Si la cantidad de vehiculos es IGUAL a 0...
            print("Error, el digito ingresado debe ser positivo") #A simple vista se ve innecesario; pero debemos recordar que el numero 0; NO ES NI NEGATIVO NI POSITIVO, ES NEUTRO.    
    except ValueError: #El ValueError se utiliza para que el programa no crashee/dropee, entonces asi el usuario no tendra que ejecutarlo de nuevo. Esta condicional se activa; en esta ocasion por ejemplo; cuando se introduce un caracter, string o numeros decimales; en vez de numeros enteros (int).
        print("Error, debe ingresar el valor en numeros enteros")

#A continuacion, el >desarrollo< del codigo.

while(contV<=cantVeh): #Este es el while principal y depende de un contador; el cual va ligado a la cantidad de vehiculos ingresados.
    print("Vehiculo numero: {}".format(contV)) #Le muestro al usuario cual es el vehiculo que esta trabajando, como si de un ticket se tratase (ticket #1, ticket #2, etc).
    while(True): #Este while cumple la misma funcion que el while de la >introduccion<. En esta ocasion se realiza una validacion de edad, ya que es ilogico introducir digitos en negativo, caracteres o menores de edad.
        try:
            edadC=int(input("Ingrese la edad del conductor: "))
            if(edadC>=18): #Aqui la unica restriccion es que el conductor deba ser mayor de 18, pero eso me hace preguntar; ¿que pasaria si alguien introduce sin querer a alguien con 300 años? ;)
                lista.append(edadC) #se agrega el valor a la lista de edades.
                break   
            else:
                print("Error, debe ingresar una edad valida")
                continue #El "continue" se encarga de solicitarle nuevamente al usuario; el dato que se esta pidiendo; tomando el "input" del principio como referencia. Así no se tiene que reiniciar el programa para poder introducirlo de manera correcta y además no se pierde el progreso.
        except ValueError:
            print("Error, debe ingresar la edad en numeros enteros")
            continue
    edadmayor=max(lista) #con esta funcion se rescata el num mayor de la lista.
    edadBackup=edadmayor
    while(True): #Se realiza una validacion del sexo del conductor, ya que solamente esta permitido registrar si es femenino o masculino.          
        try:
            sexoC=input("Ingrese el sexo del conductor (F: Femenino / M: Masculino): ").upper() #El .upper() se encarga de transformar la respuesta del usuario; en mayusculas. (Por si escribe "f" o "m"; en vez de "F" o "M")
            if(sexoC=="F") or (sexoC=="M"):
                break
            else:
                print("Error, debe ingresar si es femenino (F) o masculino (M) para proseguir")
                continue
        except ValueError:
            print("Error, debe ingresar las letras correspondientes, no se admiten numeros")
            continue
    if(edadBackup==edadC): #Dependiendo de si la "edadbackup" es igual o no a la "edadC", se sobrescribe la variable.
        sexMayor=sexoC
    while(True): #Se realiza una validacion del tipo de vehiculo, ya que solamente esta permitido registrar si es auto, camioneta o moto.
        try:
            TipoV=input("Ingrese el tipo de vehiculo (A: Automovil / C: Camioneta / M: Moto): ").upper()
            if(TipoV=="A") and (sexoC=="M"):
                mContAUTOS+=1
                break
            elif(TipoV=="A") and (sexoC=="F"):
                break
            elif(TipoV=="C") and (sexoC=="M"):
                mTotalEdadC+=edadC
                mContCAMIONETAS+=1
                break
            elif(TipoV=="C") and (sexoC=="F"):
                break
            elif(TipoV=="M") and (sexoC=="M"):
                break
            elif(TipoV=="M") and (sexoC=="F"):
                break
            else:
                print("Error, ingrese las siglas que son validas")
                continue
        except ValueError:
            print("Error, debe ingresar las letras correspondientes, no se admiten numeros")
            continue
    if(edadBackup==edadC): #Dependiendo de si la "edadbackup" es igual o no a la "edadC", se sobrescribe la variable.
        vehMayor=TipoV
    while(True): #Se realiza la validacion del año del vehiculo, con un rango simple.
        try:
            aVeh=int(input("Ingrese el año del vehiculo (1980-2006): "))
            if(aVeh<1980) or (aVeh>2006):
                print("Error, el año ingresado se encuentra fuera de rango o no es valido")
                continue
            if(aVeh>=1980) and (aVeh<=2006):
                break
        except ValueError:
            print("Error, los digitos ingresados deben ser numeros enteros")
    
    #A continuacion se programa el total de la tarifa estipulada en base al tipo de vehiculo y el año del vehiculo.

    if(TipoV=="A") and (aVeh>1998):
        totaldinero+=1000
        print("Este vehiculo debe pagar $1000")
    if(TipoV=="A") and (aVeh<=1998):
        totaldinero+=800
        print("Este vehiculo debe pagar $800")
    if(TipoV=="C") and (aVeh>1998):
        totaldinero+=1200
        print("Este vehiculo debe pagar $1200")
    if(TipoV=="C") and (aVeh<=1998):
        totaldinero+=1000
        print("Este vehiculo debe pagar $1000")
    if(TipoV=="M") and (aVeh>1998):
        totaldinero+=600
        print("Este vehiculo debe pagar $600")
    if(TipoV=="M") and (aVeh<=1998):
        totaldinero+=400
        print("Este vehiculo debe pagar $400")

    #A continuacion se calculan los valores a sumar; para los contadores de la informacion solicitada que todavia no hemos tocado.

    if(aVeh==2005) and (TipoV=="C") and (sexoC=="F"):   
        fContCamionetas2005+=1 #contador de camionetas del 2005 manejadas por mujeres 
    if(aVeh>=1999) and (aVeh<=2001) and (TipoV=="M"):
        totalMotos+=1 #cantidad total de motos entre 1999 y 2001
    if(TipoV=="A") and (sexoC=="M") and (edadC<34) and (aVeh>1998):
        totaldin2+=1000 #total recaudado por automóviles, manejados por hombres, menores a 34 años. 
    if(TipoV=="A") and (sexoC=="M") and (edadC<34) and (aVeh<=1998):
        totaldin2+=800 #tambien; total recaudado por automóviles, manejados por hombres, menores a 34 años. 
    while(True): #Se realiza la validacion de la patente (formato simple, ya que faltan los conocimientos necesarios para obligar al usuario 2 caracteres y 3 numeros)
        try:
            patente=input("Introduzca la patente del vehiculo: ")
            longitud=len(patente) #La funcion "len", se encarga de contar la cantidad de caracteres que posee una str, por ejemplo las patentes de vehiculos chilenos poseen 5 cifras.
            if(longitud==5):      #Si se cumplen las cifras, se finiquita este while.
                break
            else:
                print("Error, la patente ingresada no es valida o no cumple con tener 5 cifras")
        except ValueError:
            print("Error, la patente solo debe poseer letras")
    contV+=1

if(mContCAMIONETAS!=0): #Por que usar un if para calcular el promedio? Facil; si el divisor es igual a 0, el programa se cae y no hay como salvarlo.
    promedio=float(mTotalEdadC/mContCAMIONETAS) #Entonces es mejor dejar como condicion: Si es DISTINTO de 0 se realiza la operacion; sino; no se realiza nada.

#A continuacion, el >fin< del codigo. (Se imprimen los resultados)

print("---------------------------------------------------------------------------------------------------------------------------------------------------------------") #Estetica
print("") #Estetica
print("* Dinero total recaudado: ${}".format(totaldinero))
print("* Cantidad de camionetas conducidas por mujeres (2005): {}".format(fContCamionetas2005))
print("* Total de motos (1999-2001): {}".format(totalMotos))
print("* Cantidad total de automoviles (hombres): {}".format(mContAUTOS))
print("# Lista de edades: {}".format(lista))
print("* La persona con mayor edad es de {} años; posee un vehiculo de tipo {} y su género es {}".format(edadmayor,vehMayor,sexMayor))
if(mContCAMIONETAS!=0): #Tomar en consideracion la linea 149 del codigo.
    print("* Promedio de edades de hombres que manejan camionetas: {}".format(promedio))
else:
    print("- No se pudo obtener el promedio de edades (hombres que manejan camionetas), ya que el total de camionetas es 0. (la division entre cero no está permitida)")
print("* Total recaudado por automóviles, manejados por hombres, menores a 34 años: ${}".format(totaldin2))
print("") #Estetica
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------") #Estetica