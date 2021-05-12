print("Hola humano")
print("Ingrese solamente dos numeros")
#Variables
res=0
#Datos de entrada
num1=int(input("Ingres el primer numero:"))
num2=int(input("Ingrese el segundo numero:"))
opcion=input("Hey humano elije que operacion quieres que haga:\nS s=Suma\nR r=Resta\nM m=Multplicacion\nD d=Divicion\n")
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
else:
  print("Elije bien pues humano, no seas paltas")

#Datos de salida
print(f"Aqui esta tu resultado humano: {res}")

