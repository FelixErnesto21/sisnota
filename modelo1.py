# Programa Pago de Bono

#1: Ingreso de Datos por el Usuario:
bono_general=float(input("Ingrese el valor del Bono General:"))
bono_eficiencia=float(input("Ingrese el valor del Bono de Eficiencia:"))

#2: Leer archivo
with open("Archivo nomina.txt","r",encoding = "utf-8") as nomina:
    nomina = nomina.readlines()

cedula=[]
ingreso=[]
empleado=[]
sueldo=[]
horas=[]

for i in nomina: 
    print(i)
    cedula.insert(0,i)

print("")
print(cedula)
    

    
