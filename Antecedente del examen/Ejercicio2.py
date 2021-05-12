print("Buen dia")
#Variables

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

#Datos de salida
print(f"Su bono es de: ${bonofinal:.2f}")
 