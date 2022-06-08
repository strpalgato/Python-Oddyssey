#Un trabajador necesita calcular su sueldo semanal, el cual se obtiene de la sig. manera: 
#Si trabaja 48 horas o menos se le paga $X por hora 
#Si trabaja más de 48 horas se le paga $X por cada una de las primeras 40 horas y el doble del valor de la hora normal por cada hora extra trabajada.  
#Escriba algoritmo que ingrese número de horas trabajadas y valor a pagar por hora. Calcular y mostrar el total a recibir por la semana trabajada. 
Horas=int(input("Ingresar Horas trabajadas: "))
Sueldo=int(input("Ingresar el pago por hora: "))
if(Horas>48):
  Extras=(Horas-40)
  SueldoBase=(40*Sueldo)
  Extra=((2*Sueldo)*Extras)
  SueldoTotal=(SueldoBase+Extra)
  print("Su Valor extra es: $", Extra)
  print("Su Sueldo general mas los extras es: $",SueldoTotal)
if(Horas<=48):
  SueldoBase2=(Horas*Sueldo)
  print("Su Sueldo general es: $",SueldoBase2)