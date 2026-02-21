"""1. Faça um algoritmo que leia um lista de números V[6]. Contar a seguir, quantos valores de V são negativos 
e mostre essa informação. """

def verificador(lista,i=0,negativos=0,positivos=0):
    while(i<len(lista)):
        if lista[i]<0:
            negativos+=1
        else:
            positivos+=1
        i+=1
    print(f"A lista contendo {len(lista)} elementos\n{negativos} são negativos")
    print(f"{positivos} são positivos.")    

def main(i=0,lista=[]):
    while(len(lista)<6):
        i+=1
        n=int(input(f"Digite o {i}º valor de n: "))
        lista.append(n)
    verificador(lista)

main()
