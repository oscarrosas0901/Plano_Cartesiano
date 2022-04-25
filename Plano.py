"""Programa para calcular el cuadrante de un plano cartesiano"""

print("----------------------------------------")
print("-----cuadrante de plano cartesiano------")
print("----------------------------------------")

#input

x = int(input("Ingresar coordenada en x"))
y = int(input("Ingresar coordenada en y")) 

#prosecing

if((x > 0) and (y > 0)):
    print("punto en el primer cuadrante")

elif((x < 0) and (y > 0)):
    print("punto en el segundo cuadrante")

elif((x < 0) and (y < 0)):
    print("punto en el tercer cuadrante")

elif((x > 0) and (y < 0)):
    print("punto en el cuarto cuadrante")

elif((x > 0 or x < 0) and (y == 0)):
    print("Esta en el eje X")

elif((y > 0 or y < 0) and (x == 0)):
    print("Esta en el eje Y")

elif((y == 0) and (x == 0)):
    print("Punto de origen") 
    
