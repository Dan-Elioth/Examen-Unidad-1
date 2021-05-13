def ejercicio1DECP():
    
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

#ejercicio1DECP()

def ejercicio2DECP():
  print("Buen dia")
  #Variables
  bonofinal=0
  salariomin=930
  #Datos de entrada
  puntos=int(input("Ingrese los puntos que obtuvo por su desempeño laboral:" ))
  salariomin=int(input("Ingrese el sueldo minimo:\nTeniedo en cuenta que el salario minimo en el Perú es de=930\n"))
  #Proceso
  if puntos>=50 and puntos<=100:
    bonofinal=salariomin*0.10
  elif puntos>=101 and puntos<=150:
    bonofinal=salariomin*0.40
  elif puntos>=151:
    bonofinal=salariomin*0.70
  else:
    print("Estimado Docente, le pido que ponga mas esfuerzo a su labor" )

  #Datos de salida
  print(f"Su bono es de: ${bonofinal:.2f}")

#ejercicio2DECP()

def ejercicio3DECP():
  print("Buen dia. Bienvenido al programa de vacunción por parte del Misnisterio de Salud, este programa esta vinculado al marco del Covid-19, porfavor siga instrucciones y posteorimente se le dira que vacuna recibirá")
  #Variables
  vacuna1="A"
  vacuna2="B" 
  vacuna3="C"
  #Datos de entrada
  años=int(input("Porfavor Ingrese su edad: "))
  sexo=input("Que sexo es:\nH=Hombre\nM=Mujer\n")
  #Proceso
  if años>=70:
    VacunaFi=vacuna3
  if años>=16 and años<=69 and sexo=="M":
    VacunaFi=vacuna2
  else:
    VacunaFi=vacuna1
  if años<16:
    VacunaFi=vacuna1
  #Datos de salida
  print("La vacuna que se le administrara es tipo ",VacunaFi)

#ejercicio3DECP()

def ejercicio4DECP():
  print("Hola humano")
  print("Ingrese solamente dos numeros")
  #Variables
  res=0
  #Datos de entrada
  num1=int(input("Ingres el primer numero:"))
  num2=int(input("Ingrese el segundo numero:"))
  opcion=input("Hey humano elije que operacion quieres que haga:\ns=Suma\nr=Resta\nm=Multplicacion\nd=Divicion\n")
  #Proceso
  opcion=opcion.lower()
  if opcion=="s":
    res=num1+num2
  elif opcion=="r":
    res=num1-num2
  elif opcion=="m":
    res=num1*num2
  if opcion=="d":
    if num2!=0:
      res=num1/num2

  #Datos de salida
  print(f"Aqui esta tu resultado humano: {res}")

#ejercicio4DECP()

def ejercicio5DECP():
  #Variables
  prueba=0

  #Datos de entrada

  opcion=input("Ingrese el algoritmo que quiere probrar:\n1=ejercicio1DECP1\n2=ejercicio1DECP2\n3=ejercicio1DECP3\n4=ejercicio1DECP4\n")
  #Proceso
  if opcion=="1":
    prueba=ejercicio1DECP()
  if opcion=="2":
    prueba=ejercicio2DECP()
  if opcion=="3":
    prueba=ejercicio3DECP()
  if opcion=="4":
    prueba=ejercicio4DECP()
  #Datos de salida
print("Tu algoritmo de prueba es:")

ejercicio5DECP()






  

