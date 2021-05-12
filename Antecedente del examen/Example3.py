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

