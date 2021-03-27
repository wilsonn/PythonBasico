for i in [1,2,3,4,5,"hola"]:
    print(i)

for i in range(5):
    print(i)

for i in ["pildoras", "informaticas",3]:
    print("hola", end=" ")
    
for i in "wilsonnm22@gmail.com":
    print(i)

email = False
miemail = input("Ingrese Email: ")
for i in miemail:
    if (i == "@"):
        email=True

if email:
    print("email correcto")
else:
    print("email incorrecto")

for i in range(5):
    print(f"Valor de la varible {i}")

for i in range(5,10):
    print(f"Valor de la varible {i}")

for i in range(5, 50, 10): #range (valor inicial, valor final -1 , incremento)
    print(f"Valor de la varible {i}")
