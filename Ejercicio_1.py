import random
N = random.randint(1,20)

print("Hola, ¿Como te llamas?")
nombre = input()

print("Muy bien" , nombre , ", adivina el numero entre 1 y 20")

print(N)
z = 0

X = int(input())

while X != N:
    if X < N:
        print("Tu numero es muy bajo")
        z += 1
        X = int(input(""))
    elif X > N:
        print("Tu numero es muy alto")
        z += 1
        X = int(input(""))
    elif X == N:
        print("Acertaste!!")


print("Buen trabajo" , nombre , "\n Acertaste en" , z , "intentos.")