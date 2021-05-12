#inicio
print("Buenos dias estimado alumno")
#Variables
nota1=0
nota2=0
nota3=0
trabfin=0
notafinal=0
#Datos de entrada
Curso=input("Ingrese su curso:\nFP=Fundamento de programación\n")
nota1=float(input("Ingrese su nota de la unidad 1:"))
nota2=float(input("Ingrese su nota de la unidad 2:"))
nota3=float(input("Ingrese su nota de la unidad 3:"))
trabfin=float(input("Ingrese su nota del trabajo final:"))

#Proceso

if Curso=="FP":
  print("Su promedio de la unidad 1 es:",nota1*0.20)
  print("Su promedio de la unidad 2 es:",nota2*0.15)
  print("Su promedio de la unidad 3 es:",nota3*0.15)
  print("Su promedio de su trabajo final es:",trabfin*0.50)

if Curso=="FP":
  notafinal=(nota1*0.20)+(nota2*0.15)+(nota3*0.15)+(trabfin*0.50)
else:
  print("La opción que ingreso es incorrecto... Intenten nuevamente!.")

#Datos de salida
print("Entonces tu nota final es:",notafinal)


