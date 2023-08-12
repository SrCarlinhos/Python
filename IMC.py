from os import system

peso = float(input("Qual o seu peso?"))
altura = float(input("Qual a sua altura?"))

imc =  peso / altura**2

print("O seu imc: %f" % imc)
system("pause")