"""
14. Faça um algoritmo que leia um conjunto de 30 valores. Para cada 
valor lido, coloque em uma lista P ou I, conforme os valores forem pares 
ou ímpares. O tamanho das listas P e I é de 10 posições.  Cada vez que 
encher uma das listas, (P ou I) esvazie-o, mostrando os valores que 
estavam na lista.  Cada lista P ou I pode ser preenchido quantas vezes 
forem necessárias. No final, mostre os valores que restaram em cada uma 
das listas. 
"""

def main():
    P=[]
    I=[]
    for i in range(1,31):
        n=int(input(f"Informe o {i}º número: "))
        if(n%2==0):
            P.append(n)
        else:
            I.append(n)
        if(len(P)==10):
            print(f"A lista P encheu e continha os seguintes valores: {P}")
            del P[:]
        if(len(I)==10):
            print(f"A lista I encheu e continha os seguintes valores: {I}")
            del I[:]
    print(f"Os números restantes na lista P é {P}")
    print(f"Os números restantes na lista I é {I}")

main()

